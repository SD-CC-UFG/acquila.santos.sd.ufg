# ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
nome = raw_input("Nome: ")
sexo = raw_input("Sexo: ")
idade = int(raw_input("Idade: "))
res = s.update(nome, sexo, idade)
if res is True:
	print "Ok"
else:
	print "Nop"

# Print list of available methods
print s.system.listMethods()
