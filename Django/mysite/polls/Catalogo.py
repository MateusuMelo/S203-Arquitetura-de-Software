from .database import Database
from datetime import datetime,date,time


class Filme:
    def __init__(self,titulo,ano_lancamento,diretor,genero,tempo):
        self.titulo = titulo
        self.ano_lancamento= datetime.strptime(ano_lancamento,'%d/%m/%Y')
        self.diretor = diretor
        self.genero = genero
        self.tempo = datetime.strptime(tempo,'%H:%M')

    def to_dict(self):
        return {
            'titulo': self.titulo,
            'ano_lancamento': self.ano_lancamento.strftime('%d/%m/%Y'),
            'diretor': self.diretor,
            'genero': self.genero,
            'duracao': self.tempo.strftime('%H:%M'),
        }

class Catalogo:
    def __init__(self):
        self.data = Database()

    def cadastro(self, filme:Filme):
        query = f"""INSERT INTO polls_filme (titulo, ano, diretor, genero, duracao) values ('{filme.titulo}','{filme.ano_lancamento.strftime('%Y/%m/%d')}','{filme.diretor}','{filme.genero}','{filme.tempo.strftime('%H:%M')}')"""
        return self.data.crud(query)

    def read(self):
        query = f"""SELECT * FROM polls_filme"""
        results = self.data.crud(query)
        filmes: Filme = []
        for rows in results:
            filmes.append(Filme(rows[1], rows[2].strftime('%d/%m/%Y'), rows[3], rows[4], rows[5].strftime('%H:%M')))
        return filmes


    def filter_date(self):
        query = f"""SELECT * FROM polls_filme ORDER BY ano"""
        results = self.data.crud(query)
        filmes:Filme = []
        for rows in results:
            filmes.append(Filme(rows[1],rows[2].strftime('%d/%m/%Y'),rows[3],rows[4],rows[5].strftime('%H:%M')))
        return filmes

    def filter_gen(self):
        query = f"""SELECT * FROM polls_filme ORDER BY genero"""
        results = self.data.crud(query)
        filmes:Filme = []
        for rows in results:
            filmes.append(Filme(rows[1],rows[2].strftime('%d/%m/%Y'),rows[3],rows[4],rows[5].strftime('%H:%M')))
        return filmes

    def filter_dir(self):
        query = f"""SELECT * FROM polls_filme ORDER BY diretor"""
        results = self.data.crud(query)
        filmes:Filme = []
        for rows in results:
            filmes.append(Filme(rows[1],rows[2].strftime('%d/%m/%Y'),rows[3],rows[4],rows[5].strftime('%H:%M')))
        return filmes
