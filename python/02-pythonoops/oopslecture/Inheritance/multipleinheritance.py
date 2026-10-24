# ============================================================
# MULTIPLE INHERITANCE IN PYTHON - Complete Example
# ============================================================
# What is Multiple Inheritance?
# -> When ONE child class inherits from MORE THAN ONE parent class.
# -> Syntax: class Child(Parent1, Parent2):
#
# Here: Robot(Human, Animal) means Robot gets qualities of BOTH.
# ============================================================


# ------------------------------------------------------------
# PARENT CLASS 1 : Animal
# ------------------------------------------------------------
# Represents animal qualities like name, eating, sleeping.
class Animal:
    # __init__ is the CONSTRUCTOR. Runs automatically on object creation.
    # self -> refers to current object.
    # name -> animal name, e.g. "Dog".
    # **kwargs -> collects extra args (like id, model) and forwards them
    #              to NEXT class in MRO. This is "cooperative inheritance".
    #              Without this, multiple inheritance __init__ chain breaks.
    def __init__(self, name, **kwargs):
        # super() means "call next parent in line (MRO)".
        # For Robot(Human, Animal), MRO is: Robot -> Human -> Animal -> object.
        # So this eventually reaches object.__init__().
        super().__init__(**kwargs)
        # Store name as instance variable (each object has own copy).
        self.name = name

    # Every Animal can eat. Returns string so caller can print or use it.
    def eat(self):
        return f"{self.name} is eating food."

    # Every Animal can sleep.
    def sleep(self):
        return f"{self.name} is sleeping."

    # Generic animal sound. Robot will OVERRIDE this later.
    def make_sound(self):
        return f"{self.name} makes a sound."


# ------------------------------------------------------------
# PARENT CLASS 2 : Human
# ------------------------------------------------------------
# Represents human qualities like id, thinking, behaviour.
class Human:
    # id -> unique identity number, e.g. 101.
    # NOTE: `id` is also a Python built-in name, so professional code
    # normally uses `human_id`. We keep `id` same as YOUR original code.
    def __init__(self, id, **kwargs):
        # Forward remaining args (like `name`) to next class in MRO.
        super().__init__(**kwargs)
        self.id = id

    # YOUR original method was: def behaviour(self): print()
    # Problem: it printed empty line, did nothing useful.
    # Fix: now returns meaningful behaviour using self.id.
    def behaviour(self):
        return f"Human with ID {self.id} shows kind and intelligent behaviour."

    # Extra human quality: thinking.
    def think(self):
        return f"Human {self.id} is thinking logically."


# ------------------------------------------------------------
# CHILD CLASS : Robot (Multiple Inheritance)
# ------------------------------------------------------------
# Robot inherits from BOTH Human AND Animal.
# Order matters: class Robot(Human, Animal)
# Python follows MRO (Method Resolution Order) left to right.
# MRO here = Robot -> Human -> Animal -> object
# Check with: print(Robot.__mro__) or Robot.mro()
class Robot(Human, Animal):
    # Robot has OWN quality (model) + BOTH parents qualities (name, id).
    def __init__(self, name, id, model):
        # super() goes to Human.__init__ first (Human is first).
        # Human takes `id`, forwards `name` via **kwargs to Animal.
        # Animal takes `name` and calls object.__init__.
        # One line initialises ALL parents. This is the correct pattern.
        super().__init__(name=name, id=id)
        # Robot own attribute.
        self.model = model

    # Robot own special method (not in parents).
    def work(self):
        return f"Robot {self.model} is working non-stop without rest."

    # METHOD OVERRIDING: same name as parent, new implementation.
    # Robot overrides make_sound() of Animal to give robotic sound.
    def make_sound(self):
        return f"Robot {self.model} says: Beep-Boop!"

    # Method that USES qualities from both parents together.
    def display_info(self):
        # self.name comes from Animal, self.id from Human,
        # self.model from Robot itself.
        print("----- Robot Info -----")
        print(f"Name  : {self.name}")  # from Animal
        print(f"ID    : {self.id}")  # from Human
        print(f"Model : {self.model}")  # own
        print(f"Eat   : {self.eat()}")  # Animal method reused
        print(f"Think : {self.think()}")  # Human method reused
        print(f"Work  : {self.work()}")  # own method
        print(f"Sound : {self.make_sound()}")  # overridden method
        print("----------------------")


# ------------------------------------------------------------
# DEMO / OBJECT CREATION (runs only when file run directly)
# ------------------------------------------------------------
# __name__ == "__main__" means "run below only if we do:
# python multipleinheritance.py, NOT on import".
if __name__ == "__main__":
    # Create ONE Robot object. Needs all three values.
    robo = Robot(name="RoboDog", id=101, model="RX-100")

    # 1. Show combined info (both parents + own).
    robo.display_info()

    # 2. Also show fixed behaviour() method explicitly.
    print("Behaviour:", robo.behaviour())
    print("Sleep:", robo.sleep())

    # 3. Show MRO: order Python searches for methods.
    print("\nMRO (Method Resolution Order):")
    for cls in Robot.mro():
        print(" ->", cls.__name__)

    # 4. Prove Robot is instance of both parents.
    print("\nIs robo a Human?", isinstance(robo, Human))  # True
    print("Is robo an Animal?", isinstance(robo, Animal))  # True
    print("Is robo a Robot?", isinstance(robo, Robot))  # True
