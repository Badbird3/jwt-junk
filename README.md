## JWT Lifetime Checker
is a simple script for checking JWT token expiration. The script will parse a JWT and return the tokens expiration date and how long that is from the present. 
 
Usage:
```
$python3 main.py
Enter a JWT
Paste in a JWT plz: [enter fresh jwt here]
```
Use the following format for jwt:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE2MzA1MzEzNzB9.VUf5k9sVYyyqCDU1G-EvRJWIc-zGVFhwiCwO8qlagi4
```
Note: JWT in tmp jwt.txt generated from jwt.io

## TODO
- [] add classes to python files
- [] add .gitignore
- [] use std input instead of input
- [] create burp extension