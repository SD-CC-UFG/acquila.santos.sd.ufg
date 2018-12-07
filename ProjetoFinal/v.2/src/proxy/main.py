from proxy import ServidorProxy
import sys

server = ServidorProxy(int(sys.argv[1]))
server.start()