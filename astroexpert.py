import tkinter as tk
from tkinter import ttk, messagebox

# ASTROEXPERT
# Classificação de Planetas


REGRAS = {

    # Regras de localização
    "R01": (
        "Se o planeta orbita o Sol, "
        "então sua localização é Sistema Solar."
    ),

    "R02": (
        "Se o planeta orbita uma estrela diferente do Sol, "
        "então sua localização é Exoplaneta."
    ),

    # Regras de tipo físico
    "R03": (
        "Se o planeta possui superfície sólida "
        "e composição predominante de rochas e metais, "
        "então é um Planeta Rochoso."
    ),

    "R04": (
        "Se o planeta não possui superfície sólida convencional, "
        "possui composição predominante de hidrogênio e hélio, "
        "atmosfera densa e grande massa, "
        "então é um Gigante Gasoso."
    ),

    "R05": (
        "Se o planeta não possui superfície sólida convencional, "
        "possui materiais voláteis/gelo e atmosfera significativa, "
        "então é um Gigante de Gelo."
    )
}


def classificar_planeta(dados):

    regras_ativadas = []

    if dados["localizacao"] == "Sistema Solar":

        localizacao = "Sistema Solar"

        regras_ativadas.append("R01")

    else:

        localizacao = "Exoplaneta"

        regras_ativadas.append("R02")


    if (
        dados["superficie"] == "Sim"
        and
        dados["composicao"] == "Rochas e metais"
    ):

        tipo_fisico = "Planeta Rochoso"

        regras_ativadas.append("R03")

    elif (
        dados["superficie"] == "Não"
        and
        dados["composicao"] == "Hidrogênio e hélio"
        and
        dados["atmosfera"] == "Densa"
        and
        dados["massa"] == "Grande"
    ):

        tipo_fisico = "Gigante Gasoso"

        regras_ativadas.append("R04")



    elif (
        dados["superficie"] == "Não"
        and
        dados["composicao"] == "Materiais voláteis/gelo"
        and
        dados["atmosfera"] in ["Densa", "Significativa"]
    ):

        tipo_fisico = "Gigante de Gelo"

        regras_ativadas.append("R05")


    else:

        tipo_fisico = "Tipo físico indeterminado"


    if tipo_fisico == "Tipo físico indeterminado":

        classificacao_final = (
            f"{localizacao} — "
            "Tipo físico indeterminado"
        )

    else:

        classificacao_final = (
            f"{localizacao} — "
            f"{tipo_fisico}"
        )


    # Retorna todas as informações
    return (
        localizacao,
        tipo_fisico,
        classificacao_final,
        regras_ativadas
    )


class AstroExpert:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "AstroExpert - Sistema Especialista"
        )

        self.root.geometry("700x720")

        self.root.resizable(False, False)

        self.criar_interface()

    def criar_interface(self):


        titulo = tk.Label(
            self.root,
            text="🌌 AstroExpert",
            font=("Arial", 28, "bold")
        )

        titulo.pack(pady=(20, 5))


        subtitulo = tk.Label(
            self.root,
            text=(
                "Sistema Especialista para "
                "Classificação de Planetas"
            ),
            font=("Arial", 12)
        )

        subtitulo.pack(pady=(0, 15))


        explicacao = tk.Label(
            self.root,
            text=(
                "Informe as características do planeta.\n"
                "O sistema determinará sua localização e seu tipo físico."
            ),
            font=("Arial", 10),
            justify="center"
        )

        explicacao.pack(pady=5)

        frame = tk.Frame(self.root)

        frame.pack(
            fill="both",
            expand=True,
            padx=60,
            pady=10
        )

        self.criar_campo(
            frame,
            "1. Onde o planeta está localizado?",
            [
                "Sistema Solar",
                "Fora do Sistema Solar"
            ],
            "localizacao"
        )

        self.criar_campo(
            frame,
            "2. O planeta possui superfície sólida?",
            [
                "Sim",
                "Não"
            ],
            "superficie"
        )

        self.criar_campo(
            frame,
            "3. Qual é sua composição predominante?",
            [
                "Rochas e metais",
                "Hidrogênio e hélio",
                "Materiais voláteis/gelo"
            ],
            "composicao"
        )

        self.criar_campo(
            frame,
            "4. Como é sua atmosfera?",
            [
                "Densa",
                "Significativa",
                "Fina",
                "Ausente"
            ],
            "atmosfera"
        )


        self.criar_campo(
            frame,
            "5. Qual é sua massa aproximada?",
            [
                "Pequena",
                "Média",
                "Grande"
            ],
            "massa"
        )

        frame_botoes = tk.Frame(self.root)

        frame_botoes.pack(pady=15)


        botao_analisar = tk.Button(
            frame_botoes,
            text="🔍 ANALISAR PLANETA",
            font=("Arial", 12, "bold"),
            width=22,
            height=2,
            command=self.analisar
        )

        botao_analisar.grid(
            row=0,
            column=0,
            padx=10
        )


        botao_limpar = tk.Button(
            frame_botoes,
            text="↻ LIMPAR",
            font=("Arial", 12, "bold"),
            width=12,
            height=2,
            command=self.limpar
        )

        botao_limpar.grid(
            row=0,
            column=1,
            padx=10
        )


    def criar_campo(
        self,
        frame,
        titulo,
        opcoes,
        nome_variavel
    ):

        campo_frame = tk.LabelFrame(
            frame,
            text=titulo,
            font=("Arial", 10, "bold"),
            padx=10,
            pady=8
        )

        campo_frame.pack(
            fill="x",
            pady=6
        )


        combo = ttk.Combobox(
            campo_frame,
            values=opcoes,
            state="readonly",
            font=("Arial", 10)
        )

        combo.pack(
            fill="x"
        )


        # Guarda o campo dentro do objeto
        setattr(
            self,
            nome_variavel,
            combo
        )


    def analisar(self):

        campos = [
            self.localizacao,
            self.superficie,
            self.composicao,
            self.atmosfera,
            self.massa
        ]


        for campo in campos:

            if not campo.get():

                messagebox.showwarning(
                    "Dados incompletos",
                    "Preencha todas as características "
                    "antes de realizar a análise."
                )

                return


        dados = {

            "localizacao":
                self.localizacao.get(),

            "superficie":
                self.superficie.get(),

            "composicao":
                self.composicao.get(),

            "atmosfera":
                self.atmosfera.get(),

            "massa":
                self.massa.get()
        }

        (
            localizacao,
            tipo_fisico,
            classificacao_final,
            regras
        ) = classificar_planeta(dados)


        self.exibir_resultado(
            localizacao,
            tipo_fisico,
            classificacao_final,
            regras
        )


    def exibir_resultado(
        self,
        localizacao,
        tipo_fisico,
        classificacao_final,
        regras
    ):

        janela = tk.Toplevel(
            self.root
        )

        janela.title(
            "Resultado - AstroExpert"
        )

        janela.geometry(
            "680x620"
        )

        janela.resizable(
            False,
            False
        )


        titulo = tk.Label(
            janela,
            text="🔭 RESULTADO DA ANÁLISE",
            font=("Arial", 22, "bold")
        )

        titulo.pack(
            pady=(25, 15)
        )

        label_localizacao = tk.Label(
            janela,
            text="LOCALIZAÇÃO",
            font=("Arial", 11, "bold")
        )

        label_localizacao.pack()


        resultado_localizacao = tk.Label(
            janela,
            text=localizacao,
            font=("Arial", 18)
        )

        resultado_localizacao.pack(
            pady=(2, 15)
        )


        label_tipo = tk.Label(
            janela,
            text="TIPO FÍSICO",
            font=("Arial", 11, "bold")
        )

        label_tipo.pack()


        resultado_tipo = tk.Label(
            janela,
            text=tipo_fisico,
            font=("Arial", 20, "bold")
        )

        resultado_tipo.pack(
            pady=(2, 20)
        )


        frame_classificacao = tk.LabelFrame(
            janela,
            text="Classificação final",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=15
        )

        frame_classificacao.pack(
            fill="x",
            padx=40,
            pady=10
        )


        resultado_final = tk.Label(
            frame_classificacao,
            text=classificacao_final,
            font=("Arial", 16, "bold")
        )

        resultado_final.pack()


        frame_regras = tk.LabelFrame(
            janela,
            text="Regras utilizadas pelo Sistema Especialista",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )

        frame_regras.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=10
        )


        texto = tk.Text(
            frame_regras,
            height=8,
            width=70,
            wrap="word",
            font=("Arial", 9)
        )

        texto.pack(
            fill="both",
            expand=True
        )


        for regra in regras:

            texto.insert(
                tk.END,
                f"{regra} — {REGRAS[regra]}\n\n"
            )


        texto.config(
            state="disabled"
        )


        botao_fechar = tk.Button(
            janela,
            text="Fechar",
            font=("Arial", 10, "bold"),
            width=12,
            command=janela.destroy
        )

        botao_fechar.pack(
            pady=15
        )

    def limpar(self):

        self.localizacao.set("")
        self.superficie.set("")
        self.composicao.set("")
        self.atmosfera.set("")
        self.massa.set("")

if __name__ == "__main__":

    root = tk.Tk()

    app = AstroExpert(root)

    root.mainloop()