import sqlite3
import pandas as pd


ENDERECO = "./"
NOME_BANCO = "socios.db"
ARQUIVO_DADOS_CSV = "dados_de_socios.csv"


class Socio():
    def __init__(self, nome, email, ultimo_pago, local, instituicao):
        self.nome = nome
        self.email = email
        self.ultimo_pago = ultimo_pago
        self.local = local
        self.instituicao = instituicao


def gera_banco_de_dados():
    data_frame_socios = pd.read_csv(ENDERECO + ARQUIVO_DADOS_CSV, header=0)
    campos = ", ".join(data_frame_socios.columns.values)

    banco_de_dados = sqlite3.connect(ENDERECO + NOME_BANCO, uri=False)
    # meu_cursor = banco_de_dados.cursor()
    # print(campos)
    # meu_cursor.execute(f"create table socios ({campos})")

    with banco_de_dados:
        data_frame_socios.to_sql("socios", banco_de_dados)

    print("fim!")

#
# def carrega_instrucoes():
#     with open(ENDERECO + "gerador_SQL", "r") as arquivo:
#         instrucoes = arquivo.read()
#     return instrucoes


if __name__ == '__main__':
    try:
        arquivo = ENDERECO + NOME_BANCO
        conexao = sqlite3.connect(f"file:{arquivo}?mode=rw", uri=True)
    except sqlite3.OperationalError:
        gera_banco_de_dados()
    except Exception as e:
        print(e)
