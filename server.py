import logging
logging.basicConfig(level=logging.DEBUG)
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode, String, ByteArray, File
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import base64
import algoritmo as a

_grupos = []
_carreras = []
_grupos, _carreras = a.CargarDatos()

class Hololive(ServiceBase):
    @rpc(String, Unicode, _returns=Iterable(String))
    def algoritmo(self, nombre, data):   
        _buckets = { 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
        base64_decoded = 0
        base64_decoded = base64.decodebytes(bytes(data, 'utf-8'))
        strng = base64_decoded.decode('utf-8')
        #data = a.Decode(data)
        a.ParseData(_buckets, _grupos, strng)
        a.EscribirExcel(_buckets, _carreras, nombre)
        yield a.EncodeFile(nombre).decode('utf-8')


application = Application([Hololive],
    tns='data_cool.algoritmo',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    wsgi_app = WsgiApplication(application, max_content_length=60 * 0x100000)
    server = make_server('0.0.0.0', 1204, wsgi_app)
    server.serve_forever()
