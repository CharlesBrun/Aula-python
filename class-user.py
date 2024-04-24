# TODO: Crie uma classe UsuarioTelefone.  
# TODO: Defina um método especial `__init__`, que é o construtor da classe.
# O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.

class UsuarioTelefone:
    def __init__(self, numero, plano, nome = None):
        self._nome = nome
        self.numero = numero
        self.plano = plano

    # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Entrada:
nome = input()  
numero = input()  
plano = input()  
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:

usuario = UsuarioTelefone(numero=numero, plano=plano)
usuario.nome = nome

print(usuario)