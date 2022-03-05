import socket
import logging
import json
import threading

from LiteLogger import LiteLoggerHandler

# NOTE: This is not fully functioning yet!

PORT = 3001

d = None

TEST_R = b'POST / HTTP/1.1\r\nHost: localhost:3001\r\nUser-Agent: python-requests/2.27.1\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\nConnection: keep-alive\r\nBearer: Vqv83gM-SLAjVyuPiuBY0a52NQM6q-2kQviwV8ks\r\nContent-Length: 168\r\n\r\n'

def echo_server():
  print("running echo server")
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(('localhost', PORT))
  s.listen(1)

  conn, addr = s.accept()
  print('Connected by', addr)
  while 1:
      data = conn.recv(1024)
      if not data: break
      conn.sendall(bytes(True))
      # conn.sendall(data)
  conn.close()


if __name__ == '__main__':
    # create logger

    t = threading.Thread(target=echo_server)
    t.start()

    log = logging.getLogger('')
    log.setLevel(logging.INFO)

    # create a custom http logger handler
    llhandler = LiteLoggerHandler(
        "MyLS",
        url = f'http://localhost:{PORT}',
        verbose=True
    )

    # llhandler.setLevel(logging.INFO)

    # add handler to logger
    log.addHandler(llhandler)

    log.info('Hello world!', extra={
        'metadata':{'k':'v'},
        'tags': ['something', 'something elses']
    })
