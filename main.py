import jwt
import time 
from time import gmtime
from time import strftime

print ("Enter a JWT")
my_jwt = input("Paste in a JWT plz: ")
decoded = jwt.decode(my_jwt, verify=False)
jwt_time = (decoded["exp"])

def converter(jwt_time):
    clean_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(jwt_time))
    print (clean_time)


print('The expiration time of the inputted JWT is: ')
print(jwt_time) # int
#print(type(decoded["exp"]))
print("The current time is: ")
print(converter(time.time())) #none type
#print(type(int(time.time())))
print("Age of token in seconds:")

difference = int(time.time()) - (decoded["exp"])
print(difference)

print(strftime("%H:%M:%S", gmtime(difference))) # print difference in minutes   

#print(int(time.time()) - (decoded["exp"]))