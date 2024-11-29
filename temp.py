from pdfminer.high_level import extract_text
import re

texto = extract_text('pdf.pdf', password='10366')

resultado = r'-Compras diversas(.*)'

inserir = re.search(resultado, texto)
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write(inserir.group(1))