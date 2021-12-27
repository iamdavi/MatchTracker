from collections import defaultdict
from glob import glob
import tabula
import textract
import pandas as pd
from tqdm import tqdm
import json


def extract_jugadores_goles(jugadores, coli):
    """
    Extracts the players and the goals from the table
    """
    locales = []
    for jugador, goles in zip(jugadores[coli].values, jugadores[coli+1].values):
        if not isinstance(jugador, str):
            continue
        nombre = jugador.replace('*', '').strip()
        goles = goles if not pd.isnull(goles) else 0
        locales.append((nombre, goles))
    return locales


def name_column(column):
    """
    Returns True if most of the elements of the columns are strings
    """
    return sum(isinstance(x, str) for x in column)/len(column) > 0.5


## Actas hasta: 24/11/2021
fnames = glob('./actas/*')

equipos = defaultdict(set)

for fname in tqdm(fnames):
    # Extraer jugadores y goles
    tables = tabula.read_pdf(fname, pages='all', pandas_options={'header': None})

    jugadores = tables[1]
    local_equipo = True

    for coli in jugadores.columns:
        if name_column(jugadores[coli]):
            if local_equipo:
                locales = extract_jugadores_goles(jugadores, coli)
                local_equipo = False
            else:
                visitantes = extract_jugadores_goles(jugadores, coli)

    text = textract.process(fname).decode('utf-8')
    index = text.index('\ue033')
    lines = [l for l in text[:index].split('\n') if l]

    count_num = 0

    for ind, line in enumerate(lines):
        if line.isnumeric():
            count_num += 1
        else:
            if count_num >= 4:
                equipo_local = line
                # get first element of line that is a string
                for l in lines[ind+1:]:
                    if not l.isnumeric():
                        equipo_visitante = l
                        break
                break
            else:
                count_num = 0

    equipos[equipo_local].update(list(zip(*locales))[0])
    equipos[equipo_visitante].update(list(zip(*visitantes))[0])

equipos = {k: list(v) for k, v in equipos.items()}

with open('equipos.json', 'w') as fwr:
    json.dump(equipos, fwr, indent=2)
