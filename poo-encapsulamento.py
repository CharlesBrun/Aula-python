class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    # precisa inserir o setter para inserir um valor
    @x.setter
    def x(self, value):
        return self._x + value
    
    @x.deleter
    def x(self):
        self._x - 1
    
# foo = Foo(10)
# print(foo.x)

# foo.x = 10
# print(foo.x)

# del foo.x
# print(foo.x)

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")