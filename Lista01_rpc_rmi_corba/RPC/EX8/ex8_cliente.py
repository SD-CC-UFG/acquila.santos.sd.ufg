# ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
saldo = float(raw_input("Saldo: "))
res = s.update(saldo)
print res
# Print list of available methods
print s.system.listMethods()
