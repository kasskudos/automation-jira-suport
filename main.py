from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Define o código de resposta
        self.send_response(200)

        # Adiciona cabeçalhos
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Cria a resposta JSON
        response = {
            "currant_support_id": "PFDATSERV-1090"
        }

        # Envia a resposta
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor HTTP rodando na porta {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()