"""
Script con utilidades para extraer datos de la web de las ligas de balonmano de
gipuzkoa:

    https://www.gieskubaloia.eus/es/competicion/resultados-clasificaciones/
    
Se descargan también los logos de los equipos así como las actas de los
partidos. Estas actas se leen también para obtener información de los
jugadores.

Los archivos de actas y logos se descargan en una carpeta files dentro del path
donde se ejecuta el script. Dentro de esta habrá una carpeta para cada liga y a
su vez una carpeta "actas" y otra "logos" para cada liga.

La forma típica de ejecutar el script sería:
    
    python3 scrape_web.py -o info_ligas.json --update-actas --ncores 8

Esto descargará los datos de las ligas, los logos y los actas de los partidos.
Hecho eso se leerán los pdfs (usando 8 núcleos) y se extraerán los datos de los
jugadores. Finalmente guardará toda la información de todas las ligas en el
archivo info_ligas.json.

Cuando se parsean los pdf van apareciendo mensajes de información del partido
que se está parseando y algunos mensajes de advertencia que no son importantes.
"""
from typing import Any, Dict, List, Tuple, TypedDict
import requests, os, asyncio
from concurrent.futures import ThreadPoolExecutor

from requests_html import HTMLSession, AsyncHTMLSession, HTML
import pandas as pd
import tabula
import textract


class DescansoInfo(TypedDict):
    fecha: str
    equipo_id: str


class PartidoInfo(TypedDict):
    fecha: str
    hora: str
    lugar: str
    equipo_local_id: str
    equipo_visitante_id: str
    goles_local: int
    goles_visitante: int
    acta_path: str
    goles_por_jugador: Dict[str, int]


class JornadaInfo(TypedDict):
    numero: int
    fecha: str
    descansos: List[DescansoInfo]
    partidos: List[PartidoInfo]


class JugadorInfo(TypedDict):
    nombre: str
    apellidos: str
    dorsal: int


class EquipoInfo(TypedDict):
    nombre: str
    logo: str
    jugadores: List[JugadorInfo]


class LigaInfo(TypedDict):
    nombre: str
    jornadas: List[JornadaInfo]
    equipos: Dict[str, EquipoInfo]


class Liga:
    def __init__(self, nombre: str, req_html: HTML):
        self.nombre = nombre
        self.equipos: Dict[str, Equipo] = {}

        path = os.path.join("files", self.id_name)
        if not os.path.exists(path):
            os.mkdir(os.path.join(path))
        if not os.path.exists(os.path.join(path, "actas")):
            os.mkdir(os.path.join(path, "actas"))
        if not os.path.exists(os.path.join(path, "logos")):
            os.mkdir(os.path.join(path, "logos"))

        self.jornadas = [
            Jornada(div, self) for div in req_html.find(".card.card__partidos")
        ]

    def __str__(self) -> str:
        return "Liga: " + self.nombre

    def __repr__(self) -> str:
        return self.__str__()

    def update_actas(self):
        print("Actualizando actas de la liga: " + self.nombre)
        for jornada in self.jornadas:
            jornada.update_actas()

    @property
    def id_name(self) -> str:
        return (
            self.nombre.lower()
            .replace(" - ", "_")
            .replace(" ", "_")
            .replace("ª", "")
            .replace("º", "")
            .replace(".", "")
        )

    @property
    def info(self) -> LigaInfo:
        return {
            "nombre": self.nombre,
            "jornadas": [j.info for j in self.jornadas],
            "equipos": {nom: e.info for nom, e in self.equipos.items()},
        }

    @classmethod
    def from_info(cls, info: LigaInfo) -> "Liga":
        liga = cls.__new__(cls)
        liga.nombre = info["nombre"]
        liga.jornadas = [Jornada.from_info(j, liga) for j in info["jornadas"]]
        liga.equipos = {
            nom: Equipo.from_info(e, liga) for nom, e in info["equipos"].items()
        }
        return liga


class Jornada:
    def __init__(self, card_div: HTML, liga: Liga):
        header = card_div.find(".card__header", first=True).find("a", first=True).text
        self.numero = int(header.split(" ")[1])
        self.fecha = header.split(" ")[-1].strip()[1:-1]
        self.descansos = []
        self.partidos = []
        self.liga = liga
        self.parse_rows(card_div)

    def __str__(self) -> str:
        return f"Jornada {self.numero} ({self.fecha}): {self.liga}"

    def __repr__(self) -> str:
        return self.__str__()

    def parse_rows(self, card_div: HTML):
        rows = card_div.find(".row")
        date = None
        metas = None
        for row in rows:
            if "date" in row.attrs["class"]:
                date = row.find("span", first=True).text
            elif "partido" in row.attrs["class"]:
                if metas is not None:
                    self.partidos.append(Partido(row, metas, date, self.liga, self))
                    metas = None
                else:
                    self.descansos.append(Descanso(row, date, self.liga, self))
            elif "metas" in row.attrs["class"]:
                metas = row

    def update_actas(self):
        for partido in self.partidos:
            partido.update_acta()

    @property
    def info(self) -> JornadaInfo:
        return {
            "numero": self.numero,
            "fecha": self.fecha,
            "descansos": [d.info for d in self.descansos],
            "partidos": [p.info for p in self.partidos],
        }

    @classmethod
    def from_info(cls, info: JornadaInfo, liga: Liga) -> "Jornada":
        jornada = cls.__new__(cls)
        jornada.numero = info["numero"]
        jornada.fecha = info["fecha"]
        jornada.liga = liga
        jornada.descansos = [
            Descanso.from_info(d, liga, jornada) for d in info["descansos"]
        ]
        jornada.partidos = [
            Partido.from_info(p, liga, jornada) for p in info["partidos"]
        ]
        return jornada


class Descanso:
    def __init__(self, row: HTML, date: str, liga: Liga, jornada: Jornada):
        self.fecha = date
        self.liga = liga
        self.jornada = jornada

        sitios = row.find(".fichaEquipo")
        index = ["DESCANSO" in sitio.text for sitio in sitios].index(False)
        sitio = sitios[index]

        nombre = sitio.find(".equipo", first=True).text.title()
        try:
            logo = sitio.find(".logo", first=True).find("img", first=True).attrs["src"]
            logo_file = (
                f"./files/{self.liga.id_name}/logos/"
                + nombre.lower().replace(" ", "_")
                + ".jpg"
            )
            check_and_download(logo, logo_file)
        except AttributeError:
            logo_file = None

        equipo_obj = Equipo(nombre, liga, logo=logo_file)
        if equipo_obj.id_name not in self.liga.equipos:
            liga.equipos[equipo_obj.id_name] = equipo_obj
        self.equipo_id = equipo_obj.id_name

    def __str__(self) -> str:
        return f"Descanso {self.equipo} ({self.jornada})"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def equipo(self) -> "Equipo":
        return self.liga.equipos[self.equipo_id]

    @property
    def info(self) -> DescansoInfo:
        return {
            "fecha": self.fecha,
            "equipo_id": self.equipo_id,
        }

    @classmethod
    def from_info(cls, info: DescansoInfo, liga: Liga, jornada: Jornada) -> "Descanso":
        descanso = cls.__new__(cls)
        descanso.fecha = info["fecha"]
        descanso.liga = liga
        descanso.jornada = jornada
        descanso.equipo_id = info["equipo_id"]
        return descanso


class Partido:
    def __init__(self, row: HTML, metas: HTML, date: str, liga: Liga, jornada: Jornada):
        self.liga = liga
        self.jornada = jornada
        self.fecha = date
        self.hora, self.lugar = [item.text for item in metas.find(".col")[:2]]

        self.equipo_local_id = self.init_equipo(row.find(".col")[0])
        self.equipo_visitante_id = self.init_equipo(row.find(".col")[2])
        try:
            self.goles_local, self.goles_visitante = [
                int(item) for item in row.find(".col")[1].text.split("-")
            ]
        except ValueError:
            self.goles_local, self.goles_visitante = -1, -1

        acta_url = row.find(".acta", first=True).attrs.get("href", None)
        if acta_url is None or acta_url[-3:] != "pdf":
            self.acta_path = None
        else:
            dia = self.fecha.split()[0].replace("/", "-")
            nombre_local = self.equipo_local.nombre.lower().replace(" ", "_")
            nombre_visitante = self.equipo_visitante.nombre.lower().replace(" ", "_")
            self.acta_path = f"./files/{self.liga.id_name}/actas/{dia}_{nombre_local}_{nombre_visitante}.pdf"
            check_and_download(acta_url, self.acta_path)
        self.goles_por_jugador = {"local": {}, "visitante": {}}

    def __str__(self) -> str:
        return f"Partido ({self.fecha}): {self.resultado}"

    def __repr__(self) -> str:
        return self.__str__()

    def update_acta(self):
        if (self.acta_path is None) or (self.resultado == "Partido no jugado"):
            return

        print(f"Actualizando acta de: {self}")
        info_partido = extract_pdf(self.acta_path)
        # Comprobamos que los equipos parseados coinciden con los de la web
        web_ids = (self.equipo_local_id, self.equipo_visitante_id)
        if web_ids != tuple(info_partido.keys()):
            # Si no coinciden probamos un metodo mas costoso
            lines = [
                l.lower().replace(
                    " ",
                    "_",
                )
                for l in get_pdf_lines_no_number(self.acta_path)
            ]
            if web_ids[0] in lines and web_ids[1] in lines:
                # No se comprueba el orden de aparicion y se asigna el de la
                # web que es más fiable y es casi seguro que las tablas se lean
                # en el orden correcto
                info_partido = {k: v for k, v in zip(web_ids, info_partido.values())}
            else:
                raise ValueError(
                    f"""Los equipos de la web no coinciden con los del acta en la jornada {self}:
                En el pdf: {tuple(info_partido.keys())}
                En la web: {(self.equipo_local_id, self.equipo_visitante_id)}
                """
                )

        for key, (nombre_id, jugadores_goles) in zip(
            ("local", "visitante"), info_partido.items()
        ):
            equipo = self.liga.equipos[nombre_id]
            for jugador, goles in jugadores_goles.items():
                equipo.add_jugador(jugador)
                self.goles_por_jugador[key][str(jugador)] = goles

    def init_equipo(self, col: HTML) -> str:
        nombre = col.find(".equipo", first=True).text.title()
        try:
            logo = col.find("img", first=True).attrs["src"]
            logo_file = (
                f"./files/{self.liga.id_name}/logos/"
                + nombre.lower().replace(" ", "_")
                + ".jpg"
            )
            check_and_download(logo, logo_file)
        except AttributeError:
            logo_file = None
        equipo_obj = Equipo(nombre, self.liga, logo=logo_file)
        if equipo_obj.id_name not in self.liga.equipos:
            self.liga.equipos[equipo_obj.id_name] = equipo_obj
        return equipo_obj.id_name

    @property
    def equipo_local(self) -> "Equipo":
        return self.liga.equipos[self.equipo_local_id]

    @property
    def equipo_visitante(self) -> "Equipo":
        return self.liga.equipos[self.equipo_visitante_id]

    @property
    def resultado(self) -> str:
        if self.goles_local == -1:
            return "Partido no jugado"
        return f"{self.equipo_local} {self.goles_local} - {self.goles_visitante} {self.equipo_visitante}"

    @property
    def info(self) -> PartidoInfo:
        return {
            "fecha": self.fecha,
            "hora": self.hora,
            "lugar": self.lugar,
            "equipo_local_id": self.equipo_local_id,
            "equipo_visitante_id": self.equipo_visitante_id,
            "goles_local": self.goles_local,
            "goles_visitante": self.goles_visitante,
            "acta_path": self.acta_path,
            "goles_por_jugador": self.goles_por_jugador,
        }

    @classmethod
    def from_info(cls, info: PartidoInfo, liga: Liga, jornada: Jornada) -> "Partido":
        partido = cls.__new__(cls)
        partido.fecha = info["fecha"]
        partido.hora = info["hora"]
        partido.lugar = info["lugar"]
        partido.liga = liga
        partido.jornada = jornada
        partido.equipo_local_id = info["equipo_local_id"]
        partido.equipo_visitante_id = info["equipo_visitante_id"]
        partido.goles_local = int(info["goles_local"])
        partido.goles_visitante = int(info["goles_visitante"])
        partido.acta_path = info["acta_path"]
        partido.goles_por_jugador = info["goles_por_jugador"]
        return partido


class Equipo:
    def __init__(
        self,
        nombre: str,
        liga: Liga,
        logo: str = None,
        jugadores: List["Jugador"] = None,
    ):
        self.nombre = nombre
        self.logo = logo
        self.liga = liga
        if jugadores is None:
            self._jugadores = []
        else:
            self._jugadores = jugadores

    def __str__(self) -> str:
        return self.nombre

    def __repr__(self) -> str:
        return self.__str__()

    def add_jugador(self, jugador: "Jugador"):
        if jugador not in self._jugadores:
            self._jugadores.append(jugador)

    @property
    def jugadores(self) -> List["Jugador"]:
        return sorted(self._jugadores, key=lambda x: x.dorsal)

    @property
    def info(self) -> EquipoInfo:
        return {
            "nombre": self.nombre,
            "logo": self.logo,
            "jugadores": [j.info for j in self.jugadores],
        }

    @property
    def id_name(self) -> str:
        return self.nombre.lower().replace(" ", "_")

    @classmethod
    def from_info(cls, info: EquipoInfo, liga: Liga) -> "Equipo":
        equipo = cls.__new__(cls)
        equipo.nombre = info["nombre"]
        equipo.logo = info["logo"]
        equipo.liga = liga
        equipo._jugadores = [Jugador.from_info(j, equipo) for j in info["jugadores"]]
        return equipo


class Jugador:
    def __init__(self, nombre: str, apellidos: str, dorsal: int, equipo: Equipo = None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dorsal = dorsal
        self.equipo = equipo

    def __str__(self) -> str:
        return f"({self.dorsal}) {self.nombre} {self.apellidos}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, another: "Jugador") -> bool:
        return self.nombre == another.nombre and self.dorsal == another.dorsal

    def __hash__(self) -> int:
        return hash(self.__str__())

    @property
    def info(self) -> JugadorInfo:
        return {
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "dorsal": self.dorsal,
        }

    @classmethod
    def from_info(cls, info: JugadorInfo, equipo: Equipo) -> "Jugador":
        jugador = cls.__new__(cls)
        jugador.nombre = info["nombre"]
        jugador.apellidos = info["apellidos"]
        jugador.dorsal = info["dorsal"]
        jugador.equipo = equipo
        return jugador


def check_and_download(url: str, file_path: str):
    if not os.path.exists(file_path):
        with open(file_path, "wb") as f:
            f.write(requests.get(url).content)


async def fetch(session: HTMLSession, url: str) -> HTML:
    r = await session.get(url)
    await r.html.arender(sleep=10, timeout=0)
    return r.html


async def get_ligas_asynchronous(nombres: List[str], urls: List[str]) -> List[Liga]:
    with ThreadPoolExecutor(max_workers=27) as executor:
        session = AsyncHTMLSession()
        loop = asyncio.get_event_loop()
        tasks = [
            await loop.run_in_executor(
                executor,
                fetch,
                *(session, url),  # Allows us to pass in multiple arguments to `fetch`
            )
            for url in urls
        ]
        # Initializes the tasks to run and awaits their results
        ligas = []
        for nombre, response in zip(nombres, await asyncio.gather(*tasks)):
            ligas.append(Liga(nombre, response))
        await session.close()
    return ligas


def _interpretar_nombre_preprocesado(nombre_spl: List[str]) -> Tuple[str, str]:
    # TODO: Trabajar en el parseo de nombres
    for corto in ("De", "Do", "Da", "Del", "De La"):
        if corto in nombre_spl:
            index = nombre_spl.index(corto)
            nombre_spl[index : index + 2] = [" ".join(nombre_spl[index : index + 2])]
            return _interpretar_nombre_preprocesado(nombre_spl)
    if len(nombre_spl) <= 3:
        return nombre_spl[-1], " ".join(nombre_spl[:-1])
    if len(nombre_spl) > 3:
        return " ".join(nombre_spl[-2:]), " ".join(nombre_spl[:-2])


def interpretar_nombre_completo(nombre: str) -> Tuple[str, str]:
    """
    Separa el nombre y los apellidos de una persona teniendo en cuenta que
    puede tener un nombre compuesto y que puede haber o no comas
    """
    nombre = nombre.strip().title()
    if "," in nombre:
        apellidos, nombre = nombre.split(",")
        return nombre, apellidos
    return _interpretar_nombre_preprocesado(nombre.split())


def parse_jugadores_goles(jugadores_col: pd.DataFrame, coli: int) -> Dict[Jugador, int]:
    """
    Extracts the players and the goals from the table
    """
    jugadores = {}
    for numero, jugador, goles in zip(
        jugadores_col[coli - 1].values,
        jugadores_col[coli].values,
        jugadores_col[coli + 1].values,
    ):
        if not isinstance(jugador, str) or pd.isna(numero):
            continue
        numero = int(numero)
        nombre = jugador.replace("*", "").strip()
        if pd.isnull(goles) or goles == "\ue033":
            goles = 0
        else:
            goles = int(goles)
        nombre, apellidos = interpretar_nombre_completo(nombre)
        jugadores[Jugador(nombre, apellidos, numero)] = goles
    return jugadores


def name_column(column: List[Any]) -> bool:
    """
    Devuelve True si la columna es una columna de nombres de jugadores.
    Esto se comprueba viendo que si en la columna hay mas de 5 nombres de un
    total de 16 que sería en teoría el máximo.
    """
    return sum(isinstance(x, str) for x in column if x != "\ue033") / len(column) > (
        5 / 16
    )


def extract_jugadores_goles(
    fname: str,
) -> Tuple[Dict[Jugador, int], Dict[Jugador, int]]:
    tables = tabula.read_pdf(fname, pages="all", pandas_options={"header": None})

    jugadores = tables[1]
    local_equipo = True

    for coli in jugadores.columns:
        if name_column(jugadores[coli]):
            if local_equipo:
                locales = parse_jugadores_goles(jugadores, coli)
                local_equipo = False
            else:
                visitantes = parse_jugadores_goles(jugadores, coli)

    return locales, visitantes


def get_pdf_lines(fname: str) -> List[str]:
    text = (
        textract.process(fname)
        .decode("utf-8")
        .replace("\ue033", "")
        .replace("\xa0", " ")
    )
    return [l for l in text.split("\n") if l.strip()]


def get_pdf_lines_no_number(fname: str) -> List[str]:
    return [l for l in get_pdf_lines(fname) if not l.isnumeric()]


def extract_nombre_equipos(fname: str) -> Tuple[str, str]:
    lines = get_pdf_lines(fname)
    count_num = 0
    for ind, line in enumerate(lines):
        if line.strip().isnumeric():
            count_num += 1
        else:
            if count_num >= 4:
                equipo_local = line
                # get first element of line that is a string
                for l in lines[ind + 1 :]:
                    if not l.isnumeric():
                        equipo_visitante = l
                        return tuple(
                            n.lower().replace(" ", "_")
                            for n in (equipo_local, equipo_visitante)
                        )
                raise IOError("No se encontró el equipo visitante")
            else:
                count_num = 0
    raise IOError("No se encontraron equipos en el acta")


def extract_pdf(fname: str) -> Dict[str, Tuple[Dict[Jugador, int], Dict[Jugador, int]]]:
    """
    Lee el pdf y devuelve un diccionario con los nombres de los equipos como
    claves y un diccionario con los jugadores y los goles que han marcado como
    valores.
    """
    nombre_local, nombre_visitante = extract_nombre_equipos(fname)
    jugadores_goles = extract_jugadores_goles(fname)
    return {nombre_local: jugadores_goles[0], nombre_visitante: jugadores_goles[1]}


if __name__ == "__main__":

    import json
    import argparse
    from multiprocess import Pool

    parser = argparse.ArgumentParser(
        description="Scraper de la web de balonmano gipuzkoa. "
    )
    help = "Archivo con información de las ligas. Si se proporciona no se scrapea la web, solo se cargarían las actas."
    parser.add_argument(
        "-f",
        help=help,
        required=False,
    )
    help = "Archivo donde se escribirá la información de las ligas una vez scrapeada la web y parseados las actas."
    parser.add_argument(
        "-o",
        help=help,
        required=False,
    )
    parser.add_argument(
        "--update-actas",
        help="Actualizar las actas",
        action=argparse.BooleanOptionalAction,
        required=False,
        default=True,
    )
    parser.add_argument(
        "--ncores",
        help="Número de nucleos a usar para parsear las actas",
        required=False,
        type=int,
        default=4,
    )

    args = parser.parse_args()
    info_file = args.f
    out_file = args.o

    SESSION = HTMLSession()

    if info_file is None:
        print("Iniciando extracción de la web...")

        print("Cargando web principal...")
        main_url = (
            "https://www.gieskubaloia.eus/es/competicion/resultados-clasificaciones/"
        )
        req = SESSION.get(main_url)
        req.html.render(sleep=10, timeout=0)
        calendars = req.html.find(".calendar")
        nombres_ligas = [div.find("div")[1].text for div in req.html.find(".competi")]

        if not os.path.exists("./files"):
            os.mkdir("./files")

        print("Cargando ligas...")
        urls = [cal.attrs["href"] for cal in calendars]
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(get_ligas_asynchronous(nombres_ligas, urls))
        loop.run_until_complete(future)

        ligas = future.result()
        ligas_info = [liga.info for liga in ligas]
    else:
        print("Cargando desde archivo")
        with open(info_file, "r") as f:
            ligas_info = json.load(f)

        ligas = [Liga.from_info(info) for info in ligas_info]
    print("Ligas cargadas")

    if args.update_actas:
        print("Actualizando datos de las ligas con actas")

        def update_liga(liga):
            liga.update_actas()
            return liga.info

        with Pool(args.ncores) as p:
            ligas_info_new = p.map(update_liga, ligas)
        print("Actas actualizadas")

    if out_file is not None:
        print("Guardando")
        with open(out_file, "w") as f:
            if args.update_actas:
                json.dump(ligas_info_new, f, indent=2)
            else:
                json.dump([liga.info for liga in ligas], f, indent=2)

    SESSION.close()
    print("Finalizado")
