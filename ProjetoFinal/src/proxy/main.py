from proxy import ServidorProxy
import argparse

parser = argparse.ArgumentParser(description="p2pProxy")
parser.add_argument('--port', type=int, default= 4321 , help='Define the proxy port')
parser.add_argument('--host', type=str, default= 'localhost', help='Define the proxy host')
args = parser.parse_args()

server = ServidorProxy(args.port, args.host)
server.start()