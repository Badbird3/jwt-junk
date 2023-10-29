# generate a private key first

import jwt 

private_key = '-----BEGIN PRIVATE KEY-----\n'
private_key += '\n'
private_key += '-----END PRIVATE KEY-----'

payload = {}

encoded = jwt.encode(payload, private_key, algorithm="RS256")

print(encoded)