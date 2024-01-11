def decor(func):
     def wrap():
      print("there is somethig above this")
      res=func()
      print("there is something behind it")
      return res
     return wrap
@decor
def greet():
    return ("helloooo")
result=greet()
print(result)
        