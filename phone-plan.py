# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':


# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:    
    
# TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo: 
    

# Classe UsuarioTelefone:
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

# TODO: Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:
    def verificar_saldo(self):
        return self.plano.mensagem_personalizada()
 

class PlanoTelefone:
    def __init__(self, nome, saldo):
        self._nome = nome
        self._saldo = saldo

    def verificar_saldo(self):
        return self._saldo
    
    def mensagem_personalizada(self):
        saldo = self.verificar_saldo()
        if saldo < 10:
            return saldo,  "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif saldo >= 50:
            return saldo, "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return saldo, "Seu saldo está razoável. Aproveite o uso moderado do seu plano."


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

 # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)