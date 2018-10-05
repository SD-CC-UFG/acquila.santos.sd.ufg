# ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
  rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
class Pessoa:
  """docstring for Pessoa"""
  def aposentadoria(self, idade, tempo_servico):
    if idade > 65:
      return "Pode aposentar"
    if tempo_servico > 30:
      return "Pode aposentar"
    if idade > 60 and tempo_servico > 25:
      return "Pode aposentar"

    return "Nao pode aposentar"

server.register_instance(Pessoa())

# Run the server's main loop
server.serve_forever()
