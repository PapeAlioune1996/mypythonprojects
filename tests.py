class A:
    def func(self):
        pass


class B:
    def func(self, number):
        pass


elements = [A(), B()]
B.func()