## Multi level inheritance


class BagFactory:
    def __init__(self, materal, zips, pockets):
        self.material = materal
        self.zips = zips
        self.pockets = pockets

    # instance method
    def detail(self):
        print("Your bag detials are: ")
        print(self.material)
        print(self.zips)
        print(self.pockets)


class Rebook(BagFactory):
    def __init__(self, materal, zips, pockets, color):
        super().__init__(materal, zips, pockets)
        self.color = color

    def detail(self):
        print(self.color)
        return super().detail()


class Campus(Rebook):
    def __init__(self, materal, zips, pockets, color):
        super().__init__(materal, zips, pockets, color)


# Objects
bag1 = Campus("ledar", "steel", 2, "blue")
bag2 = BagFactory("polyster", "plastic", 4)
bag1.detail()
bag2.detail()
