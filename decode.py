import jwt
import argparse

# todo, token token as cli input, use argeparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('jwt', metavar='J', type=str, nargs='+',
                    help='enter a jwt')
args = parser.parse_args()
print(args.accumulate(args.integers))

#token = "foo"

# todo
# get the 'exp' parameter and print it, then check to see how long until it expires

#decoded = jwt.decode(token, options={"verify_signature": False}) # works in PyJWT >= v2.0
#print (decoded)


