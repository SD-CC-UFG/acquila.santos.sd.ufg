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
def cred(saldo):
  if saldo < 200:
    return "Saldo Medio: %f\tNenhum Credito -> %f\n" % (saldo, saldo)
  elif saldo <= 600:
    return "Saldo Medio: %f\tPercentual de Credito: 0.3 -> %f\n"%(saldo, saldo * 0.3)
  elif saldo <= 400:
    return "Saldo Medio: %f\tPercentual de Credito: 0.2 -> %f\n"%(saldo, saldo * 0.2)
  else:
    return "Saldo Medio: %f\tPercentual de Credito: 0.4 -> %f\n"%(saldo, saldo * 0.4)


server.register_function(cred, 'update')

# Run the server's main loop
server.serve_forever()
