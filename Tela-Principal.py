import tkinter as tk
import random as rr
from tkinter import messagebox

# PERSONAGEM
class Pessoa:
    def __init__(self, nome, sexo):
        self.nome          = nome
        self.sexo          = sexo
        self.classe_social = rr.choice(['Rico', 'Medio', 'Pobre'])  
        self.periodo       = 1
        self.saude         = rr.randint(1, 5)
        self.inteligencia  = rr.randint(1, 5)
        self.carisma       = rr.randint(1, 5)
        self.stresse       = 0

    def avancar_periodo(self):
        self.periodo += 1

    def aplicar_efeitos(self, efeitos: dict):
        for attr, valor in efeitos.items():
            atual = getattr(self, attr, None)
            if atual is not None:
                setattr(self, attr, max(0, atual + valor))
 # Atributos
    def resumo(self) -> str:
        return (
            f"Saúde: {self.saude}  |  "
            f"Intel: {self.inteligencia}  |  "
            f"Car: {self.carisma}  |  "
            f"Stress: {self.stresse}"
        )

# DEPÓSITO DE EVENTOS

class DepositoEventos:
    def __init__(self):
        self.eventos = {
                                       # PERÍODO 1 
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
                         "efeitos": {"stresse": +3}},
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
                         "efeitos": {"carisma": -1, "inteligencia": +1}},
                        {"texto": "Sentar e ficar em silêncio",
                         "efeitos": {"carisma": -2}},
                        {"texto": "Tentar liderar a conversa",
                         "efeitos": {"carisma": +3, "stresse": +2}},
                    ]
                },
                {
                    "texto": "Você encontra um veterano nos corredores.",
                    "opcoes": [
                        {"texto": "Pedir dicas sobre a faculdade",
                         "efeitos": {"carisma": +1, "inteligencia": +1}},
                        {"texto": "Conversar sobre o curso",
                         "efeitos": {"carisma": +2}},
                        {"texto": "Apenas cumprimentar",
                         "efeitos": {"carisma": +1}},
                        {"texto": "Ignorar e seguir andando",
                         "efeitos": {"carisma": -1}},
                    ]
                },
            ],

                                         #  PERÍODO 2 
            "Periodo2": [
                {
                    "texto": "Você puxou uma matéria com um professor horrível.",
                    "opcoes": [
                        {"texto": "Estudar como nunca",
                         "efeitos": {"inteligencia": +5, "stresse": +4, "saude": -3}},
                        {"texto": "Viu a primeira aula e decidiu trancar",
                         "efeitos": {"inteligencia": -3, "stresse": -5}},
                        {"texto": "Fazer um grupo de estudos",
                         "efeitos": {"carisma": +3, "inteligencia": +3}},
                        # ★ Exclusivo Rico / Medio
                        {"texto": "Contratar um professor particular",
                         "efeitos": {"inteligencia": +4, "stresse": -2},
                         "restrito_a": ["Rico", "Medio"]},
                    ]
                },
                {
                    "texto": "Um trabalho em grupo é dado por um professor.",
                    "opcoes": [
                        {"texto": "Escolher bem as pessoas para pegar os melhores",
                         "efeitos": {"inteligencia": +2, "stresse": -1}},
                        {"texto": "Entrar no grupo que sobrar",
                         "efeitos": {"carisma": -1, "stresse": +1}},
                        {"texto": "Ir no grupinho de sempre",
                         "efeitos": {"carisma": +1, "stresse": -1}},
                        {"texto": "Perguntar se pode fazer sozinho",
                         "efeitos": {"stresse": -2, "carisma": -2}},
                    ]
                },
                {
                    "texto": "Há uma festa universitária acontecendo hoje à noite.",
                    "opcoes": [
                        {"texto": "Ir à festa e conhecer pessoas",
                         "efeitos": {"carisma": +2, "saude": -3}},
                        {"texto": "Ir apenas por algumas horas",
                         "efeitos": {"carisma": +1}},
                        {"texto": "Ficar em casa estudando",
                         "efeitos": {"inteligencia": +2, "stresse": +1, "saude": +3}},
                        # ★ Exclusivo Rico
                        {"texto": "Organizar uma festa no seu apartamento",
                         "efeitos": {"carisma": +4, "saude": -2, "stresse": -1},
                         "restrito_a": ["Rico"]},
                    ]
                },
            ],

                                         #  PERÍODO 3 
            "Periodo3": [
                {
                    "texto": (
                        "Um professor oferece uma pesquisa remunerada. "
                        "Mas vai tomar muito tempo."
                    ),
                    "opcoes": [
                        {"texto": "Aceitar mesmo tendo que atrasar matérias",
                         "efeitos": {"inteligencia": +3, "stresse": +2, "saude": -4}},
                        {"texto": "Aceitar mas negociar tempo para não atrasar",
                         "efeitos": {"inteligencia": +1, "stresse": +4, "saude": +1}},
                        {"texto": "Recusar educadamente",
                         "efeitos": {"stresse": -2, "inteligencia": -2}},
                        {"texto": "Ignorar o e-mail",
                         "efeitos": {"carisma": -2, "stresse": -1}},
                    ]
                },
                {
                    "texto": "Seu grupo ainda não começou o trabalho e o prazo está perto.",
                    "opcoes": [
                        {"texto": "Assumir a liderança",
                         "efeitos": {"carisma": +2, "stresse": +1}},
                        {"texto": "Organizar uma reunião",
                         "efeitos": {"carisma": +1}},
                        {"texto": "Fazer apenas sua parte",
                         "efeitos": {"inteligencia": +1}},
                        {"texto": "Deixar para a última hora",
                         "efeitos": {"stresse": +2}},
                    ]
                },
            ],

                                           #  PERÍODO 4 
            "Periodo4": [
                {
                    "texto": "O professor pede que os alunos formem duplas para um trabalho.",
                    "opcoes": [
                        {"texto": "Convidar alguém para fazer dupla",
                         "efeitos": {"carisma": +2, "stresse": -1}},
                        {"texto": "Esperar alguém te chamar",
                         "efeitos": {"carisma": -1, "stresse": +1}},
                        {"texto": "Fazer o trabalho sozinho",
                         "efeitos": {"inteligencia": +1, "stresse": +2}},
                        {"texto": "Pedir ajuda ao professor",
                         "efeitos": {"carisma": +1}},
                    ]
                },
                {
                    "texto": "A cantina está lotada durante o intervalo.",
                    "opcoes": [
                        {"texto": "Entrar na fila normalmente",
                         "efeitos": {"stresse": +1}},
                        {"texto": "Conversar com colegas enquanto espera",
                         "efeitos": {"carisma": +1, "stresse": -1}},
                        {"texto": "Pular o lanche",
                         "efeitos": {"saude": -2}},
                        # ★ Exclusivo Rico / Medio
                        {"texto": "Pedir delivery para comer na sala",
                         "efeitos": {"saude": +2, "stresse": -1},
                         "restrito_a": ["Rico", "Medio"]},
                    ]
                },
            ],

                                      # PERÍODO 5 
            "Periodo5": [
                {
                    "texto": "Você recebe uma oferta de estágio no meio do curso.",
                    "opcoes": [
                        {"texto": "Aceitar e equilibrar com a faculdade",
                         "efeitos": {"inteligencia": +2, "stresse": +3}},
                        {"texto": "Recusar para focar nos estudos",
                         "efeitos": {"inteligencia": +3, "stresse": -1}},
                        {"texto": "Aceitar e reduzir matérias",
                         "efeitos": {"carisma": +2, "inteligencia": -1}},
                        # ★ Exclusivo Rico
                        {"texto": "Recusar — família já garante seu futuro",
                         "efeitos": {"stresse": -5, "carisma": -1},
                         "restrito_a": ["Rico"]},
                    ]
                },
                {
                    "texto": "Um colega te pede para revisar o trabalho final dele.",
                    "opcoes": [
                        {"texto": "Ajudar com prazer",
                         "efeitos": {"carisma": +2, "stresse": +1}},
                        {"texto": "Ajudar rapidamente",
                         "efeitos": {"carisma": +1}},
                        {"texto": "Recusar, você está ocupado",
                         "efeitos": {"carisma": -1, "stresse": -1}},
                        {"texto": "Cobrar para ajudar",
                         "efeitos": {"carisma": -2, "stresse": -2}},
                    ]
                },
            ],

                                         #  PERÍODO 6 
            "Periodo6": [
                {
                    "texto": "A universidade oferece um intercâmbio de um semestre.",
                    "opcoes": [
                        # ★ Exclusivo Rico / Medio
                        {"texto": "Se inscrever no intercâmbio",
                         "efeitos": {"inteligencia": +4, "carisma": +2, "stresse": +2},
                         "restrito_a": ["Rico", "Medio"]},
                        {"texto": "Tentar uma bolsa para o intercâmbio",
                         "efeitos": {"inteligencia": +2, "stresse": +3}},
                        {"texto": "Ficar e aproveitar para se destacar",
                         "efeitos": {"inteligencia": +2, "carisma": +1}},
                        {"texto": "Ignorar a oportunidade",
                         "efeitos": {"stresse": -2}},
                    ]
                },
                {
                    "texto": "Você está sobrecarregado com provas e trabalhos.",
                    "opcoes": [
                        {"texto": "Enfrentar tudo de cabeça erguida",
                         "efeitos": {"inteligencia": +2, "stresse": +3, "saude": -2}},
                        {"texto": "Pedir extensão de prazo ao professor",
                         "efeitos": {"stresse": -2, "carisma": +1}},
                        {"texto": "Tirar um dia de descanso",
                         "efeitos": {"saude": +3, "stresse": -3, "inteligencia": -1}},
                        {"texto": "Trancar uma matéria",
                         "efeitos": {"stresse": -4, "inteligencia": -2}},
                    ]
                },
            ],

                                         # PERÍODO 7 
            "Periodo7": [
                {
                    "texto": "Você precisa escolher o tema do TCC.",
                    "opcoes": [
                        {"texto": "Tema inovador e desafiador",
                         "efeitos": {"inteligencia": +3, "stresse": +3}},
                        {"texto": "Tema seguro mas bem documentado",
                         "efeitos": {"inteligencia": +2, "stresse": +1}},
                        {"texto": "Tema sugerido pelo orientador",
                         "efeitos": {"carisma": +1, "stresse": -1}},
                        {"texto": "Copiar a estrutura de um TCC antigo",
                         "efeitos": {"stresse": -2, "inteligencia": -2, "saude": +1}},
                    ]
                },
                {
                    "texto": "Seu orientador cancela a reunião de orientação pela terceira vez.",
                    "opcoes": [
                        {"texto": "Mandar e-mail firme cobrando resposta",
                         "efeitos": {"carisma": -1, "stresse": -2}},
                        {"texto": "Procurar outro orientador",
                         "efeitos": {"carisma": +1, "stresse": +2}},
                        {"texto": "Continuar esperando pacientemente",
                         "efeitos": {"stresse": +3}},
                        {"texto": "Trabalhar sozinho enquanto isso",
                         "efeitos": {"inteligencia": +2, "stresse": +1}},
                    ]
                },
            ],

                                     #  PERÍODO 8 (FINAL) 
            "Periodo8": [
                {
                    "texto": (
                        "É sua apresentação final do TCC. "
                        "Tudo que você viveu na faculdade culmina neste momento."
                    ),
                    "opcoes": [
                        {"texto": "Apresentar com confiança e desenvoltura",
                         "efeitos": {"carisma": +2, "stresse": -2}},
                        {"texto": "Focar nos dados e argumentos técnicos",
                         "efeitos": {"inteligencia": +2, "stresse": -1}},
                        {"texto": "Improvisar — você conhece o assunto",
                         "efeitos": {"carisma": +1, "stresse": +2}},
                        {"texto": "Ler direto dos slides",
                         "efeitos": {"carisma": -2, "stresse": -3}},
                    ]
                },
            ],
        }

# GERENCIADOR DE EVENTOS
class GerenciarEventos(DepositoEventos):
    def __init__(self):
        super().__init__()

    def sortear_evento(self, periodo: int):
        chave = f"Periodo{periodo}"
        lista = self.eventos.get(chave, [])
        if not lista:
            return None
        return rr.choice(lista)

# TELA MENU

class Menu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Projeto F", font=("Arial", 20, "bold"), fg="#8A2BE2").pack(pady=40)
        tk.Button(self, text="Iniciar", width=18, font=("Arial", 12),
                  command=lambda: master.mostrar_tela("criacao")).pack(pady=8)
        tk.Button(self, text="Sair", width=18, font=("Arial", 12),
                  command=master.destroy).pack(pady=4)

# TELA CRIAÇÃO DE PERSONAGEM

class TelaCriacao(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="Crie seu Universitario",
                 font=("Arial", 20, "bold")).pack(pady=20)

        tk.Label(self, text="Seu Nome:", font=("Arial", 12)).pack()
        self.entry_nome = tk.Entry(self, font=("Arial", 12), width=25)
        self.entry_nome.insert(0, "Jogador")
        self.entry_nome.pack(pady=4)

        tk.Label(self, text="Sexo:", font=("Arial", 12)).pack(pady=(12, 0))
        self.var_sexo = tk.StringVar(value="masculino")
        frame_sexo = tk.Frame(self)
        frame_sexo.pack()
        for opcao in ["masculino", "feminino"]:
            tk.Radiobutton(frame_sexo, text=opcao.capitalize(),
                           variable=self.var_sexo, value=opcao,
                           font=("Arial", 11)).pack(side="left", padx=12)

        tk.Label(
            self,
            text=(
                "  Classe social, atributos (Saúde, Inteligência, Carisma)\n"
                "    serão sorteados automaticamente ao confirmar."
            ),
            font=("Arial", 10), fg="gray", justify="center"
        ).pack(pady=(18, 6))

        tk.Button(self, text="Confirmar →", width=18, font=("Arial", 12),
                  command=self._confirmar).pack(pady=8)
        tk.Button(self, text="← Voltar ao Menu", font=("Arial", 10),
                  command=lambda: master.mostrar_tela("menu")).pack()

    def _confirmar(self):
        nome = self.entry_nome.get().strip() or "Jogador"
        sexo = self.var_sexo.get()
        self.master.personagem = Pessoa(nome, sexo)   # classe sorteada dentro de Pessoa
        self.master.mostrar_tela("introducao")

# TELA INTRODUÇÃO

class TelaIntroducao(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text=" Introdução",
                 font=("Arial", 18, "bold")).pack(pady=(20, 10))

        self.label_intro = tk.Label(self, wraplength=460, justify="left",
                                    font=("Arial", 11))
        self.label_intro.pack(padx=20, pady=8)

        self.label_ficha = tk.Label(self, font=("Arial", 11, "bold"), fg="#444")
        self.label_ficha.pack(pady=(8, 4))

        tk.Button(self, text="Começar a jornada!", width=23, font=("Arial", 12),
                  command=self._iniciar_jogo).pack(pady=14)
        tk.Button(self, text=" Voltar", font=("Arial", 10),
                  command=lambda: master.mostrar_tela("criacao")).pack()

    def atualizar(self):
        p = self.master.personagem
        pronome = "Bem-vindo" if p.sexo == "masculino" else "Bem-vinda"
        classe_desc = {
            "Rico":  "uma família abastada — a faculdade está paga e certas portas já estão abertas.",
            "Medio": "uma família de classe média — você tem suporte, mas precisa se esforçar.",
            "Pobre": "uma família humilde — cada semestre é uma conquista.",
        }[p.classe_social]

        texto = (
            f"{pronome}, {p.nome}!\n\n"
            f"Você foi aceito(a) no curso dos seus sonhos. "
            f"Vem de {classe_desc}\n\n"
            f"À sua frente estão 8 períodos cheios de desafios, amizades, "
            f"provas e decisões difíceis."
            f"Equilibrar saude e estresse e vida social é importante.\n\n"
            f"Boa sorte, calouro(a)!"
        )
        self.label_intro.config(text=texto)
        self.label_ficha.config(
            text=(
                f"👤 {p.nome}  |  {p.sexo.capitalize()}  |  Classe: {p.classe_social}\n"
                f"{p.resumo()}"
            )
        )

    def _iniciar_jogo(self):
        self.master.gerenciador = GerenciarEventos()
        self.master.telas["jogo"] = TelaJogo(
            self.master, self.master.gerenciador, self.master.personagem
        )
        self.master.mostrar_tela("jogo")

# TELA GAME OVER

class TelaGameOver(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.label_titulo = tk.Label(self, font=("Arial", 22, "bold"), fg="#cc0000")
        self.label_titulo.pack(pady=(40, 8))

        self.label_motivo = tk.Label(self, font=("Arial", 13), wraplength=420,
                                     justify="center")
        self.label_motivo.pack(pady=8, padx=20)

        self.label_ficha = tk.Label(self, font=("Arial", 11), fg="#555")
        self.label_ficha.pack(pady=(14, 4))

        tk.Button(self, text=" Tentar novamente", width=22, font=("Arial", 12),
                  command=lambda: master.reiniciar()).pack(pady=14)
        tk.Button(self, text="← Menu Principal", font=("Arial", 10),
                  command=lambda: master.mostrar_tela("menu")).pack()

    def atualizar(self, motivo: str):
        p = self.master.personagem
        if motivo == "saude":
            self.label_titulo.config(text=" Foi forcado a trancar")
            self.label_motivo.config(
                text=(
                    f"{p.nome} acabou indo parar no hospital e teve que "
                    f"trancar o curso. A saúde para você não vem em primeiro lugar — "
                    f"mas desta você foi longe demais."
                )
            )
        else:  # stresse
            self.label_titulo.config(text=" COLAPSO NERVOSO")
            self.label_motivo.config(
                text=(
                    f"{p.nome} atingiu o limite do estresse e simplesmente "
                    f"não conseguiu mais continuar. "
                    f"Às vezes a faculdade cobra um preço alto demais."
                )
            )
        self.label_ficha.config(
            text=f"Período {p.periodo}  |  {p.resumo()}"
        )

# TELA FIM DE CURSO 
class TelaFimDeCurso(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.label_titulo = tk.Label(self, font=("Arial", 20, "bold"), fg="#0f960f")
        self.label_titulo.pack(pady=(30, 8))

        self.label_msg = tk.Label(self, font=("Arial", 12), wraplength=440,
                                  justify="center")
        self.label_msg.pack(pady=10, padx=20)

        self.label_ficha = tk.Label(self, font=("Arial", 11, "bold"), fg="#444")
        self.label_ficha.pack(pady=(14, 4))

        tk.Button(self, text=" Jogar novamente", width=22, font=("Arial", 12),
                  command=lambda: master.reiniciar()).pack(pady=14)
        tk.Button(self, text=" Menu Principal", font=("Arial", 10),
                  command=lambda: master.mostrar_tela("menu")).pack()

    def atualizar(self):
        p = self.master.personagem
        intel_alto = p.inteligencia > 5
        carisma_alto = p.carisma > 5

        if intel_alto and carisma_alto:
            titulo = " FORMATURA ÉPICA!"
            msg = (
                f"{p.nome}, você se formou com louvor! "
                f"Sua inteligência afiada e seu carisma irresistível "
                f"conquistaram professores e colegas. "
                f"O mercado de trabalho vai te receber de braços abertos. "
                f"Brilhante jornada, doutor(a)!"
            )
        elif intel_alto and not carisma_alto:
            titulo = " O GÊNIO SOLITÁRIO"
            msg = (
                f"Parabéns, {p.nome}! Seu conhecimento é invejável — "
                f"as notas falam por si. Mas ao longo do caminho você "
                f"deixou de cultivar relações. No mundo profissional, "
                f"inteligência sem rede de contatos pode travar voos. "
                f"Hora de trabalhar o lado humano!"
            )
        elif not intel_alto and carisma_alto:
            titulo = " O NETWORKER NATO"
            msg = (
                f"{p.nome}, você talvez não tenha as melhores notas, "
                f"mas todo mundo gosta de você! Sua capacidade de se "
                f"conectar com pessoas vai abrir portas que o currículo "
                f"sozinho não abre. Use isso a seu favor!"
            )
        else:
            titulo = " A JORNADA DIFÍCIL"
            msg = (
                f"{p.nome}, você chegou até o fim — e isso já é uma vitória! "
                f"A faculdade foi dura e você saiu sem grandes destaques, "
                f"mas o diploma na mão é real. Agora é recomeçar com "
                f"tudo que aprendeu no caminho."
            )

        self.label_titulo.config(text=titulo)
        self.label_msg.config(text=msg)
        self.label_ficha.config(
            text=(
                f"👤 {p.nome}  |  {p.sexo.capitalize()}  |  {p.classe_social}\n"
                f"{p.resumo()}"
            )
        )

# TELA JOGO (EVENTOS)

class TelaJogo(tk.Frame):
    NOMES_ATRIBUTOS = {
        "inteligencia": "Inteligência",
        "carisma":      "Carisma",
        "saude":        "Saúde",
        "stresse":      "Stress",
    }

    def __init__(self, master, gerenciador: GerenciarEventos, personagem: Pessoa):
        super().__init__(master)
        self.gerenciador = gerenciador
        self.personagem  = personagem

        self.label_periodo = tk.Label(self, font=("Arial", 12, "bold"))
        self.label_periodo.pack(pady=(10, 0))

        self.label_atributos = tk.Label(self, font=("Arial", 12), fg="#333")
        self.label_atributos.pack()

        self.label_texto = tk.Label(self, wraplength=460, justify="center",
                                    font=("Arial", 12))
        self.label_texto.pack(pady=14, padx=20)

        self.botoes = []
        for i in range(4):
            btn = tk.Button(self, width=52, anchor="w", font=("Arial", 10),
                            command=lambda idx=i: self.escolher(idx))
            btn.pack(pady=3, padx=10)
            self.botoes.append(btn)

        tk.Button(self, text="← Menu Principal", font=("Arial", 9),
                  command=lambda: master.mostrar_tela("menu")).pack(pady=8)

        self.carregar_evento()

    # Cabeçalho 
    def _atualizar_cabecalho(self):
        p = self.personagem
        self.label_periodo.config(
            text=f"Período {p.periodo}/8  —  {p.nome}  ({p.sexo.capitalize()} | {p.classe_social})"
        )
        self.label_atributos.config(text=p.resumo())

    # Carrega evento e filtra opções restritas
    def carregar_evento(self):
        self._atualizar_cabecalho()
        self.evento_atual = self.gerenciador.sortear_evento(self.personagem.periodo)

        # Período 8 concluído → tela de fim de curso
        if self.personagem.periodo > 8:
            self.master.telas["fim"] = TelaFimDeCurso(self.master)
            self.master.telas["fim"].atualizar()
            self.master.mostrar_tela("fim")
            return

        if self.evento_atual is None:
            self.label_texto.config(text=" Parabéns! Você concluiu todos os períodos!")
            for btn in self.botoes:
                btn.config(text="—", state="disabled")
            return

        # Filtra opções disponíveis para a classe social do jogador
        todas = self.evento_atual["opcoes"]
        self.opcoes_disponiveis = [
            op for op in todas
            if "restrito_a" not in op or self.personagem.classe_social in op["restrito_a"]
        ]

        # Garante ao menos 4 opções (repete a última se necessário)
        while len(self.opcoes_disponiveis) < 4:
            self.opcoes_disponiveis.append(self.opcoes_disponiveis[-1])

        self.label_texto.config(text=self.evento_atual["texto"])
        for i, btn in enumerate(self.botoes):
            op = self.opcoes_disponiveis[i]
            marcador = "⭐ " if "restrito_a" in op else "   "
            btn.config(text=f"{marcador}{i+1}. {op['texto']}", state="normal")

    # aqui processa escolha 
    def escolher(self, indice):
        opcao   = self.opcoes_disponiveis[indice]
        efeitos = opcao.get("efeitos", {})

        self.personagem.aplicar_efeitos(efeitos)

        # Monta feedback
        linhas = [f"Você escolheu:\n«{opcao['texto']}»\n"]
        for attr, val in efeitos.items():
            sinal = "+" if val >= 0 else ""
            linhas.append(f"  {self.NOMES_ATRIBUTOS.get(attr, attr)}: {sinal}{val}")
        linhas.append(f"\n{self.personagem.resumo()}")
        messagebox.showinfo("Resultado da escolha", "\n".join(linhas))

        # verificador de game over 
        p = self.personagem
        if p.saude <= 0:
            self._game_over("saude")
            return
        if p.stresse >= 10:
            self._game_over("stresse")
            return

        p.avancar_periodo()
        self.carregar_evento()

    def _game_over(self, motivo: str):
        go = TelaGameOver(self.master)
        self.master.telas["gameover"] = go
        go.atualizar(motivo)
        self.master.mostrar_tela("gameover")

# Parte principal 

class Jogo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo da Faculdade")
        self.geometry("560x510")
        self.resizable(False, False)

        self.personagem  = None
        self.gerenciador = GerenciarEventos()

        self.telas: dict[str, tk.Frame] = {
            "menu":       Menu(self),
            "criacao":    TelaCriacao(self),
            "introducao": TelaIntroducao(self),
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

    def reiniciar(self):
        """Destroi as telas dinâmicas e volta para a criação de personagem."""
        for chave in ["jogo", "gameover", "fim"]:
            if chave in self.telas:
                self.telas[chave].destroy()
                del self.telas[chave]
        self.personagem  = None
        self.gerenciador = GerenciarEventos()
        self.mostrar_tela("criacao")


app = Jogo()
app.mainloop()