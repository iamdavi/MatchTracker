import PyPDF2
import os


class Archivo:
	nombre = ''
	tipo = ''
	tamano = ''
	ruta = ''

	def __init__(self, ruta: str):
		self.ruta = ruta

	def parsear_pdf(self):
		base_path = os.path.dirname(os.path.realpath(__file__))
		pdf_path = base_path + self.ruta
		pdf_file = open(pdf_path, 'rb')
		pdf_reader = PyPDF2.PdfFileReader(pdf_file)
		page = pdf_reader.getPage(0)
		texto = page.extractText()
		return texto


archivo = Archivo('/media/acta_balonmano.pdf')
texto = archivo.parsear_pdf()
print(texto)