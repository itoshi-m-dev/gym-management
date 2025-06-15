
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log_academia.txt'


class NotificaçãoMixin:
    def enviar_notificação(self,msg,):
        mensagem = f'Notificação para {self.nome} : {msg}'

        with open(LOG_FILE, 'a',encoding='utf-8') as arquivo:
            print('Salvando log...')
            arquivo.write(mensagem)
            arquivo.write('\n')

class Pessoa:
    def __init__(self,nome,idade,id):
        self.nome = nome
        self.idade = idade
        self.id = id

class Aluno(Pessoa,NotificaçãoMixin):
    def __init__(self, nome, idade, id):
        super().__init__(nome, idade, id)
        self._exercicios = []

    def listar_treino(self):
        print(f'\n Treino de {self.nome}')
        for ex in self._exercicios:
            print(ex)

    def adicionar_exercicios(self,exercicio):
        self._exercicios.append(exercicio)
        self.enviar_notificação('Novo exercicio adicionado:', exercicio)

class Instrutor(Pessoa, NotificaçãoMixin):
    def __init__(self, nome, idade, id,especialidade):
        super().__init__(nome, idade, id)
        self._especialidades = especialidade
        self._alunos = []
    
    def adicionar_aluno(self,aluno):
        self._alunos.append(aluno)
        self.enviar_notificação(f'Aluno adicionado com sucesso: {aluno}')
    
    def listar_alunos(self):
        print(f'\nAlunos de {self.nome}')
        for aluno in self._alunos:
            print(aluno)

class Exercicio:
    def __init__(self,nome,grpmuscular,duracao):
        self.nome = nome
        self.grpmuscular = grpmuscular
        self.duracao = duracao

    def atualizar_duracao(self,nova_duracao):
        self.duracao = nova_duracao

class Academia(NotificaçãoMixin):
    def __init__(self,nome):
        self.nome = nome
        self.alunos = []
        self.instrutores = []
        self.exercicios = []

    def cadastrar_alunos(self,aluno):
        self.alunos.append(aluno)
        self.enviar_notificação(f'Aluno novo na academia: {aluno}')
    
    def cadastrar_instrutor(self,instrutor):
        self.instrutores.append(instrutor)
        self.enviar_notificação(f'Novo instrutor na academia: {instrutor} ')
    
    def cadastrar_exercicio(self,exercicio):
        self.exercicios.append(exercicio)
        self.enviar_notificação(f'Novo exercicio na academia: {exercicio}')

    def listar_exercicios(self):
        def listar_exercicios(self):
            print(f"\nExercícios disponíveis na academia {self.nome}:")
        for ex in self.exercicios:
            print(f"- {ex.nome} ({ex.grpmuscular}) - {ex.duracao} min")

if __name__ == '__main__':
    joao = Aluno('Joao', 20, 1)
    ava = Instrutor('Ava Max', 30, 2, 'Musculação')
    ex1 = Exercicio('Cadeira Extensora', 'Pernas', 30)
    acad = Academia('Panobianco')
    acad.cadastrar_alunos(joao.nome)
    acad.cadastrar_instrutor(ava.nome)
    acad.cadastrar_exercicio(ex1.nome)




    
            




