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
def categoria(idade):
  if idade < 5:
  	return "Nao participa"
  elif idade < 8:
  	return "Infantil A"
  elif idade < 11:
  	return "Infantil B"
  elif idade < 14:
  	return "Juvenil A"
  elif idade < 18:
  	return "Juvenil B"
  else:
  	return "Adulto"

server.register_function(categoria, 'update')

# Run the server's main loop
server.serve_forever()
