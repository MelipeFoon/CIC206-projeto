from tkinter import *
from tkinter import ttk

I = ['0.25', '0.50', '1.00']
# I = ['b', '0.25', '0.50', '1.00']
S_ = [0, 1, 2, 3, 4, 5, 6, 7, 8]
s0 = 0
F = [8]
delta = [[1, 2, 4], [2, 3, 5], [3, 4, 6], [4, 5, 7], [5, 6, 8], [6, 7, 8], [7, 8, 8], [8, 8, 8], [8, 8, 8]]
# delta = [[0, 1, 2, 4], [1, 2, 3, 5], [2, 3, 4, 6], [3, 4, 5, 7], [4, 5, 6, 8], [5, 6, 7, 8], [6, 7, 8, 8], [7, 8, 8, 8], [0, 8, 8, 8]]

def f(estado, entrada):
    return delta[estado][I.index(entrada)]

def g(estado):
    if estado in F:
        return True
    else:
        return False

def botao(*args):
    cadeia = entr.get().strip().split(" ")
    saldo = 0
    estado = s0
    fim_cadeia = False
    i = 0
    try:
        while not fim_cadeia:
            if i == len(cadeia):
                fim_cadeia = True
            else:
                estado = f(estado, cadeia[i])
                saldo += float(cadeia[i])
                # print(estado)
            i+=1
        if g(estado) and saldo > 2:
            resposta.set(f"Aqui está seu refrigerante!\nTroco: R$ {saldo-2:.2f}")
            # print(f"Aqui está seu refrigerante!\nTroco: R$ {saldo-2:.2f}")

        elif saldo == 2:
            resposta.set(f"Aqui está seu refrigerante!")
            # print(f"Aqui está seu refrigerante!")

        else:
            resposta.set(f"Saldo insuficiente")
            # print(f"Saldo insuficiente")
    except ValueError:
        resposta.set(f"A cadeia foi rejeitada")
        # print(f"A cadeia foi rejeitada")
    except Exception as e:
        resposta.set("Erro executando o autômato: ", e)
        # print("Erro executando o autômato: ", e)


root = Tk()
root.title("Máquina de vendas")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

entr = StringVar()
entrada_cadeia = ttk.Entry(mainframe, width=7, textvariable=entr)
entrada_cadeia.grid(column=2, row=1, sticky=(W, E))

resposta = StringVar()
ttk.Label(mainframe, textvariable=resposta).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Dispensar", command=botao).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="saldo").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="resposta").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

entrada_cadeia.focus()
root.bind("<Return>", botao)

root.mainloop()

# testes
# if __name__ == '__main__':
#     botao(['1.00', '1.00']) # aceita
#     botao(['0.25', '1.00']) #  rejeita
#     botao(['1.00', '1.00', '1.00', '0.50'])