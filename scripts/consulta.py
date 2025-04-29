from sqlalchemy.orm import sessionmaker
from config.conexao import engine
from models.funcionario import Funcionario

Session = sessionmaker(bind=engine)
Session = Session()

cidade_busca = input("Digite a cidade para buscar os funcionários: ")
resultado = Session.query(Funcionario).filter(Funcionario.cidade == cidade_busca).all()

if resultado:
    print(f"\nFuncionários encontrados em {cidade_busca}:")
    for pessoa in resultado:
        print(f"ID: {pessoa.id} | Nome: {pessoa.nome} | Idade: {pessoa.idade} | Profissão: {pessoa.profissao}")
else:
    print(f"\nNenhum funcionário encontrado em {cidade_busca}.")


Session.close()