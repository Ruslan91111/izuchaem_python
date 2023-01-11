x = 1
def nester():
    print(x)
    class C:
        print(x)
        def method1(self):
            print(x)
        def method2(self):
            x = 3
            print(x)
    I = C()
    I.method1()
    I.method2()
print(x)
nester()
print('-'*40)
