# ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
nome = raw_input("Nome: ")
cargo = raw_input("Cargo: ")
salario = float(raw_input("Salario: "))
res = s.update(nome, cargo, salario)
print(res)

# Print list of available methods
print s.system.listMethods()
