from http.server import BaseHTTPRequestHandler, HTTPServer
 import json

 class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
     def do_GET(self):
         if self.path == '/ping':
             # Responde com "pong" para o endpoint /ping
             self.send_response(200)
             self.send_header('Content-type', 'application/json')
             self.end_headers()
             response = {"message": "pong"}
             self.wfile.write(json.dumps(response).encode('utf-8'))

         elif self.path == '/getCurrentSupportId':
             # Responde com o suporte atual para o endpoint /getCurrentSupportId
             self.send_response(200)
             self.send_header('Content-type', 'application/json')
             self.end_headers()
             response = {
                 "current_support_id": "PFDATSERV-1090"
             }
             self.wfile.write(json.dumps(response).encode('utf-8'))

         else:
             # Handler para rotas não encontradas (404)
             self.send_response(404)
             self.send_header('Content-type', 'application/json')
             self.end_headers()
             response = {"error": "Endpoint não encontrado"}
             self.wfile.write(json.dumps(response).encode('utf-8'))

 def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
     server_address = ('', port)
     httpd = server_class(server_address, handler_class)
     print(f'Servidor HTTP rodando na porta {port}')
     httpd.serve_forever()

 if __name__ == '__main__':
     run()