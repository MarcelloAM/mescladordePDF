import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_de_arquivos = os.listdir('mescladordepdf/arquivos')
lista_de_arquivos.sort()

print(lista_de_arquivos)

for arquivo in lista_de_arquivos:
    if '.pdf' in arquivo:
        merger.append(f'mescladordepdf/arquivos/{arquivo}')

merger.write('PDF Final.pdf')
