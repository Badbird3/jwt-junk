import jwt

# todo, token token as cli input, see awss for a good module for that

token = "foo"

# todo
# get the 'exp' parameter and print it, then check to see how long until it expires

decoded = jwt.decode(token, options={"verify_signature": False}) # works in PyJWT >= v2.0
print (decoded)


