# ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
altura = float(raw_input("Altura: "))
sexo = raw_input("Sexo: ")
res = s.update(altura, sexo)
print "Peso ideal: %f" % (res)
# Print list of available methods
print s.system.listMethods()
