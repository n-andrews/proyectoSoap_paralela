import sys
input_file = str(sys.argv[1])

import base64
data = open(input_file, 'rb').read()
base64_encoded = base64.b64encode(data)
file = open("output.bin", 'wb').write(base64_encoded)

## Este script sirve para crear un archivo que es un string de b64 para simular el request sin tener que montar el srever y usar soap ui pq vale callampa
