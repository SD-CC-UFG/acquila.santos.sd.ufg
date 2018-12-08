from middle import MiddleWare
import argparse

parser = argparse.ArgumentParser(description="p2pProxy")
parser.add_argument('--proxyPort', nargs="+", type=int, default= [] , help='Define the default proxy ports')
args = parser.parse_args()
print args.proxyPort
m = MiddleWare(args.proxyPort)
m.start()
