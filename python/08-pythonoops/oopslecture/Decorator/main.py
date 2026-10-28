def extra(func):
     def wrap():
        print("Start")
        func()

      print("stop")
     return wrap

@extra
def greet():
    print("progress")
