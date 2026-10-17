class A:
    def process(self):
        print("Processing A")


class B(A):
    def process(self):
        print("Processing B")
        super().process()


class C(A):
    def process(self):
        print("Processing C")
        super().process()


class D(B, C):
    def process(self):
        print("Processing D")
        super().process()


obj = D()
obj.process()
