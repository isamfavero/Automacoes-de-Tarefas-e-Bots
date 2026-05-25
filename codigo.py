
import pyautogui 
import time 
pyautogui.PAUSE = 0.5 

# 1: entrar no sistema (aplicativo)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")    
time.sleep(0.5) 

#1.1 abrir site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)
# 2: fazer login
pyautogui.press("tab")
pyautogui.write("umbomendereco@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(0.5)

#3: abrir a base de dados (importar o arquivo)
    # pip install pandas openpyxl
import pandas 
table = pandas.read_csv("produtos.csv")
print(table) # mostra os dados do arquivo anexado no terminal 

#4: cadastrar 1 produto

for line in table.index: 
    pyautogui.click(x=690, y=246)
        #código
    codigo = str(table.loc [line,"codigo" ])
    pyautogui.write(codigo)
    pyautogui.press("tab")

        # marca 
    marca = str (table.loc[line,"marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

        # tipo
    tipo = str(table.loc[line,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

        # categoria
    categoria = str(table.loc[line,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

        # precoUnitario
    precoUnitario = str(table.loc[line,"preco_unitario"])
    pyautogui.write(precoUnitario) 
    pyautogui.press("tab") 

        # custo
    custo = str(table.loc[line,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

        # obs
    obs =  str(table.loc[line,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")




