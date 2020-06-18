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
nombre = input("Ingrese nombre deseado del archivo csv")
ruta = input("Ingrese ruta del archivo")
try:
    data = open(ruta,"r").read()
    encoded = base64.b64encode(data)
    data.close()
    nomArchivo,archivo64 = client.service.algoritmo(nombre,data)
    archivo64 = archivo64.split(',',1)[1]
    xlDecoded = base64.b64decode(archivo64)
    xlFile = open(nomArchivo+'.xlsx','wb')
    xlFile.write(xlDecoded)
    xlFile.close()
    print("Se creo el archivo exitosamente")
except:
    print("Error al obtener datos, intente nuevamente")