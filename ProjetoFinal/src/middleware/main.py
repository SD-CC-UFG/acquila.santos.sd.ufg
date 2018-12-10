from middle import MiddleWare
import argparse

parser = argparse.ArgumentParser(description="p2pProxy")
parser.add_argument('--cluster', nargs="+", type=int, default= [] , help='Define the default proxy ports')
parser.add_argument('--host', type=str, default= 'localhost', help='Define the middleware host')
args = parser.parse_args()
print args.cluster
m = MiddleWare(args.cluster, args.host)
m.start()
