## Ducktype of polymorphsim in python
class Hen:
    def fly(self):
        print("Hen can fly.")


class Duck:
    def fly(self):
        print("Duck can fly")


def use_bird(b):
    b.fly()


ob = Hen()
ob1 = Duck()

use_bird(ob)
use_bird(ob1)
