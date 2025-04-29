from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Aqui vou fazer com que o código leia o meu .env para esconder as minhas informações pessoais.
load_dotenv()
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
porta = os.getenv("PORTA")
host = os.getenv("HOST")
banco = os.getenv("BANCO")

# Criando a engine para fazer conexão com o banco de dados do Mysql.
engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}")

# Testando a conexão com o banco de dados.
try:
    conexao = engine.connect()
    print("Tudo certo com a conexão!")
    conexao.close()
except Exception as e:
    print(f"A conexão com o banco de dados falhou! {e}")
