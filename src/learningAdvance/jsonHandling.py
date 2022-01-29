#Handle the JSON parameters:

import json
try:
    a = '{"name":"prince","surname":"shivhare","age":"29"}'
    data = json.loads(a)
    print(data["hello"])
except:
    print("invalid json")
