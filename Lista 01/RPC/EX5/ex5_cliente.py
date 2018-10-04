# ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
idade = int(raw_input("Iade: "))
res = s.update(idade)
print res
# Print list of available methods
print s.system.listMethods()
