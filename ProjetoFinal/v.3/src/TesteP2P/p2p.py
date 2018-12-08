#!/usr/bin/python
from time import time
import argparse
from uuid import uuid4
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.task import LoopingCall
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
import json

class ProtocolP2P(Protocol):
	def __init__(self, factory, peertype = "1"):
		self.factory = factory
		self.state = "HELLO"
		self.remote_nodeid = None
		self.lc_ping = LoopingCall(self.send_ping)
		self.lastping = None
		self.peertype = peertype
		self.nodeid = self.factory.nodeid

	def connectionMade(self):
		remote_ip = self.transport.getPeer()
		host_ip = self.transport.getHost()
		self.remote_ip = remote_ip.host + ":" + str(remote_ip.port)
		self.host_ip = host_ip.host + ":" + str(host_ip.port)
		print "Connection from", self.transport.getPeer()
		
	def connectionLost(self, reason):
		if self.remote_nodeid in self.factory.peers:
				self.factory.peers.pop(self.remote_nodeid)
				self.lc_ping.stop()
		print self.nodeid, "disconnected"

	def dataReceived(self, data):
		for line in data.splitlines():
			line = line.strip()
			msgtype = json.loads(line)['msgtype']
			if self.state == "HELLO":
				self.handle_hello(line)
				self.state = "READY"
			elif msgtype == "ping":
				self.handle_ping()
			elif msgtype == "pong":
				self.handle_pong()
			elif msg_type == "getaddr":
				self.handle_getaddr()

	def send_addr(self, mine=False):
		now = time()
		if mine:
			peers = [self.host_ip]
		else:
			peers = [(peer.remote_ip, peer.remote_nodeid) for peer in self.factory.peers if peer.peertype == 1 and peer.lastping > now-240]
		addr = json.puts({'msgtype': 'addr', 'peers': peers})
		self.transport.write(peers + "\n")

	def handle_addr(self, addr):
		json = json.loads(addr)
		for remote_ip, remote_nodeid in json["peers"]:
			if remote_node not in self.factory.peers:
				host, port = remote_ip.split(":")
				point = TCP4ClientEndpoint(reactor, host, int(port))
				d = connectProtocol(point, ProtocolP2P(2))
				d.addCallback(gotProtocol)

	def handle_getaddr(self, getaddr):
		self.send_addr()

	def send_ping(self):
		ping = json.puts({'msgtype': 'ping'})
		print "Ping", self.remote_nodeid
		self.transport.write(ping + "\n")

	def handle_ping(self, ping):
		self.send_pong()

	def send_pong(self):
		ping = json.puts({'msgtype': 'pong'})
		self.transport.write(pong + "\n")

	def handle_pong(self, pong):
		print "Got pong from", self.remote_nodeid
		self.lastping = time()

	def send_hello(self):
		hello = json.puts({'nodeid': self.nodeid, 'msgtype': 'hello'})
		self.transport.write(hello + "\n")

	def handle_hello(self, hello):
		hello = json.loads(hello)
		self.remote_nodeid = hello["nodeid"]
		if self.remote_nodeid == self.nodeid:
				print "Connected to myself."
				self.transport.loseConnection()
		else:
				self.factory.peers[self.remote_nodeid] = self
				self.lc_ping.start(60)
				self.send_addr(mine=True)
				self.send_getaddr()

def gotProtocol(p):
	"""Callback to start the protocol exchange.""" 
	p.send_hello()

class MyFactory(Factory):

	def startFactory(self):
		self.peers = {}
		self.nodeid = generate_nodeid()

	def buildProtocol(self, addr):
		return ProtocolP2P(self)

# DEFAULT_PORT = 5005

BOOTSTRAP_LIST = [ "localhost:5999"
								 , "localhost:5998"
								 , "localhost:5997" ]

# parser = argparse.ArgumentParser(description="ncpoc")
# parser.add_argument('--port', type=int, default=DEFAULT_PORT)
# parser.add_argument('--listen', default="127.0.0.1")
# parser.add_argument('--bootstrap', action="append", default=[])


# args = parser.parse_args()
# try:
# 	endpoint = TCP4ServerEndpoint(reactor, args.port, interface=args.listen)
# 	print "Listen: " + args.listen + "port: " + args.port
# 	factory = MyFactory()
# 	endpoint.listen(factory)
# except Exception as e:
# 	raise SystemExit
endpoint = TCP4ServerEndpoint(reactor, 5999)
factory = MyFactory()
endpoint.listen(factory)


for bootstrap in BOOTSTRAP_LIST:
	host, port = bootstrap.split(":")
	point = TCP4ClientEndpoint(reactor, host, int(port))
	d = connectProtocol(point, ProtocolP2P(factory))
	d.addCallback(gotProtocol)
reactor.run()


