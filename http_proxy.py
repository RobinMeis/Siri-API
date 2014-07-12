""" Basic Python3 HTTP Proxy which redirects all traffic on port 8080 to http://www.siri.smartnoob.de """

from http.server import BaseHTTPRequestHandler, HTTPServer

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

    HTTPProxy = HTTPServer(('', 8080), HTTPRequestHandler)
    HTTPProxy.serve_forever()
    input("Press key to exit")
    HTTPProxy.server_close()