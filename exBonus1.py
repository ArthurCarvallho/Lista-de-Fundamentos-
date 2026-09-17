class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentacao(self):
        print(f"Olá, meu nome é {self.nome}, eu tenho {self.idade} anos.")
    
pessoa1 = Pessoa("Arthur", 18)
Pessoa.apresentacao(pessoa1)