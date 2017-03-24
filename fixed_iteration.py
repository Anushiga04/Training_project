# -*- coding: utf-8 -*-
def func1(y1):
    return (1.+(1/y1))
    
def func2(y2):
    return ((y2*y2*y2)+2)/7.

i=1
x=1
permissable_error = 0.0005

while (i < 100):
    func1_res = func1(x)
    #print "Value of func1:", func1_res
    res = func1(func1_res)
    #print "Value of func1(func_1):", res
    diff = abs(func1_res - res)
    #print "Value of sub", diff
    if diff < permissable_error:
        print("Root for function1:",func1_res)
        break;
    else:
        x=func1_res
    i = i + 1


while (i < 100):
    func2_res = func2(x)
    #print "Value of func2:", func2_res
    res2 = func2(func2_res)
    #print "Value of func2(func_2:)", func2_res
    diff_2 = abs(func2_res - res2)
    #print "Value of diff_2", diff_2
    if diff_2 < permissable_error:
        print("Root for function2:",func2_res)
        break;
    else:
        x = func2_res
    i = i + 1
    



    
    
    

