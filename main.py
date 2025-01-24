from database.pacotes import BancoDados
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
app = FastAPI()

db = BancoDados()

@app.get("/filmes")
def read_filmes():
    """
    Endpoint GET para listar todos os filmes cadastrados.
    :return: Uma lista de filmes no formato JSON.
    """
    
    lista = db.listar_todos_filmes()
    return lista

@app.get("/filmes/{filme_id}")
def read_filme(filme_id: int):
    """
    Endpoint GET para retornar os dados de um filme específico.
    :param filme_id: ID do filme a ser consultado.
    :return: Os dados do filme no formato JSON.
    """
    filme = db.listar_filme_por_id(filme_id)
    return filme

class Filme(BaseModel):
    NomeFilme: str
    DtLancamento: date 
    PaisOrigem: str | None = None
    ImdbId: str | None = None
    Direcao: str | None = None

@app.post("/filmes")
async def create_filme(filme: Filme):
    """
    Endpoint POST para adicionar um novo filme ao banco de dados.
    :param filme: Objeto com os dados do filme enviado no corpo da requisição.
    :return: Os dados do filme que foi cadastrado.
    """
    db.inserir_filme(filme)
    return filme