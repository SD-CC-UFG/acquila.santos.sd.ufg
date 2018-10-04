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
def atualiza_salario(nome,cargo, salario):
    if cargo == 'operador':
        salario = salario * 1.2
    elif cargo == 'programador':
        salario = salario * 1.18
    return "Nome: %s\nSalario: %f" % (nome, salario)

server.register_function(atualiza_salario, 'update')

# Run the server's main loop
server.serve_forever()
