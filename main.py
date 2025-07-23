from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Variável global para armazenar o current_support_id
current_support_id = "PFDATSERV-2442"

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        # Manipula requisições HEAD, respondendo apenas com os cabeçalhos
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/ping':
            # Responde com "pong" para o endpoint /ping
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"message": "pong"}
            self.wfile.write(json.dumps(response).encode('utf-8'))

        elif self.path == '/getCurrentSupportId':
            # Responde com o current_support_id dinâmico
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "current_support_id": current_support_id
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))

        else:
            # Handler para rotas não encontradas (404)
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"error": "Endpoint não encontrado"}
            self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_POST(self):
        if self.path == '/updateCurrentSupportId':
            # Lê o comprimento do corpo da requisição
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                # Tenta interpretar o corpo como JSON
                data = json.loads(post_data)
                new_support_id = data.get("current_support_id")

                if new_support_id:
                    # Atualiza a variável global
                    global current_support_id
                    current_support_id = new_support_id

                    # Responde com sucesso
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = {"message": "current_support_id atualizado com sucesso"}
                else:
                    # Responde com erro, se a chave não foi encontrada
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = {"error": "Chave 'current_support_id' não encontrada no corpo da requisição"}

            except json.JSONDecodeError:
                # Responde com erro se o corpo não for um JSON válido
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"error": "JSON inválido"}

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
