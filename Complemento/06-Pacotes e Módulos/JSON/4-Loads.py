import json

a = ["Mathew", "Peter", (10, 32.9, 80), {"Name": "Tokio"}]

b = json.dumps(a)
c = json.loads(b)

print(c)
