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
def maioridade(nome, sexo, idade):
  if sexo == "masculino":
    if idade >=  18:
      return True
    else:
      return False
  elif sexo == "feminino":
    if idade >= 21:
      return True
    else:
      return False


server.register_function(maioridade, 'update')

# Run the server's main loop
server.serve_forever()
