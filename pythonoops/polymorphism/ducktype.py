# Duck type polymorphism what method can do not what method it is 
class pen:
    def use(self):
        print("writing...")

class eraser:
    def use(self):
        print("Removing...")

def tool(obj):
    return obj.use()

a=pen()
b=eraser()
tool(a)
tool(b)