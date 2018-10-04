# ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
idade = int(raw_input("Idade: "))
tempo_servico = int(raw_input("Tempo de servico: "))
res = s.aposentadoria(idade, tempo_servico)
print res
# Print list of available methods
print s.system.listMethods()
