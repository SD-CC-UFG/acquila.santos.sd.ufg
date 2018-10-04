# ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
notas = [0, 0]
notas[0] = int(raw_input("Nota 1: "))
notas[1] = int(raw_input("Nota 2: "))
res = s.update(notas)
print res
# Print list of available methods
print s.system.listMethods()
