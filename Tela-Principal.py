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
class GerenciadorEventos(tk.TK):
    def __init__(self):
        super().__init__():
        self.eventos = {
            "pool1": [
                {
                    "texto": "É seu primeiro dia de aula.",
                    "opcoes": [
                        "Sair correndo",
                        "Entrar normalmente",
                        "Puxar conversa",
                        "Desfilar"
                    ]
                }
            ],

            "pool2": [
                {
                    "texto": "O professor anuncia uma prova surpresa.",
                    "opcoes": [
                        "Estudar",
                        "Colar",
                        "Fingir doença",
                        "Aceitar o destino"
                    ]
                }
            ]
        }

    def obter_evento(self, pool):
        return rr.choice(self.eventos[pool])
    for opcao in opcoes:
        botao = tk.Button(
            self,
            text=opcao,
            width=30,
            command=lambda o=opcao: self.resposta(o)
        )
        botao.pack(pady=5)
    def mostrar_evento(id_evento):
        evento = eventos[id_evento]
        pergunta.config(text=evento["texto"])

        for i, botao in enumerate(botao):
            botao.config(text=evento["opcoes"][i])



'''Colocar os recursos de escolha de evento'''
class Escolha1(Pessoa):
    opcao=[]
    messagebox.showinfo('Escolha',f'Você escolheu:{opcao}')
    def criar_interface():
        janela = tk.Tk()
        janela.title("Ano 0")
















'''Aqui colocar a interface grafica'''
class Tela_Principal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.tela= tk.Label(text='Menu')
        self.tela.pack(anchor="w")

        self.but1=tk.Button(text='iniciar jogo')
        self.but1.pack(anchor="w")


pri= Tela_Principal()
pri.geometry("700x500")
pri.mainloop