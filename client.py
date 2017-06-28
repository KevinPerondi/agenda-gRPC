"""The Python implementation of the GRPC agenda.Greeter client."""

from __future__ import print_function

import grpc

import agenda_pb2
import agenda_pb2_grpc


def set_value(stub, v1, v2):
	request = stub.ContactValues(name=v1, fone=v2)
	response = stub.addContact(request, TIMEOUT_SECONDS)
	return response

def run():
	channel = grpc.insecure_channel('localhost:50051')
	stub = agenda_pb2_grpc.AgendaRemotaStub(channel)
	set_value(stub,"Juaum","5122")
	#response = stub.addContact(stub.ContactValues(name='Robson', fone='+5544999981234'))
	#print("Client received: " + response.messageConfirm)

if __name__ == '__main__':
	run()