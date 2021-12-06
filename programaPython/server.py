import time
from http.server import BaseHTTPRequestHandler, HTTPServer

# peguei isso de um link que obv q um dev front end escreveu de tao malfeito q tava, reajustei oq achei bom


hostName = "localhost"
serverPort = 8080 # You can choose any available port; by default, it is 8000

def checkRequest(response, headers, package):
    
    if not response in [200, 201, 500, 400, 404, 401, 403, 405]:
        if headers:
            if type(package) == str:
                return True
    return False
    


class MyServer(BaseHTTPRequestHandler):  
    def buildHTTPResponse(self, response, headers, package):
        if checkRequest(response, headers, package):
            # response
            self.send_response(response)
            
            # headers 
            for header in headers:
                self.send_header(header[0], header[1])
            self.end_headers()

            # send package - eu assumi que devesse mandar linha por linha entao fiz esse for
            for line in package:
                self.wfile.write(bytes(line, "utf-8"))
    


    def do_GET(self):
        self.send_response(200)    
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://testserver.com</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))  #Server starts
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass
    webServer.server_close()  #Executes when you hit a keyboard interrupt, closing the server
    print("Server stopped.")

