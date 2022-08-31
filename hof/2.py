class A:
    def method1(self):
        print('Method of class A is called')

class B(A):
    def method1(self):
        print('method of class B is called')

class C(B,A):
    def method1(self):
        print('method of class C is called')
        

d = C()

print(d.method1())
print(A.method1(d))