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
class Carta():
  
  def func(self, naipe, valor):
    NAIPE =['Ouros','Paus','Copas','Espadas']
    VALOR = ['As', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valete', 'Rainha', 'Rei']
    return "%s de %s\n" % (VALOR[valor - 1], NAIPE[naipe - 1])

server.register_instance(Carta())

# Run the server's main loop
server.serve_forever()
