import tkinter as tk
import random as rr
from tkinter import messagebox
'''aqui colocar a parte personagem'''
class Pessoa():
    def __init__(self,nome):
        self.nome=nome
        self.periodo=0
    def avdperiodo(self):
        self.periodo += 1
class Dsexo(Pessoa):
   listas = ['masculino','feminino']
   sexo = rr.choice(listas)
class Riqueza(Pessoa):
    li = ['Rico','Medio','Pobre']
    csocial = rr.choice(li)
class Edu(Pessoa):
    pass  
class Curso(Pessoa):
    pass 
class saude(Pessoa):
    pass
''''Aqui colocar os eventos'''
class DepositoEventos():
    def __init__(self):
        self.eventos = {
        "Periodo1": [
            {
                "texto":"É seu primeiro dia de aula. Um grupo de alunos conversa perto da entrada."
                "opçao":[
                    "Apresentar-se ao grupo",
                    "Entrar sozinho",
                    "Fazer uma piada",
                    "Esperar alguém falar com você"
                ]
            },
            {
                "texto": "Durante o intervalo, alguns colegas convidam você para sentar com eles.",
                "opçao":[ 
                    "Aceitar o convite",
                    "Recusar educadamente",
                    "Sentar e ficar em silêncio",
                    "Tentar liderar a conversa"]
            }
        ],
        "Periodo2": [...],
        "Periodo3": [...],
        "Periodo4": [...],
        "Periodo5": [...],
        "Periodo6": [...],
        "Periodo7": [...],
        "Periodo8": [...]
}

  



'''Colocar os recursos de escolha de evento'''
class GerenciarEventos(DepositoEventos):
   def __init__(self):
        super().__init__()
        self.evento = rr.choice(self.eventos["Periodo1"])

    def mostrar_evento(evento):

        self.label_texto.config(text=evento["texto"])

        for i in range(4):
            botoes[i].config(
                text=evento["opcoes"][i]
            )
       
















'''Aqui colocar a interface grafica'''
class Menu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Menu").pack(pady=20)

        tk.Button(
            self,
            text="Iniciar",
            command=lambda: master.mostrar_tela("Ev")
        ).pack()

class Ev(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Tela 2").pack(pady=20)

        tk.Button(
            self,
            text="Voltar",
            command=lambda: master.mostrar_tela("Menu")
        ).pack()

class Jogo(tk.Tk):
    def __init__(self):
        super().__init__()

        self.telas = {
            "tela1": Menu(self),
            "tela2": Ev(self)
        }

        self.mostrar_tela("tela1")

    def mostrar_tela(self, nome):

        for tela in self.telas.values():
            tela.pack_forget()

        self.telas[nome].pack(fill="both", expand=True)

app = Jogo()
app.mainloop()