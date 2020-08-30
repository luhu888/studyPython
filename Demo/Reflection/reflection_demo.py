class Reflection:
    name = 'luhu'
    @classmethod
    def func1(cls):
        print('in func1')
    def func2(self):
        print('in fnc2')
if hasattr(Reflection, 'func1'):
    print(getattr(Reflection, 'func1'))
if hasattr(Reflection, 'name'):
    print(getattr(Reflection, 'name'))




