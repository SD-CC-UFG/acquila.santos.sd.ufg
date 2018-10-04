# ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
valor = int(raw_input("Valor: "))
naipe = int(raw_input("Naipe: "))
res = s.func(naipe, valor)
print res
# Print list of available methods
print s.system.listMethods()
