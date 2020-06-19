from zeep import Client
import base64
from zeep import Plugin

class MyLoggingPlugin(Plugin):
    def ingress(self, envelope, http_headers, operation):
        http_headers['Content-Type']='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; charset=utf-8;'
        return envelope, http_headers
    
    def egress(self, envelope, http_headers, operation, binding_options):
        http_headers['Content-Type']='text/csv; charset=utf-8;'
        return envelope, http_headers

client = Client('http://localhost:1204/?wsdl', plugins=[MyLoggingPlugin()])
nombre = input("Ingrese nombre deseado del archivo xlsx: ")
ruta = input("Ingrese ruta del archivo csv: ")
try:
    data = open(ruta,"rb").read()
    encoded = base64.b64encode(data)
    archivo64 = client.service.algoritmo(nombre,encoded)
    archivo64 = archivo64[0]
    xlDecoded = base64.b64decode(archivo64)
    xlFile = open(nombre+'.xlsx','wb')
    xlFile.write(xlDecoded)
    xlFile.close()
    print("Se creo el archivo exitosamente")
except:
    print("Error al ingresar los datos, intente nuevamente")
