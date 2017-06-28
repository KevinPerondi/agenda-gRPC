"""The Python implementation of the GRPC agenda.Greeter server."""

from concurrent import futures
import time

import grpc

import agenda_pb2
import agenda_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(agenda_pb2_grpc.AgendaRemotaServicer):

	def addContact(self, request, context):
		return agenda_pb2.Confirm(messageConfirm = 'Contact %s/%s added!' %request.name %request.fone)

	def removeContact(self, request, context):
		return agenda_pb2.Confirm(messageConfirm = 'Contact %s/%s removed!' %request.name %request.fone)

	def checkContact(self, request, context):
		return agenda_pb2.Confirm(messageConfirm = 'Contact %s/%s exists!' %request.name %request.fone)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  agenda_pb2_grpc.add_AgendaRemotaServicer_to_server(Greeter(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  print ("Server is running...")
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
