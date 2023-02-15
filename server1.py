import socket
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "192.168.1.164"
port = int("8080")
sleep = float("0")

s.connect((ip, port))

for i in range(1, 100 * 10000):
  s.send(random._urandom(10) * 1000)
  print(f"Send: {i}", end='\r')
  time.sleep(sleep)