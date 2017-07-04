from __future__ import print_function
import grpc
import agenda_pb2
import agenda_pb2_grpc

def addPessoa():
    pessoa = agenda_pb2.Pessoa()
    pessoa.nome = input('Nome: ')
    pessoa.celular = input('Celular: ')
    pessoa.telefone = input('Telefone: ')
    return pessoa


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = agenda_pb2_grpc.ManagerStub(channel)
    option = 0

    while option != 5:
        print('1 - Adicionar contato')
        print('2 - Remover contato')
        print('3 - Buscar contato pelo nome')
        print('4 - Listar todos os contatos')
        print('5 - Sair')
        option = int(input('Option: '))
        
        if option == 1:
            pessoa = addPessoa()
            response = stub.AddPessoa(pessoa)
            if response.reply:
                print('Contato inserido com sucesso!')
            else:
                print('Contato com mesmo nome já existe na sua agenda!')
        elif option == 2:
            nome = input('Insira o nome do contato que deseja remover: ')
            response = stub.DelPessoa(agenda_pb2.NomePessoa(nome = nome))
            if response.reply:
                print('Contato removido com sucesso!')
            else:
                print('Contato inexistente')
        elif option == 3:
            nome = input('Insira o nome do contato que deseja buscar: ')
            contactslist = stub.BuscaPessoa(agenda_pb2.NomePessoa(nome = nome))
            for pessoa in contactslist:
                print(pessoa)
        elif option == 4:
            contactslist = stub.ListaAgenda(agenda_pb2.ContactsRequest(ListaAgenda = True))
            for pessoa in contactslist:
                print(pessoa)

if __name__ == '__main__':
  run()