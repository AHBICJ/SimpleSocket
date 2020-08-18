from socket import *
from concurrent.futures import ThreadPoolExecutor


def process(sock, addr):
    sentence = sock.recv(1024).decode()
    capitalized_sentence = sentence.upper()
    sock.send(capitalized_sentence.encode())
    sock.close()


serverPort = 12200
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(10)
print('The server is ready to receive')
pool = ThreadPoolExecutor(10)

while True:
    client_sock, client_addr = serverSocket.accept()
    pool.submit(process, client_sock, client_addr)
