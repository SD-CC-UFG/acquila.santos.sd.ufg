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
  def salario_liq(self, nome, nivel, salario, dep):
    if nivel == "A":
      if dep:
        salario = salario * 0.97
      else:
        salario = salario * 0.92
    elif nivel == "B":
      if dep:
        salario = salario * 0.95
      else:
        salario = salario * 0.90
    elif nivel == "C":
      if dep:
        salario = salario * 0.98
      else:
        salario = salario * 0.85
    elif nivel == "D":
      if dep:
        salario = salario * 0.90
      else:
        salario = salario * 0.83

    return "Nome: %s\nNivel: %s\nSalario Liquido: %f\n" %(nome, nivel, salario)
    

server.register_instance(Pessoa())

# Run the server's main loop
server.serve_forever()
