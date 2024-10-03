from tkinter import *
from tkinter import ttk

# Descrição formal do AFD
I = [0.25, 0.50, 1.00]
O = ['r', 'n', 't']
S_ = [0, 1, 2, 3, 4, 5, 6, 7, 8]
s0 = 0
F = [8]
delta = [[1, 2, 4], [2, 3, 5], [3, 4, 6], [4, 5, 7], [5, 6, 8], [6, 7, 8], [7, 8, 8], [8, 8, 8], [8, 8, 8]] # Tabela de estado próximo estado
delta2 = [['n', 'n', 'n'], ['n', 'n', 'n'], ['n', 'n', 'n'], ['n', 'n', 'n'], ['n', 'n', 'n'], ['n', 'n', 't'], ['n', 'n', 't'], ['n', 't', 't'], ['t', 't', 't']] # Saída

# função de transição
def f(estd, entrada):
    return delta[estd][I.index(entrada)]

# função de saída
def g(estd, cad):
    if len(cad) <= 0:
        return 'n'
    if sum(cad) == 2:
        return 'r'
    return delta2[estd][I.index(cad[-1])]

def botao():
    saldo = 0
    estado = s0
    fim_cadeia = False
    i = 0
    try:
        while not fim_cadeia:
            if i == len(cadeia):
                fim_cadeia = True
                sld.set(0.0)
            else:
                estado = f(estado, cadeia[i])
                saldo += cadeia[i]

            i+=1

        if g(estado, cadeia) == O[2]:
            resposta.set(f"Aqui está seu refrigerante!\nTroco: R$ {saldo-2:.2f}")
            cadeia.clear()

        elif g(estado, cadeia) == O[0]:
            resposta.set(f"Aqui está seu refrigerante!")
            cadeia.clear()

        else:
            resposta.set(f"Saldo insuficiente")
            cadeia.clear()

    except ValueError:
        resposta.set(f"A cadeia foi rejeitada")
        cadeia.clear()
 
    except Exception as e:
        resposta.set("Erro executando o autômato: ", e)
        cadeia.clear()


cadeia = []

# Moeda de 25 centavos
def add025():
    cadeia.append(0.25)
    sld.set(sum(cadeia))

# Moeda de 50 centavos
def add050():
    cadeia.append(0.50)
    sld.set(sum(cadeia))

# Moeda de 1 real
def add100():
    cadeia.append(1.00)
    sld.set(sum(cadeia))

# Criação da GUI
root = Tk()
root.title("Máquina de vendas")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Rótulos
# Indicador do saldo acumulado
sld = StringVar()
sld.set(0.0)
ttk.Label(mainframe, textvariable=sld).grid(column=3, row=2, sticky=(W, E))

# Indicador da resposta
resposta = StringVar()
ttk.Label(mainframe, textvariable=resposta).grid(column=2, row=5, sticky=(W, E))

ttk.Label(mainframe, text="Saldo").grid(column=4, row=2, sticky=W)
ttk.Label(mainframe, text="Resposta:").grid(column=1, row=5, sticky=W)

# Botões com valores das moedas
ttk.Button(mainframe, text="0.25", command=add025).grid(column=1, row=1, sticky=N)
ttk.Button(mainframe, text="0.50", command=add050).grid(column=2, row=1, sticky=N)
ttk.Button(mainframe, text="1.00", command=add100).grid(column=3, row=1, sticky=N)

# Botão de dispensar o refrigerante
ttk.Button(mainframe, text="Dispensar", command=botao).grid(column=4, row=1, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
root.bind("<Return>", botao)
root.mainloop()