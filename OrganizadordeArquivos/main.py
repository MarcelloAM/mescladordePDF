import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione uma pasta') # Selecionando qual pasta irá ser usada

lista_arquivos = os.listdir(caminho) # Usando uma lista para observar os arquivos dentro do caminho
print(lista_arquivos) # Verificando os arquivos

locais = {
    'imagens': ['.png', '.jpg', '.jpeg'], # Nome da pasta, extensões de arquivos que terá na página
    'textos': ['.txt'],
    'documentos': ['.docx'],
    'planilhas': ['.xlsx'],
    'pdfs': ['.pdf'],
    'musicas': ['.mp4'],
    'executaveis': ['.exe'],
    'zipadas': ['.rar', '.7z', '.zip']
} # Locais que serão jogados os arquivos

for arquivo in lista_arquivos: # Percorrendo a lista de arquivos
    # A Variavel arquivo é o nome do arquivo com extensão
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}') # Extraindo do arquivo a extensão do arquivo usando o splittext
    for pasta in locais:
        if extensao in locais[pasta]: # Vericica se se a extensão está dentro das lisas criadas acima
            if not os.path.exists(f'{caminho}/{pasta}'): # Caso não existir a pasta, irá ser criado a pasta.
                os.makedirs(f'{caminho}/{pasta}') 
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}') # Pegando o arquivo e colocando na pasta nova que foi criada.