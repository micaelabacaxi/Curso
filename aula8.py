import datetime
import os 


print(os.listdir("arquivos"))

print(datetime.date.today())

#pandas trabalhar com o excel como base de dados

#openpyxl    editar arquivos excel

#pyautogui  automatizar tarefas do mouse e teclado

lista_arquivos = os.listdir("arquivos")

for arquivo in lista_arquivos:
    if ".txt" in arquivo: 
        if "22" in arquivo: 
            os.rename(f"arquivos/{arquivo}", f"arquivos/22/{arquivo}")
        elif "23" in arquivo: 
            os.rename(f"arquivos/{arquivo}", f"arquivos/23/{arquivo}")