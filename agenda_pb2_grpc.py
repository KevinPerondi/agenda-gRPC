# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import agenda_pb2 as agenda__pb2


class ManagerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddPessoa = channel.unary_unary(
        '/Manager/AddPessoa',
        request_serializer=agenda__pb2.Pessoa.SerializeToString,
        response_deserializer=agenda__pb2.BooleanReply.FromString,
        )
    self.DelPessoa = channel.unary_unary(
        '/Manager/DelPessoa',
        request_serializer=agenda__pb2.NomePessoa.SerializeToString,
        response_deserializer=agenda__pb2.BooleanReply.FromString,
        )
    self.BuscaPessoa = channel.unary_stream(
        '/Manager/BuscaPessoa',
        request_serializer=agenda__pb2.NomePessoa.SerializeToString,
        response_deserializer=agenda__pb2.Pessoa.FromString,
        )
    self.ListaAgenda = channel.unary_stream(
        '/Manager/ListaAgenda',
        request_serializer=agenda__pb2.ContactsRequest.SerializeToString,
        response_deserializer=agenda__pb2.Pessoa.FromString,
        )


class ManagerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def AddPessoa(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DelPessoa(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BuscaPessoa(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListaAgenda(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ManagerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddPessoa': grpc.unary_unary_rpc_method_handler(
          servicer.AddPessoa,
          request_deserializer=agenda__pb2.Pessoa.FromString,
          response_serializer=agenda__pb2.BooleanReply.SerializeToString,
      ),
      'DelPessoa': grpc.unary_unary_rpc_method_handler(
          servicer.DelPessoa,
          request_deserializer=agenda__pb2.NomePessoa.FromString,
          response_serializer=agenda__pb2.BooleanReply.SerializeToString,
      ),
      'BuscaPessoa': grpc.unary_stream_rpc_method_handler(
          servicer.BuscaPessoa,
          request_deserializer=agenda__pb2.NomePessoa.FromString,
          response_serializer=agenda__pb2.Pessoa.SerializeToString,
      ),
      'ListaAgenda': grpc.unary_stream_rpc_method_handler(
          servicer.ListaAgenda,
          request_deserializer=agenda__pb2.ContactsRequest.FromString,
          response_serializer=agenda__pb2.Pessoa.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Manager', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
