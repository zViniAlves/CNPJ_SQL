#Importando bibliotecas para manipulação de grandes DF, descompactação de arquivos .zip, interação com browser e manipulação de arquivos no diretorio
import requests as req
import pyodbc
import zipfile
import os
import tkinter as tk
from tkinter import messagebox

try:
    os.remove(os.getcwd() + '\Arquivos CNPJ\aqui ficarão os arquivos que serão baixados.txt')
except:pass

#######################################################################################################################################################################################################################################################################################

#                                                    JANELA PARA LOGIN NO SQL

#######################################################################################################################################################################################################################################################################################

#Função para fechar janela de login
def on_close():
    if messagebox.askokcancel("Fechar", "Você quer fechar a janela?"):
        subwindow.destroy()

#Função que pega o login do SQL
def getLogin():
    
    global subwindow
    global selected_options
    
    #Função para acionar quando Enter apertado
    def on_enter_press(event):
        submit_button.invoke()
    
    #Função que identifica o login 
    def submit_login():
        
        global sql
        global user
        global password
        global database
        
        sql = sql_entry.get()
        user = user_entry.get()
        password = password_entry.get()
        database = data_entry.get()
        
        #Verificando se é conexão local ou por usuario
        if selected_options.get() == 'Conexão Local':
            try:
                conn = pyodbc.connect('Driver={};Server={};''Database={};''Trusted_Connection=yes;'.format('{SQL Server}',sql,database))
                conn.commit()
                subwindow.destroy()
            except:
                messagebox.showerror("Error", "Não foi possível fazer login, verifique as informações")
                return
        else:
            try:
                conn = pyodbc.connect('Driver={};Server={};''Database={};''UID:{};''PWD:{}'.format('{SQL Server}',sql,database,user,password))
                conn.commit()
                subwindow.destroy()
            except:
                messagebox.showerror("Error", "Não foi possível fazer login, verifique as informações")
                return
    
    #Criando window para login
    subwindow = tk.Tk()
    subwindow.iconbitmap(os.getcwd() + '\Icon.ico')
    subwindow.resizable(False,False)
    subwindow.title("Login Microsoft SQL")
    subwindow.geometry("300x110")
    subwindow.config(bg='#376994')
    subwindow.protocol("WM_DELETE_WINDOW", on_close)
    subwindow.bind('<Return>',on_enter_press)
    
    #Commando para desativar os campos quando mudado a opção
    def on_command(typeConnection):
        if typeConnection == 'SQL Server':
            password_label.configure(state=tk.NORMAL,disabledforeground='#376994')
            password_entry.configure(state=tk.NORMAL,disabledforeground='#376994')
            user_label.configure(state=tk.NORMAL,disabledforeground='#376994')
            user_entry.configure(state=tk.NORMAL,disabledforeground='#376994')
        else:
            password_label.configure(state=tk.DISABLED,disabledforeground='#376994')
            password_entry.configure(state=tk.DISABLED,disabledforeground='#376994')
            user_label.configure(state=tk.DISABLED,disabledforeground='#376994')
            user_entry.configure(state=tk.DISABLED,disabledforeground='#376994')
    
    #Criando a Checkbox
    options = ['Conexão Local','SQL Server']
    selected_options = tk.StringVar(subwindow)
    selected_options.set(options[1])
    checkbox = tk.OptionMenu(subwindow,selected_options, *options, command=on_command)
    checkbox.configure(fg='white',bg='#376994',borderwidth=0,highlightthickness=0,font=('Arial 10 bold'),activebackground='#376994',activeforeground='white',justify=tk.CENTER)
    
    #Criando so campos e butões
    sql_label = tk.Label(subwindow, text="Servidor:", bg='#376994', fg='white')
    sql_entry = tk.Entry(subwindow, width=35)
    
    user_label = tk.Label(subwindow, text="Usuario:",bg='#376994', fg='white')
    user_entry = tk.Entry(subwindow, width=35)
    
    password_label = tk.Label(subwindow, text="Senha:",bg='#376994', fg='white')
    password_entry = tk.Entry(subwindow, show="*", width=35)
    
    data_label = tk.Label(subwindow, text="Data Base:",bg='#376994', fg='white')
    data_entry = tk.Entry(subwindow, width=35)
    
    submit_button = tk.Button(subwindow, text="Logar", command=submit_login,bg='#376994', fg='white', width=10)
    
    sql_label.grid(row=0, column=0)
    sql_entry.grid(row=0, column=1, columnspan=2)
    
    data_label.grid(row=1, column=0)
    data_entry.grid(row=1, column=1, columnspan=2)
    
    user_label.grid(row=2, column=0)
    user_entry.grid(row=2, column=1, columnspan=2)
    
    password_label.grid(row=3, column=0)
    password_entry.grid(row=3, column=1, columnspan=2)
    
    checkbox.grid(row=4, column=2)
    
    submit_button.grid(row=4, column=0, columnspan=2)
    
    subwindow.mainloop()

#Função para pegar os dados do servidor
getLogin()

print(34*"=")
print(10*"-" +"LOGIN EFETUADO" + 10*"-")
print(34*"=")

#Conectando com a DataBase no SQL
if selected_options.get() == 'Conexão Local':
    conn = pyodbc.connect('Driver={};Server={};''Database={};''Trusted_Connection=yes;'.format('{SQL Server}',sql,database))
else:
    conn = pyodbc.connect('Driver={};Server={};''Database={};''UID:{};''PWD:{}'.format('{SQL Server}',sql,database,user,password))
cursor = conn.cursor()

#######################################################################################################################################################################################################################################################################################

#                                                    BAIXANDO, REMOVENDO E CONVERTENDOS OS ARQUIVOS DO SITE DA RECEITA

#######################################################################################################################################################################################################################################################################################

#Removendo os arquivos anteriores se existe
zipFiles = os.listdir(os.getcwd() + '\Arquivos CNPJ')
for file in zipFiles:
    os.remove(os.getcwd() +'\Arquivos CNPJ\\'+ file)

print("Baixando arquivos .zip")
print(34*"=")

#Função que baixa os arquivos .zip do site da receita federal
def download_zip(nameFile):
    response = req.get("https://dadosabertos.rfb.gov.br/CNPJ/{}.zip".format(nameFile))
    with open(os.getcwd() + '\Arquivos CNPJ\{}.zip'.format(nameFile),'wb') as f:
        f.write(response.content)

#Baixando os arquivos .zip
listFile = open(os.getcwd() +'\FileNames.txt',encoding='utf-8').read().split('\n')
step = 100/len(listFile)
cStep = 0
for file in listFile:
    download_zip(file)
    cStep += 1
    print(round(step*cStep),"%")
print(34*"=")
print("Descompactando .zips")
print(34*"=")

#Pegando os nomes dos arquivos .zip
zipFiles = os.listdir(os.getcwd() + '\Arquivos CNPJ')

#Descompactando todos os arquivos .rar
for file in zipFiles:
    zipfile.ZipFile(os.getcwd() +'\Arquivos CNPJ\\'+file,'r').extractall(os.getcwd() +'\Arquivos CNPJ')
    os.remove(os.getcwd() +'\Arquivos CNPJ\\'+file)

#Pegandos os nomes dos arquivos descompactados
nameFiles = os.listdir(os.getcwd() + '\Arquivos CNPJ')

#Convertendo os arquivos para .csv
iEmpre = 0
iEstabele = 0
iSocios = 0
for file in nameFiles:
        fileant = os.getcwd() +'\Arquivos CNPJ\\'+file
        if '.EMPRECSV' in file:
            fileatual = os.getcwd() +'\Arquivos CNPJ\\Empresas'+ str(iEmpre) + '.csv'
            iEmpre += 1
            os.rename(fileant, fileatual)
        elif '.ESTABELE' in file:
            fileatual = os.getcwd() +'\Arquivos CNPJ\\Estabelecimentos'+ str(iEstabele) + '.csv'
            iEstabele += 1
            os.rename(fileant, fileatual)
        elif '.SOCIOCSV' in file:
            fileatual = os.getcwd() +'\Arquivos CNPJ\\Socios'+ str(iSocios) + '.csv'
            iSocios += 1
            os.rename(fileant,fileatual)
        elif '.SIMPLES' in file:
            fileatual = os.getcwd() +'\Arquivos CNPJ\\Simples.csv'
            os.rename(fileant,fileatual)
        elif '.MUNICCSV' in file:
            fileatual = os.getcwd() +'\Arquivos CNPJ\\Municipios.csv'
            os.rename(fileant, fileatual)
        elif '.NATJUCSV' in file:
            fileatual = os.getcwd() +'\Arquivos CNPJ\\Natureza.csv'
            os.rename(fileant, fileatual)
        elif '.QUALSCSV' in file:
            fileatual = os.getcwd() +'\Arquivos CNPJ\\Qualificações.csv'
            os.rename(fileant, fileatual)
        elif '.MOTICSV' in file:
            fileatual = os.getcwd() +'\Arquivos CNPJ\\Motivos.csv'
            os.rename(fileant, fileatual)
        elif '.CNAECSV' in file:
            fileatual = os.getcwd() +'\Arquivos CNPJ\\Cnaes.csv'
            os.rename(fileant, fileatual)
        elif '.PAISCSV' in file:
            fileatual = os.getcwd() +'\Arquivos CNPJ\\Pais.csv'
            os.rename(fileant, fileatual)
            
#######################################################################################################################################################################################################################################################################################

#                                                    CRIANDO A TABELA E SUAS RELAÇÕES NO SERVIDOR

#######################################################################################################################################################################################################################################################################################          

#Lendos os comandos para então executalos
textCreateTables = open(os.getcwd() + '\.sqls e .txt\\Criar Tabelas.txt','r').read().replace('{database}',database)
textReworkData = open(os.getcwd() + '\.sqls e .txt\\Arrumar Dados.txt','r').read().replace('{database}',database)
textBulkInsert = open(os.getcwd() + '\.sqls e .txt\\BulkInsert.txt','r').read().replace('{database}',database).replace('{directory}',os.getcwd())
textCreateNewColumns = open(os.getcwd() + '\.sqls e .txt\\Create New Columns.txt','r').read().replace('{database}',database)
textRemoveAuxTables = open(os.getcwd() + '\.sqls e .txt\\RemoveAuxTables.txt','r', encoding='utf-8').read().replace('{database}',database)

#Acessando o database 
cursor.execute("USE {}".format(database))
conn.commit()

#Executando os comandos
print("Criando tabelas e colocando seus respectivos dados")
print(34*"=")
cursor.execute(textCreateTables)
conn.commit()
listBulkInsert = textBulkInsert.split('\n')
for text in listBulkInsert:
    if text != '':
        cursor.execute(text)
        conn.commit()

#Removendo os arquivos .csv após colocalos no SQL para liberar espaço de disco
listRemove = os.listdir(os.getcwd() + '\Arquivos CNPJ')
for file in listRemove:
    os.remove(os.getcwd() +'\Arquivos CNPJ\\'+file)

print("Fazendo a adptação dos dados das tabelas OBS!!!: Processo demora muito")
print(34*"=")
cursor.execute(textCreateNewColumns)
conn.commit()
listReworkData = textReworkData.split(';')
for text in listReworkData:
    if text != '':
        cursor.execute(text)
        conn.commit()
cursor.execute(textRemoveAuxTables)
conn.commit()

print("Concluido!!!")
print(34*"=")

#Closing the connection
cursor.close()
conn.close()

print("Fechando Conexão")
print(34*"=")