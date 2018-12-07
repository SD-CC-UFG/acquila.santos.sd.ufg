import argparse
import socket

BOOTSTRAP_LIST = [ "localhost:5999"
                 , "localhost:5998"
                 , "localhost:5997" ]

DEFAULT_PORT = 5005

parser = argparse.ArgumentParser(description="ncpoc")
parser.add_argument('--port', type=int, default=DEFAULT_PORT)
parser.add_argument('--listen', default="127.0.0.1")
parser.add_argument('--bootstrap', action="append", default=[])


def Server(self)
	p2pSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	p2pSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	#p2pSocket.settimeout( timeout )
	p2pSocket.bind(("localhost", parser.port))
	p2pSocket.listen(3)

	conn, addr = p2pSocket.accept()
	