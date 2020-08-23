tuple1 = (1,2,3,4,5)
tuple2 = ('a','b','c')
tuple3 = (1,'a','abc',[1,2,3,4,5],['a','b','c'])
#tuple[0] = 6           #error

def myFunc():
    print('hi')

tuple4 = (1,2,myFunc)
tuple4[2]()
