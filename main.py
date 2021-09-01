import jwt
import time 
from time import gmtime
from time import strftime

print("JWT Lifetime Checker v1.0!")
print ("Enter a JWT")
my_jwt = input("Paste in a JWT plz: ")
decoded = jwt.decode(my_jwt, verify=False)
jwt_time = (decoded["exp"])

def converter(jwt_time):
    clean_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(jwt_time))
    print (clean_time)


print('The expiration time of the inputted JWT is: ')
print(converter(jwt_time)) # This is an int
print("The current time is: ")
print(converter(time.time())) # This is a none type


if int(jwt_time) <= int(time.time()):
    difference = int(time.time()) - (decoded["exp"])
    print("The supplied JWT is expired, plz get a fresh JWT and try again.")
    print("The token expired this many minutes ago: ")
    print(int(difference) / 60)
else:
    fresh_difference =  (decoded["exp"]) - int(time.time())
    print("The supplied JWT is not expired.")
    print("The token will expire in this many minutes: ")
    print(int(fresh_difference) / 60)
    