import tkinter as tk
import random as rr
from tkinter import messagebox

# ─────────────────────────────────────────────
# PERSONAGEM
# ─────────────────────────────────────────────
class Pessoa:
    def __init__(self, nome, sexo, classe_social):
        self.nome          = nome
        self.sexo          = sexo
        self.classe_social = classe_social  
        self.periodo       = 1
       
        self.saude    = rr.randint(1, 10)
        self.educacao = rr.randint(1, 10)   
        self.carisma  = rr.randint(1, 10)
        self.stresse  = 0                   

    def avancar_periodo(self):
        self.periodo += 1

    def aplicar_efeitos(self, efeitos: dict):
        for attr, valor in efeitos.items():
            atual = getattr(self, attr, None)
            if atual is not None:
                setattr(self, attr, max(0, atual + valor))

    def resumo(self) -> str:
        return (
            f"Sau: {self.saude}  |  "
            f"Edu: {self.educacao}  |  "
            f"Car: {self.carisma}  |  "
            f"Stress: {self.stresse}"
        )


# ─────────────────────────────────────────────
# DEPÓSITO DE EVENTOS
# ─────────────────────────────────────────────
class DepositoEventos:
    def __init__(self):
        self.eventos = {
            "Periodo1": [
                {
                    "texto": (
                        "É seu primeiro dia de aula. Um grupo de alunos "
                        "conversa perto da entrada."
                    ),
                    "opcoes": [
                        {"texto": "Apresentar-se ao grupo",
                         "efeitos": {"carisma": +2, "stresse": -1}},
                        {"texto": "Ignorar e entrar sozinho",
                         "efeitos": {"carisma": -1, "stresse": +1}},
                        {"texto": "Fazer uma piada",
                         "efeitos": {"carisma": +1, "stresse": -1}},   
                        {"texto": "Esperar alguém falar com você",
                         "efeitos": {"stresse": +2}},
                    ]
                },
                {
                    "texto": (
                        "Durante o intervalo, alguns calouros te convidam para "
                        "sentar com eles."
                    ),
                    "opcoes": [
                        {"texto": "Aceitar o convite",
                         "efeitos": {"carisma": +2, "stresse": -1}},
                        {"texto": "Recusar educadamente",
                         "efeitos": {"carisma": -1, "educacao": +1}},
                        {"texto": "Sentar e ficar em silêncio",
                         "efeitos": {"carisma": -2}},
                        {"texto": "Tentar liderar a conversa",
                         "efeitos": {"carisma": +3, "stresse": +2}},
                    ]
                },
                {
        "texto": (
            "Você encontra um veterano nos corredores."
        ),
        "opcoes": [
            {
                "texto": "Pedir dicas sobre a faculdade",
                "efeitos": {"carisma": +1, "inteligencia": +1}
            },
            {
                "texto": "Conversar sobre o curso",
                "efeitos": {"carisma": +2}
            },
            {
                "texto": "Apenas cumprimentar",
                "efeitos": {"carisma": +1}
            },
            {
                "texto": "Ignorar e seguir andando",
                "efeitos": {"carisma": -1}
            },
        ]
    },
            ],
            "Periodo2": [
                {
                    "texto": "Você puxou uma matéria com um professor horrível.",
                    "opcoes": [
                        {"texto": "Estudar como nunca",
                         "efeitos": {"educacao": +5, "stresse": +4}},
                        {"texto": "Viu a primeira aula e decidiu trancar",
                         "efeitos": {"educacao": -3, "stresse": -5}},
                        {"texto": "Fazer um grupo de estudos",
                         "efeitos": {"carisma": +3, "educacao": +3}},
                        {"texto": "Pagar alguém para fazer as provas por você",
                         "efeitos": {"stresse": -7}},
                    ]
                },
                {
                    "texto": "Um trabalho em grupo é dado por um professor.",
                    "opcoes": [
                        {"texto": "Escolher bem as pessoas para pegar os melhores",
                         "efeitos": {"educacao": +2, "stresse": -1}},
                        {"texto": "Entrar no grupo que sobrar",
                         "efeitos": {"carisma": -1, "stresse": +1}},
                        {"texto": "Ir no grupinho de sempre",
                         "efeitos": {"carisma": +1, "stresse": -1}},
                        {"texto": "Perguntar se pode fazer sozinho",
                         "efeitos": {"stresse": -2, "carisma": -2}},
                    ]
                },
                 {
        "texto": (
            "Há uma festa universitária acontecendo hoje à noite."
        ),
        "opcoes": [
            {
                "texto": "Ir à festa e conhecer pessoas",
                "efeitos": {"carisma": +2, "esaude": -3}
            },
            {
                "texto": "Ir apenas por algumas horas",
                "efeitos": {"carisma": +1}
            },
            {
                "texto": "Ficar em casa estudando",
                "efeitos": {"inteligencia": +2, "stresse": +1}
            },
            {
                "texto": "Ignorar o convite",
                "efeitos": {"carisma": -1}
            },
        ]
    },
            ],
            "Periodo3": [
                {
                    "texto": (
                        "Um professor oferece uma pesquisa remunerada. "
                        "Mas vai tomar muito tempo."
                    ),
                    "opcoes": [
                        {"texto": "Aceitar mesmo tendo que atrasar matérias",
                         "efeitos": {"educacao": +3, "stresse": +2}},
                        {"texto": "Aceitar mas negociar tempo para não atrasar",
                         "efeitos": {"educacao": +1, "stresse": +4, "carisma": +1}},
                        {"texto": "Recusar educadamente",
                         "efeitos": {"stresse": -2, "educacao": -2}},
                        {"texto": "Ignorar o e-mail",
                         "efeitos": {"carisma": -2, "stresse": -1}},
                    ]
                },
                 {
        "texto": (
            "Seu grupo ainda não começou o trabalho e o prazo está perto."
        ),
        "opcoes": [
            {
                "texto": "Assumir a liderança",
                "efeitos": {"carisma": +2, "stresse": +1}
            },
            {
                "texto": "Organizar uma reunião",
                "efeitos": {"carisma": +1}
            },
            {
                "texto": "Fazer apenas sua parte",
                "efeitos": {"inteligencia": +1}
            },
            {
                "texto": "Deixar para a última hora",
                "efeitos": {"stresse": +2}
            },
        ]
    },
            ],
            "Periodo4": [
            {
        "texto": (
            "O professor pede que os alunos formem duplas para um trabalho."
        ),
        "opcoes": [
            {
                "texto": "Convidar alguém para fazer dupla",
                "efeitos": {"carisma": +2, "stresse": -1}
            },
            {
                "texto": "Esperar alguém te chamar",
                "efeitos": {"carisma": -1, "stresse": +1}
            },
            {
                "texto": "Fazer o trabalho sozinho",
                "efeitos": {"inteligencia": +1, "stresse": +2}
            },
            {
                "texto": "Pedir ajuda ao professor",
                "efeitos": {"carisma": +1}
            },
        ]
    },
    {
        "texto": (
            "A cantina está lotada durante o intervalo."
        ),
        "opcoes": [
            {
                "texto": "Entrar na fila normalmente",
                "efeitos": {"paciencia": +1}
            },
            {
                "texto": "Conversar com colegas enquanto espera",
                "efeitos": {"carisma": +1, "stresse": -1}
            },
            {
                "texto": "Comprar algo rápido na máquina",
                "efeitos": {"dinheiro": -1}
            },
            {
                "texto": "Pular o lanche",
                "efeitos": {"energia": -2}
            },
        ]
    },
            ],
            "Periodo5": [
                {
        "texto": (
            "Você percebe que esqueceu um material importante para a aula."
        ),
        "opcoes": [
            {
                "texto": "Pedir emprestado para um colega",
                "efeitos": {"carisma": +1, "stresse": -1}
            },
            {
                "texto": "Improvisar com o que tem",
                "efeitos": {"inteligencia": +1}
            },
            {
                "texto": "Sair para comprar outro",
                "efeitos": {"dinheiro": -2, "stresse": -1}
            },
            {
                "texto": "Ficar sem o material",
                "efeitos": {"stresse": +2}
            },
        ]
    },
            ],
            "Periodo6": [
                 {
        "texto": (
            "Uma prova surpresa é anunciada pelo professor."
        ),
        "opcoes": [
            {
                "texto": "Fazer a prova com confiança",
                "efeitos": {"inteligencia": +2}
            },
            {
                "texto": "Pedir alguns minutos para revisar",
                "efeitos": {"stresse": -1}
            },
            {
                "texto": "Tentar colar",
                "efeitos": {"inteligencia": -1, "stresse": +2}
            },
            {
                "texto": "Desistir da prova",
                "efeitos": {"stresse": +1}
            },
        ]
    },
            ],
            "Periodo7": [
                 {
        "texto": (
            "O professor faz uma pergunta difícil para a turma."
        ),
        "opcoes": [
            {
                "texto": "Levantar a mão e responder",
                "efeitos": {"carisma": +1, "inteligencia": +2}
            },
            {
                "texto": "Responder mesmo sem certeza",
                "efeitos": {"carisma": +2}
            },
            {
                "texto": "Esperar outro aluno responder",
                "efeitos": {}
            },
            {
                "texto": "Evitar contato visual",
                "efeitos": {"carisma": -1}
            },
        ]
    }
            ],
            "Periodo8": [],
        }


# ─────────────────────────────────────────────
# GERENCIADOR DE EVENTOS
# ─────────────────────────────────────────────
class GerenciarEventos(DepositoEventos):
    def __init__(self):
        super().__init__()

    def sortear_evento(self, periodo: int):
        chave = f"Periodo{periodo}"
        lista = self.eventos.get(chave, [])
        if not lista:
            return None
        return rr.choice(lista)


# ─────────────────────────────────────────────
# TELA 1 — MENU PRINCIPAL
# ─────────────────────────────────────────────
class Menu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(
            self, text="🎓 Jogo da Faculdade",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        tk.Button(
            self, text="Iniciar",
            command=lambda: master.mostrar_tela("criacao")
        ).pack(pady=8)

        tk.Button(
            self, text="Sair",
            width=20, font=("Arial", 12),
            command=master.destroy
        ).pack(pady=4)


# ─────────────────────────────────────────────
# TELA 2 — CRIAÇÃO DE PERSONAGEM
# ─────────────────────────────────────────────
class TelaCriacao(tk.Frame):   # BUG 7: nome era "Telacriacoa" (typo)
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(
            self, text="Crie seu Personagem", font=("Arial", 20, "bold")
        ).pack(pady=20)

        # Nome
        tk.Label(self, text="Seu Nome:", font=("Arial", 12)).pack()  
        self.entry_nome = tk.Entry(self, font=("Arial", 12), width=25)  
        self.entry_nome.insert(0, "Jogador")
        self.entry_nome.pack(pady=4)

        # Sexo
        tk.Label(self, text="Sexo:", font=("Arial", 12)).pack(pady=(10, 0))
        self.var_sexo = tk.StringVar(value="masculino")
        frame_sexo = tk.Frame(self)
        frame_sexo.pack()
        for opcao in ["masculino", "feminino"]:
            tk.Radiobutton(
                frame_sexo, text=opcao.capitalize(),
                variable=self.var_sexo, value=opcao,
                font=("Arial", 11)
            ).pack(side="left", padx=10)  

        # Classe Social
        tk.Label(self, text="Classe Social:", font=("Arial", 12)).pack(pady=(10, 0))
        
        self.var_classe = tk.StringVar(value="Medio")
        frame_classe = tk.Frame(self)
        frame_classe.pack()
        for opcao in ["Rico", "Medio", "Pobre"]:
            tk.Radiobutton(
                frame_classe, text=opcao,
                variable=self.var_classe, value=opcao,
                font=("Arial", 11)
            ).pack(side="left", padx=8)

        
        tk.Label(
            self,
            text="Atributos iniciais sorteados ao confirmar:\nSaúde | Educação | Carisma (1–10)  |  Stress: 0",
            font=("Arial", 10), fg="gray"
        ).pack(pady=(16, 4))

        tk.Button(
            self, text="Confirmar →", width=18, font=("Arial", 12),
            command=self._confirmar
        ).pack(pady=8)

        tk.Button(
            self, text="← Voltar ao Menu", font=("Arial", 10),
            command=lambda: master.mostrar_tela("menu")  
        ).pack()

    def _confirmar(self):
        nome   = self.entry_nome.get().strip() or "Jogador"
        sexo   = self.var_sexo.get()
        classe = self.var_classe.get()
        self.master.personagem = Pessoa(nome, sexo, classe)
        self.master.mostrar_tela("introducao")


# ─────────────────────────────────────────────
# TELA 3 — INTRODUÇÃO
# ─────────────────────────────────────────────
class TelaIntroducao(tk.Frame):
    def __init__(self, master):
        super().__init__(master)   # BUG 15: era super().__int__() (typo)
        self.master = master

        tk.Label(self, text="📖 Introdução", font=("Arial", 18, "bold")).pack(pady=(20, 10))

        self.label_intro = tk.Label(
            self, wraplength=440, justify="left", font=("Arial", 11)
        )
        self.label_intro.pack(padx=20, pady=10)

        self.label_ficha = tk.Label(self, font=("Arial", 11, "bold"), fg="#444")
        self.label_ficha.pack(pady=(10, 4))

        tk.Button(
            self, text="Começar a jornada! →",
            width=23, font=("Arial", 12),
            command=self._iniciar_jogo
        ).pack(pady=14)

        tk.Button(
            self, text="← Voltar",
            font=("Arial", 10),
            command=lambda: master.mostrar_tela("criacao")
        ).pack()

    def atualizar(self):
        p = self.master.personagem
        pronome = "Bem-vindo" if p.sexo == "masculino" else "Bem-vinda"
        texto = (
            f"{pronome}, {p.nome}!\n\n"
            f"Você foi aceito(a) na Universidade para o curso de Biotecnologia. "
            f"À sua frente estão semestres cheios de desafios, amizades, "
            f"provas, festas e decisões difíceis.\n\n"
            f"Cada escolha que fizer vai moldar quem você se torna. "
            f"Suas habilidades serão testadas e você irá superar todas as adversidades "
            f"— ou não — dependendo do seu caminho.\n\n"
            f"Boa sorte, calouro(a)!"
        )
        self.label_intro.config(text=texto)   
        self.label_ficha.config(
            text=f"👤 {p.nome}  |  {p.sexo.capitalize()}  |  {p.classe_social}\n"
                 f"{p.resumo()}"
        )

    def _iniciar_jogo(self):
        self.master.gerenciador = GerenciarEventos()
        self.master.telas["jogo"] = TelaJogo(
            self.master, self.master.gerenciador, self.master.personagem
        )
        self.master.mostrar_tela("jogo")


# ─────────────────────────────────────────────
# TELA 4 — JOGO (EVENTOS)
# ─────────────────────────────────────────────
class TelaJogo(tk.Frame):
    def __init__(self, master, gerenciador: GerenciarEventos, personagem: Pessoa):
        super().__init__(master)
        self.gerenciador = gerenciador
        self.personagem  = personagem

        self.label_periodo = tk.Label(self, font=("Arial", 10, "bold"))
        self.label_periodo.pack(pady=(10, 0))

        self.label_atributos = tk.Label(self, font=("Arial", 10), fg="#333")
        self.label_atributos.pack()

        self.label_texto = tk.Label(
            self, wraplength=430, justify="center", font=("Arial", 12)
        )
        self.label_texto.pack(pady=16, padx=20)

        self.botoes = []
        for i in range(4):
            btn = tk.Button(
                self, width=48, anchor="w", font=("Arial", 10),
                command=lambda idx=i: self.escolher(idx)
            )
            btn.pack(pady=3, padx=10)
            self.botoes.append(btn)

        tk.Button(
            self, text="← Menu Principal",
            font=("Arial", 9),
            command=lambda: master.mostrar_tela("menu")
        ).pack(pady=8)

        self.carregar_evento()

    def _atualizar_cabecalho(self):
        p = self.personagem
        self.label_periodo.config(
            text=f"Período {p.periodo}  —  {p.nome} ({p.sexo} | {p.classe_social})"
        )
        self.label_atributos.config(text=p.resumo())

    def carregar_evento(self):
        self._atualizar_cabecalho()
        self.evento_atual = self.gerenciador.sortear_evento(self.personagem.periodo)

        if self.evento_atual is None:
            self.label_texto.config(
                text=(
                    "🎉 Parabéns! Depois de tantos desafios, "
                    "você concluiu seu curso de Biotecnologia!"
                )
            )
            for btn in self.botoes:
                btn.config(text="—", state="disabled")
            return

        self.label_texto.config(text=self.evento_atual["texto"])
        for i, btn in enumerate(self.botoes):
            opcao = self.evento_atual["opcoes"][i]
            btn.config(text=f"  {i+1}. {opcao['texto']}", state="normal")  

    def escolher(self, indice):
        opcao   = self.evento_atual["opcoes"][indice]
        efeitos = opcao.get("efeitos", {})

        self.personagem.aplicar_efeitos(efeitos)

        nomes = {
            "educacao": "Educação",
            "carisma":  "Carisma",
            "saude":    "Saúde",
            "stresse":  "Stress",
        }
        linhas = [f"Você escolheu:\n«{opcao['texto']}»\n"]
        for attr, val in efeitos.items():
            sinal = "+" if val >= 0 else ""
            linhas.append(f"  {nomes.get(attr, attr)}: {sinal}{val}")
        linhas.append(f"\n{self.personagem.resumo()}")

        messagebox.showinfo("Resultado da escolha", "\n".join(linhas))

        self.personagem.avancar_periodo()
        self.carregar_evento()


# ─────────────────────────────────────────────
# APLICAÇÃO PRINCIPAL
# ─────────────────────────────────────────────
class Jogo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo da Faculdade")
        self.geometry("540x480")
        self.resizable(False, False)

        self.personagem  = None   # criado em TelaCriacao._confirmar
        self.gerenciador = GerenciarEventos()

        self.telas: dict[str, tk.Frame] = {
            "menu":       Menu(self),
            "criacao":    TelaCriacao(self),
            "introducao": TelaIntroducao(self),
            # "jogo" é criada dinamicamente após o personagem existir
        }

        self.mostrar_tela("menu")

    def mostrar_tela(self, nome: str):
        for tela in self.telas.values():
            tela.pack_forget()

        if nome == "introducao" and self.personagem:
            self.telas["introducao"].atualizar()

        tela = self.telas.get(nome)
        if tela:
            tela.pack(fill="both", expand=True)


app = Jogo()
app.mainloop()