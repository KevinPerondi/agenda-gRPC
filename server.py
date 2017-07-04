from concurrent import futures
import time
import grpc
import collections
import agenda_pb2
import agenda_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Manager(agenda_pb2_grpc.ManagerServicer):

    def __init__(self):
        self.contactsList = dict()

    def AddPessoa(self, request, context):
        if request.nome not in self.contactsList:
            print(request)
            self.contactsList[request.nome] = request
            return agenda_pb2.BooleanReply(reply = True)
        return agenda_pb2.BooleanReply(reply = False)

    def DelPessoa(self, request, context):
        if request.nome in self.contactsList:
            print(self.contactsList[request.nome])
            del self.contactsList[request.nome]
            return agenda_pb2.BooleanReply(reply = True)
        return agenda_pb2.BooleanReply(reply = False)

    def BuscaPessoa(self, request, context):
       for pessoa in self.contactsList.values():
            if request.nome.lower() in pessoa.nome.lower():
                yield pessoa

    def ListaAgenda(self, request, context):
        for person in self.contactsList.values():
            yield person

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agenda_pb2_grpc.add_ManagerServicer_to_server(Manager(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
