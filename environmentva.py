
import os
from dotenv import load_dotenv
load_dotenv()
a= os.getenv("API_KEY")
b= os.getenv("USER-NAME")
c= os.getenv("password")
print(f" your password is {c}, please assign some strong password")
print(b)
if a:
    print(f"api key is found, your api key is {a}" )
else:
    print("api key not found in env, first pass an api key into it")
