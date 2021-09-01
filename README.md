## JWT Lifetime Checker
is a simple script for checking JWT token expiration. The script will parse a JWT and return the tokens expiration date and how long that is from the present. 
 
Usage:
```
$python3 main.py
Enter a JWT
Paste in a JWT plz: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2NsYWltcyI6eyJwcm92aWRlciI6ImZhY2Vib29rIiwic3ViIjoiMTAxNTUxMzk1ODI2MzgxMzEiLCJlbWFpbCI6ImdlbnpvcmdAZ21haWwuY29tIn0sImp0aSI6ImU0ZDliYWU0LTljMjItNGY4YS1iNDI0LTU5YTQ1MTk0NmJkYyIsImV4cCI6MTUxMDc0MTQ0MSwiZnJlc2giOmZhbHNlLCJpYXQiOjE1MTA3NDA1NDEsInR5cGUiOiJhY2Nlc3MiLCJuYmYiOjE1MTA3NDA1NDEsImlkZW50aXR5Ijp7InByb3ZpZGVyIjoiZmFjZWJvb2siLCJpZCI6IjEwMTU1MTM5NTgyNjM4MTMxIiwiZW1haWwiOiJnZW56b3JnQGdtYWlsLmNvbSJ9fQ.cgAdiXbbp9KhaOgdbFGPCqDSNW01tPaKBL7r4roHvDg
```
Note: JWT in tmp jwt.txt is a random JWT found in pastebin. 

## TODO
- [] add classes to python files
- [] add .gitignore
- [] use std input instead of input
- [] create burp extension