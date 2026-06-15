import tkinter as tk
import random as rr
from tkinter import messagebox
'''aqui colocar a parte personagem'''
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.periodo = 1
        self.sexo = rr.choice(['masculino', 'feminino'])
        self.classe_social = rr.choice(['Rico', 'Medio', 'Pobre'])

    def avancar_periodo(self):
        self.periodo += 1

''''Aqui colocar os eventos'''
class DepositoEventos:
    def __init__(self):
        self.eventos = {
            "Periodo1": [
                {
                    "texto": "É seu primeiro dia de aula. Um grupo de alunos conversa perto da entrada.",
                    "opcoes": [          # ← chave consistente
                        "Apresentar-se ao grupo",
                        "Entrar sozinho",
                        "Fazer uma piada",
                        "Esperar alguém falar com você"
                    ]
                },
                {
                    "texto": "Durante o intervalo, alguns colegas convidam você para sentar com eles.",
                    "opcoes": [
                        "Aceitar o convite",
                        "Recusar educadamente",
                        "Sentar e ficar em silêncio",
                        "Tentar liderar a conversa"
                    ]
                }
            ],
            "Periodo2": [...],
            "Periodo3": [...],
        }

'''Gerenciador de Eventos'''
class GerenciarEventos(DepositoEventos):
    def __init__(self):
        super().__init__()

    def sortear_evento(self, periodo: int):
        chave = f"Periodo{periodo}"
        lista = self.eventos.get(chave, [])
        if not lista:
            return None
        return rr.choice(lista)

'''Aqui colocar a interface grafica'''
class Menu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="🎓 Jogo da Faculdade", font=("Arial", 18, "bold")).pack(pady=30)
        tk.Button(
            self, text="Iniciar",
            command=lambda: master.mostrar_tela("jogo")
        ).pack()


class TelaJogo(tk.Frame):
    def __init__(self, master, gerenciador: GerenciarEventos, personagem: Pessoa):
        super().__init__(master)
        self.gerenciador = gerenciador
        self.personagem = personagem

        self.label_periodo = tk.Label(self, font=("Arial", 10))
        self.label_periodo.pack(pady=(10, 0))

        self.label_texto = tk.Label(
            self, wraplength=400, justify="center", font=("Arial", 12)
        )
        self.label_texto.pack(pady=20, padx=20)

        self.botoes = []
        for i in range(4):
            btn = tk.Button(
                self, width=40,
                command=lambda idx=i: self.escolher(idx)
            )
            btn.pack(pady=4)
            self.botoes.append(btn)

        tk.Button(
            self, text="Voltar ao Menu",
            command=lambda: master.mostrar_tela("menu")
        ).pack(pady=10)

        self.carregar_evento()

    def carregar_evento(self):
        self.evento_atual = self.gerenciador.sortear_evento(self.personagem.periodo)

        self.label_periodo.config(
            text=f"Período {self.personagem.periodo} — {self.personagem.nome} ({self.personagem.sexo})"
        )

        if self.evento_atual is None:
            self.label_texto.config(text="Sem eventos para este período.")
            for btn in self.botoes:
                btn.config(text="—", state="disabled")
            return

        self.label_texto.config(text=self.evento_atual["texto"])
        for i, btn in enumerate(self.botoes):
            btn.config(text=self.evento_atual["opcoes"][i], state="normal")

    def escolher(self, indice):
        opcao = self.evento_atual["opcoes"][indice]
        messagebox.showinfo("Escolha", f"Você escolheu:\n«{opcao}»")
        self.personagem.avancar_periodo()
        self.carregar_evento()
        
''' parte principal do Jogo'''
class Jogo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo da Faculdade")
        self.geometry("500x400")

        personagem = Pessoa("Jogador")
        gerenciador = GerenciarEventos()

        self.telas = {
            "menu": Menu(self),
            "jogo": TelaJogo(self, gerenciador, personagem),
        }

        self.mostrar_tela("menu")

    def mostrar_tela(self, nome):
        for tela in self.telas.values():
            tela.pack_forget()
        self.telas[nome].pack(fill="both", expand=True)


app = Jogo()
app.mainloop()