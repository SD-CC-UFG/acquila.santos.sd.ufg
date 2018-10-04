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
def aprovado(notas):
  media = (notas[0] + notas[1])/2
  if media >= 7.0:
    return "Aprovado"
  elif media >= 3.0:
    return "Fazer N3"
  else:
    return "Reprovado"


server.register_function(aprovado, 'update')

# Run the server's main loop
server.serve_forever()
