from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String
from config.conexao import engine

# Vcou criar uma base no qual todas minhas classes vao herdar.
base = declarative_base()

# Criando a classe Funcionario que vai representar a tabela funcionarios que ainda vai ser crida!
class Funcionario(base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    idade = Column(Integer)
    cidade = Column(String(100))
    profissao = Column(String(150))

# Aqui vou fazer a tabela ser criada.
base.metadata.create_all(engine)
