class Automato:
    I: list
    S: list
    s0: int
    F: list
    delta: list
    
    def __init__(self):
        self.I = ['0.25', '0.50', '1.00']
        self.S = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.s0 = 0
        self.F = [8]
        self.delta = [[1, 2, 4], [2, 3, 5], [3, 4, 6], [4, 5, 7], [5, 6, 8], [6, 7, 8], [7, 8, 8], [8, 8, 8], [8, 8, 8]]
    
    def f(self, estado, entrada):
        return self.delta[estado][self.I.index(entrada)]
    
    def g(self, estado):
        if estado in self.F:
            return True
        else:
            return False
        
    def botao(self, cadeia:list):
        saldo = 0
        estado = self.s0
        fim_cadeia = False
        i = 0
        try:
            while not fim_cadeia:
                if i == len(cadeia):
                    fim_cadeia = True
                else:
                    estado = self.f(estado, cadeia[i])
                    saldo += float(cadeia[i])
                    # print(estado)
                i+=1
            if self.g(estado) and saldo > 2:
                return f"Aqui está seu refrigerante!\n Troco: R$ {saldo-2:.2f}"
            
            elif saldo == 2:
                return f"Aqui está seu refrigerante!"

            else:
                return f"Saldo insuficiente"
        except ValueError:
            return f"A cadeia foi rejeitada"
        except Exception as e:
            return f"Erro executando o autômato: {e}"