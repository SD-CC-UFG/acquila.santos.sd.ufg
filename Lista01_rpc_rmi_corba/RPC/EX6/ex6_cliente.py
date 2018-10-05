# ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
nome = raw_input("Nome: ")
nivel = raw_input("Nivel: ")
salario = float(raw_input("Salario: "))
dep = int(raw_input("Dependentes: "))
res = s.salario_liq(nome, nivel, salario, dep)
print res
# Print list of available methods
print s.system.listMethods()
