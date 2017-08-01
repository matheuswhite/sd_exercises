import httplib

ip = "127.0.0.1"
port = 8000

conn = httplib.HTTPConnection(ip, port)
conn.request("GET", "/index.html")
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print data1
conn.close()
