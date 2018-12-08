from p2p import send, receive
from cache import Cache

cache = Cache(9999999)

send(cache, "0.0.0.0", 4321)
