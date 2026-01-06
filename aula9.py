# janela para selecionar arquivos do nosso computador

# fazer backup dos arquivos importantes que estao nesta pasta

import os
from tkinter.filedialog import askdirectory # abre uma janela para selecionar a pasta desejada
import shutil  # copiar arquivos de uma pasta para outra
import datetime 

nome_pasta_selecionada = askdirectory()  # abre a janela para selecionar a pasta\
print(nome_pasta_selecionada)

lista_arquivos = os.listdir(nome_pasta_selecionada) # lista todos os arquivos da pasta selecionada
print(lista_arquivos) 

# fazer backup dos arquivos importantes que estao nesta pasta
nome_pasta_backup = "backup"

nome_completo_pasta_backup = f"{nome_pasta_selecionada}/{nome_pasta_backup}"
if not os.path.exists(nome_completo_pasta_backup):
      os.mkdir(nome_completo_pasta_backup)  # cria a pasta de backup

data_atual = datetime.date.today().strftime("%Y-%m-%d %H%M%S")
print(data_atual)


for arquivo in lista_arquivos:
    print(arquivo) 
    nome_completo_arquivo = f"{nome_pasta_selecionada}/{arquivo}"
    nome_final_arquivo = f"{nome_completo_pasta_backup}/{data_atual}/{arquivo}"
    
    if not os.path.exists(f"{nome_completo_pasta_backup}/{data_atual}"): 
        os.mkdir(f"{nome_completo_pasta_backup}/{data_atual}")
    
    if "." in arquivo:
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo)  # copia o arquivo para a pasta de backup
    elif "backup" != arquivo:
         shutil.copytree(nome_completo_arquivo, nome_final_arquivo)