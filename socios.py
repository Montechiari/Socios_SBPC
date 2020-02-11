import sqlite3
import pandas as pd


ENDERECO = "./"
NOME_BANCO = "socios.db"
ARQUIVO_DADOS_CSV = "socios.csv"


class Socio():
    def __init__(self, nome, email, ultimo_pago, local, instituicao):
        self.nome = nome
        self.email = email
        self.ultimo_pago = ultimo_pago
        self.local = local
        self.instituicao = instituicao


def gera_banco_de_dados():
    data_frame_socios = pd.read_csv(ENDERECO + ARQUIVO_DADOS_CSV, header=0)
    banco_de_dados = sqlite3.connect(ENDERECO + NOME_BANCO, uri=False)
    with banco_de_dados:
        data_frame_socios.to_sql("socios", banco_de_dados)
    return banco_de_dados


def faz_recorte(conexao, consulta):
    data_frame = pd.read_sql_query(consulta, conexao, index_col="nome")
    data_frame.drop_duplicates(inplace=True)
    return data_frame.drop(columns="index")


def inicializar():
    try:
        arquivo = ENDERECO + NOME_BANCO
        conexao = sqlite3.connect(f"file:{arquivo}?mode=rw", uri=True)
    except sqlite3.OperationalError:
        conexao = gera_banco_de_dados()
    except Exception as e:
        print(e)
    return conexao


if __name__ == '__main__':

    conexao = inicializar()
    print(faz_recorte(conexao,
                      "SELECT * FROM socios WHERE anuidade > 2018"))
