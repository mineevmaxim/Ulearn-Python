from xmlrpc.server import SimpleXMLRPCServer

host = '127.0.0.32'
port = 12345

with SimpleXMLRPCServer((host, port)) as server:
    def get_sqrt_of_discriminant(a, b, c):
        return (b*b-4*a*c)**0.5
    server.register_function(get_sqrt_of_discriminant)

    server.serve_forever()
    