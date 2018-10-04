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
def peso(idade):
  if idade < 5:
  	return (62.1 * altura) - 44.7
  else:
  	return (72.7 * altura) - 58

server.register_function(peso, 'update')

# Run the server's main loop
server.serve_forever()
