from config.conexao import engine
from models.funcionario import Funcionario, base
from sqlalchemy.orm import sessionmaker

# Aqui estou criando uma sessão para inserir funcionarios na minha tabela nova
Session = sessionmaker(bind=engine)
Session = Session()

novo_funcionario1 = Funcionario(
    nome = "Gustavo Augusto",
    idade = 20,
    cidade = "Mauá",
    profissao = "Engenheiro de dados"
)

novo_funcionario2 = Funcionario(
    nome = "Yasmin Kamilly Machado",
    idade = 19,
    cidade = "Mauá",
    profissao = "Psicóloga"
)

novo_funcionario3 = Funcionario(
    nome = "Neymar Da Silva Santos Junior",
    idade = 33,
    cidade = "Santos",
    profissao = "Jogador de Futebol"
)

Session.add(novo_funcionario1)
Session.add(novo_funcionario2)
Session.add(novo_funcionario3)
Session.commit()
Session.close()