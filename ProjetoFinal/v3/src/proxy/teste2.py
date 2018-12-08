from p2p import send, receive

obj = receive(4321)

r = obj.existingUrl("url")

print r