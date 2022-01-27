import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# peguei isso de um link que obv q um dev front end escreveu de tao malfeito q tava, reajustei oq achei bom


hostName = "localhost"
serverPort = 8080 # You can choose any available port; by default, it is 8000

def checkRequest(response, headers, packageName):
    
    if not response in [200, 201, 500, 400, 404, 401, 403, 405]:
        if headers:
            if type(packageName) == str:
                return True
    return False
    


class MyServer(BaseHTTPRequestHandler):  
    def buildHTTPResponse(self, response, headers, packageFilename):
        #if checkRequest(response, headers, packageFilename):
            # response
        self.send_response(response)
        
        # headers 
        for header in headers:
            self.send_header(header[0], header[1])
        self.end_headers()

        # send packageFilename - eu assumi que devesse mandar linha por linha entao fiz esse for
        with open(packageFilename, 'r') as packageFile:
            for line in packageFile:
                self.wfile.write(bytes(line, "utf-8"))

# TRANSFORMAR EM JSON
# TESTAR POST E GET ENTRE O PC E O LAPTOP 

    def do_GET(self):
        print(os.listdir())
        
        self.buildHTTPResponse(200, [["Content-type", "application/json"]], "test.json")

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)    
        
        print("POST REQUEST RECEIVED - READING PACKAGE")
        print(post_body)
        
        self.buildHTTPResponse(200, [["Content-type", "application/json"]], "response.json")
        print("POST REQUEST RECEIVED - RESPONSE SENT")


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))  #Server starts
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass
    webServer.server_close()  #Executes when you hit a keyboard interrupt (ctrl + c), closing the server
    print("Server stopped.")