import base64
import json

data = input()
print(base64.b64encode(data.encode()).decode())