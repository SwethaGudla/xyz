data='{"name":"soma","location":"Hyd"}'
x=json.loads(data,object_hook=lambda d: namedtuple('x',d.keys()) (*d.values()))
print(x.name,x.location)
