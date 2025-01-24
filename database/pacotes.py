import sqlite3


class BancoDados():
    def __init__(self):
        # Conexão com o banco de dados SQLite e inicialização do cursor
        self.banco_dados = sqlite3.connect('database/movies.db',check_same_thread=False)
        self.cursor = self.banco_dados.cursor()

    def inserir_filme(self, filme: dict):
        """
        Insere um novo filme no banco de dados.
        :param filme: Um dicionário contendo os dados do filme (NomeFilme, DtLancamento, PaisOrigem, ImdbId, Direcao).
        """
        if filme.NomeFilme and filme.DtLancamento:
            self.cursor.execute('INSERT INTO filmes (NomeFilme, DtLancamento, PaisOrigem, ImdbId, Direcao) VALUES ( ?, ?, ?, ?, ?)', (filme.NomeFilme, filme.DtLancamento, filme.PaisOrigem, filme.ImdbId, filme.Direcao))
            self.banco_dados.commit()
        

    def listar_todos_filmes(self):
        """
        Retorna uma lista de todos os filmes cadastrados no banco de dados.
        :return: Uma lista de dicionários contendo os dados de cada filme.
        """
        lista_filmes = []
        retorno = self.cursor.execute("SELECT NomeFilme, DtLancamento, PaisOrigem, ImdbId, Direcao from filmes")
        filmes = retorno.fetchall()
        for filme in filmes:
            lista_filmes.append(
                {'NomeFilme': filme[0],
                 'DtLancamento': filme[1],
                 'PaisOrigem': filme[2],
                 'ImdbId': filme[3],
                 'Direcao': filme[4]}
            )
        return lista_filmes
    
    def listar_filme_por_id(self, id):
        """
        Retorna os dados de um filme específico, identificado pelo ID.
        :param id: ID do filme a ser consultado.
        :return: Um dicionário contendo os dados do filme.
        """
        retorno = self.cursor.execute("SELECT NomeFilme, DtLancamento, PaisOrigem, ImdbId, Direcao from filmes where IdFilme = ?", (int(id),))
        filme = retorno.fetchone()
        return {'NomeFilme': filme[0],
                 'DtLancamento': filme[1],
                 'PaisOrigem': filme[2],
                 'ImdbId': filme[3],
                 'Direcao': filme[4]}

