class Bags:
    a = 12  ## class attributes

    def __init__(self, material, zips, pockets):
        # Object/instance attriubutes
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def display(self):  # object/instance method
        print(
            f"Material: {self.material} | Zips: {self.zips} | Pockets: {self.pockets}"
        )


nike = Bags("polyister", "stainless steel", 2)  ## Object
nike.display()
