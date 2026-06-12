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
class evetos(tk.Tk):
    ev-1= tk.Label(text="É seu primeiro dia, você está muito animado(a) que finalmente chegou sua primeira visão é um grupo de alunos.Oque você faz")
    opcoes = [
        "Sair correndo",
        "Ignorar e só entra",
        "Tenta puxar assunto aleatorio",
        "Tentar chamar atenção desfilando"
    ]

    for opcao in opcoes:
        botao = tk.Button( text=opcao, width=25, height=2,
                          command=lambda o=opcao: resposta(o))
        botao.pack(pady=5)





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
        self.tela.grid(row=2,column=1)

        self.but1=tk.Button(text='iniciar jogo')
        self.but1.grid(row=2,column=2)


pri= Tela_Principal()
pri.geometry("700x500")
pri.mainloop