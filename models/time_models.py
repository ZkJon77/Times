# Importa o objeto db de 'db', que fornece as funcionalidades do SQLAlchemy para interagir com o banco de dados
from db import db  

# Define a classe Carro que representa a tabela 'carros' no banco de dados
class time(db.Model):  
    # Define o nome da tabela no banco de dados
    __tablename__ = 'time'  

    # Define as colunas da tabela 'carros'
    id = db.Column(db.Integer, primary_key=True)  # Coluna para o ID do jogo, chave primária
    titulo = db.Column(db.String(80), nullable=False)  # Coluna para o titulo do jogo, não pode ser nulo
    liga = db.Column(db.String(80), nullable=False)  # Coluna para o genero do jogo, não pode ser nulo
    jogadores = db.Column(db.String(80), nullable=False)  # Coluna para o desenvolvedor do jogo, não pode ser nulo
    clube = db.Column(db.String(80), nullable=False)  # Coluna para a plataforma do jogo, não pode ser nulo

    # Método para retornar os dados do jogo
    #  como um dicionário
    def json(self):  
        return {
            'id': self.id,  # ID do jogo
            'titulo': self.titulo,  # titulo do jogo
            'liga': self.liga,  # genero do jogo
            'jogadores': self.jogadores,  # desenvolvedor do jogo
            'clube': self.clube  # Plataforma do jogo
        }
