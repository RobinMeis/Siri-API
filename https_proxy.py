""" HTTPS Proxy try. If it is set as proxy, it produces the error from screenshot.png """

from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import BaseServer
import ssl

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.path == "http://siri.smartnoob.de/"):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes('Succesfully redirected, I could do much more here', "utf-8"))
        else:
            self.send_response(301)
            self.send_header("Location", "http://siri.smartnoob.de/")
            self.end_headers()


if __name__ == '__main__':
    HTTPSPROXY = HTTPServer(('', 8080), HTTPRequestHandler)
    HTTPSPROXY.socket = ssl.wrap_socket (HTTPSPROXY.socket, certfile='cert.pem', server_side=True)
    HTTPSPROXY.serve_forever()