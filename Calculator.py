#!/usr/bin/env python
# coding: utf-8

# In[4]:


import unittest
import math
import statistics as st
from itertools import permutations as per
from itertools import combinations as comb
from functools import reduce
import sys

def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b

def mul(a,b):
    return a*b
    
def div(a,b):
    return a/b
    
def idiv(a,b):
    return a//b
    
def mod(a,b):
    return a%b
    
def power(a,b):
    return pow(a,b)

def nroot(a,b):
    s=(1/b)
    return (a**s)
    
def fact(a):
    if(a==1 or a==0):
        return 1
    else:
        return a*fact(a-1)

def prime(n):
    k=1
    if(n<=0):
        print("Enter positive number")
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                k=0
                break
        if k==1:
            print("{} is a prime number".format(n))
        else:
            print("{} is not a prime number".format(n))
def MatAdd():
    n=int(input("Enter the row size of  matrix : "))
    m=int(input("Enter the col size of  matrix : "))
    l1=[]
    for i in range(n):
        l=[]
        for j in range(m):
            l.append(int(input("Enter the 1st matrix number : ")))
        l1.append(l)
    l2=[]
    for i in range(n):
        l=[]
        for j in range(m):
            l.append(int(input("Enter the 2nd matrixnumber : ")))
        l2.append(l)
    r=[]
    for i in range(n):
        l=[]
        for j in range(m):
            l.append(l1[i][j]+l2[i][j])
        r.append(l)
    for i in range(n):
        print(r[i])
        
def MatSub():
    n=int(input("Enter the row size of  matrix : "))
    m=int(input("Enter the col size of  matrix : "))
    l1=[]
    for i in range(n):
        l=[]
        for j in range(m):
            l.append(int(input("Enter the 1st number : ")))
        l1.append(l)
    l2=[]
    for i in range(n):
        l=[]
        for j in range(m):
            l.append(int(input("Enter the 2nd number : ")))
        l2.append(l)
    r=[]
    for i in range(n):
        l=[]
        for j in range(m):
            l.append(l1[i][j]-l2[i][j])
        r.append(l)
    for i in range(n):
        print(r[i])
        
def MatMul():
    n1=int(input("Enter the row size of 1st matrix : "))
    m1=int(input("Enter the col size of 1st matrix : "))
    l1=[]
    for i in range(n1):
        l=[]
        for j in range(m1):
            l.append(int(input("Enter the number : ")))
        l1.append(l)
    n2=int(input("Enter the row size of 2st matrix : "))
    m2=int(input("Enter the col size of 2st matrix : "))
    l2=[]
    for i in range(n2):
        l=[]
        for j in range(m2):
            l.append(int(input("Enter the number : ")))
        l2.append(l)
    try:
        if(m1!=n2):
            raise ValueError("Error: Enter the correct dimensions of matrixes")
        r=[]
        for i in range(n1):
            l=[]
            for j in range(m2):
                a=0
                for k in range(n2):
                    a+=(l1[i][k]*l2[k][j])
                l.append(a)
            r.append(l)
        for i in range(n1):
            print(r[i])
    except ValueError as e:
        print(e)
    
def var(l):
    print("Square of elements are : ",list(map(lambda x:x**2,l)))
    print("Cube of elements are : ",list(map(lambda x:x**3,l)))
    print("Sum of elements : ",reduce(lambda x,y:x+y,l))
    print("Mean of elements : ",st.mean(l))
    print("Median of elements : ",st.median(l))
    if(len(set(l))!=len(l)):
        print("Mode of elements : ",st.mode(l))
    else:
        print("All are unique elements")
    print("Variance of elements : ",st.variance(l))
    print("Standard Deviation of elements : ",st.pstdev(l))

    
def permutation(l,r):
    p=per(l,r)
    print("The permutations of size {} are ".format(int(r)))
    for i in p:
        print(i)
        
def combination(l,r):
    c=comb(l,r)
    print("The combinations of size {} are".format(int(r)))
    for i in c:
        print(i)
    
def trig(a):
    print("Sine of {} is {}".format(a,math.sin(a)))
    print("Cosine of {} is {}".format(a,math.cos(a)))
    print("Tangent of {} is {}".format(a,math.tan(a)))

def log(a,b):
    print("The logarithm base {} of {} is {}".format(b,a,math.log(a,b)))

while(True):
    print("The available operations are :")
    print("1-Arithmetic Expression\n2-Addition\n3-substraction\n4-Multiplication\n5-Division\n6-Integer Division\n7-Modulus\n8-Power\n9-Nth root\n10-Factorial\n11-Prime Number\n12-Matrix Addition\n13-Matrix Substraction\n14-Matrix Multiplication\n15-Varaince\n16-Permutation\n17-combination\n18-Trigometric\n19- Log ")
    c=input('Enter the operation : ')
    a,b=0,0
    l=[]
    if (c=='10' or c=='11'):
        a=int(input("Enter the positive number : "))
    elif c=='1':
        a=input("Enter the expression : ")
    elif(c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8'):
        a=float(input("Enter the first number : "))
        b=float(input("Enter the second number : "))
    elif(c=='15'):
        a=int(input("Enter the number of elements : "))
        for x in range(a):
            l.append(int(input("Enter the {} element : ".format(x+1))))
    elif(c=='16' or c=='17'):
        a=int(input("Enter the number of elements : "))
        for x in range(a):
            l.append(int(input("Enter the {} element : ".format(x+1))))
        b=int(input("Enter the length"))
        
    if c=='1':
        try:
            if(a==''):
                raise ValueError("Enter valid expression.")
            else:
                r=eval(a)
                print(r)
        except ValueError as e:
            print(e)
        except:
            print("Oops", sys.exc_info(), "occured")
            
    elif c=='2':
        r=add(a,b)
        print("{} + {} = {}".format(a,b,r))
    elif c=='3':
        r=sub(a,b)
        print("{} - {} = {}".format(a,b,r))
    elif c=='4':
        r=mul(a,b)
        print("{} * {} = {}".format(a,b,r))
    elif c=='5':
        try:
            if(b==0):
                raise ValueError("Enter value other than 0")
            r=div(a,b)
            print("{} / {} = {}".format(a,b,r))
        except ValueError as e:
            print(e)
    elif c=='6':
        try:
            if(b==0):
                raise ValueError("Enter value other than 0")
            r=idiv(a,b)
            print("{} // {} = {}".format(a,b,r))
        except ValueError as e:
            print(e)
    elif c=='7':
        r=mod(a,b)
        print("{} % {} = {}".format(a,b,r))
    elif c=='8':
        r=power(a,b)
        print("{} ^ {} = {}".format(a,b,r))
    elif c=='9':
        a=int(input("Enter the value : "))
        b=int(input("Enter the root value : "))
        try:
            if(b==0):
                raise ValueError("Enter the valid value ")
            r=nroot(a,b)
            print("{}th root of {} is {}".format(b,a,r))
        except ValueError as e:
            print(e)
    elif c=='10':
        try:
            if a<0:
                raise MemoryError("Error: Enter the positive number")
            print(fact(a))
        except MemoryError as m:
            print(m)
    elif c=='11':
        if(a==1):
            print("{} neither prime nor composite")
        else:
            prime(a)
    elif c=='12':
        MatAdd()
    elif c=='13':
        MatSub()
    elif c=='14':
        MatMul()
    elif c=='15':
        var(l)
    elif c=='16':
        try:
            if b>a:
                raise MemoryError("Error: size should be less than the list length")
            permutation(l,b)
        except MemoryError as e:
            print(e)
    elif c=='17':
        try:
            if b>a:
                raise MemoryError("Error: size should be less than the list length")
            combination(l,b)
        except MemoryError as e:
            print(e)
    elif c=='18':
        a=int(input("Enter the value : "))
        trig(a)
    elif c=='19':
        a=int(input("Enter the value : "))
        b=int(input("Enter the base value : "))
        log(a,b)
    else:
        print("Enter the valid operation")
    try:
        q=str(input('Do you want to continue : y/n'))
        if(q!='y' and q!='n'):
            raise ValueError("Error: Enter Valid operation")
    except ValueError as e:
        print(e)
    finally:
        if(q!='y'):
            break

class TestingSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add(2,3),5,"It should be 5")
    def test_sub(self):
        self.assertEqual(sub(4,2),2,"It should be 2")
    def test_mul(self):
        self.assertEqual(mul(2,3),6,"It should be 6")
    def test_div(self):
        self.assertEqual(div(9,3),3,"It should be 3")
    def test_idiv(self):
        self.assertEqual(idiv(10,3),3,"It should be 3")
    def test_mod(self):
        self.assertEqual(mod(10,2),0,"It should be 0")
    def test_mod(self):
        self.assertEqual(power(2,4),16,"It should be 16")
    def test_root(self):
        self.assertEqual(nroot(16,4),2,"It should be 2")
    def test_fact(self):
        self.assertEqual(fact(5),120,"It should be 120")
        
        
if __name__=='__main__':
    unittest.main()


# # 

'''O/P:
The available operations are :
0-Arithmetic Expression
1-Addition
2-substraction
3-Multiplication
4-Division
5-Integer Division
6-Modulus
7-Power
8-Factorial
9-Matrix Addition
10-Matrix Substraction
11-Matrix Multiplication
12-Varaince
13-Permutation
14-combination 
Enter the operation : 0
Enter the expression : 2*3/5
1.2
Do you want to continue : y/ny
The available operations are :
0-Arithmetic Expression
1-Addition
2-substraction
3-Multiplication
4-Division
5-Integer Division
6-Modulus
7-Power
8-Factorial
9-Matrix Addition
10-Matrix Substraction
11-Matrix Multiplication
12-Varaince
13-Permutation
14-combination 
Enter the operation : 1
Enter the first number : 456
Enter the second number : 75378
456.0 + 75378.0 = 75834.0
Do you want to continue : y/ny
The available operations are :
0-Arithmetic Expression
1-Addition
2-substraction
3-Multiplication
4-Division
5-Integer Division
6-Modulus
7-Power
8-Factorial
9-Matrix Addition
10-Matrix Substraction
11-Matrix Multiplication
12-Varaince
13-Permutation
14-combination 
Enter the operation : 2
Enter the first number : 76
Enter the second number : 345567
76.0 - 345567.0 = -345491.0
Do you want to continue : y/ny
The available operations are :
0-Arithmetic Expression
1-Addition
2-substraction
3-Multiplication
4-Division
5-Integer Division
6-Modulus
7-Power
8-Factorial
9-Matrix Addition
10-Matrix Substraction
11-Matrix Multiplication
12-Varaince
13-Permutation
14-combination 
Enter the operation : 7
Enter the first number : -5
Enter the second number : -2
-5.0 ^ -2.0 = 0.04
Do you want to continue : y/ny
The available operations are :
0-Arithmetic Expression
1-Addition
2-substraction
3-Multiplication
4-Division
5-Integer Division
6-Modulus
7-Power
8-Factorial
9-Matrix Addition
10-Matrix Substraction
11-Matrix Multiplication
12-Varaince
13-Permutation
14-combination 
Enter the operation : 8
Enter the positive number : 20
2432902008176640000
Do you want to continue : y/ny
The available operations are :
0-Arithmetic Expression
1-Addition
2-substraction
3-Multiplication
4-Division
5-Integer Division
6-Modulus
7-Power
8-Factorial
9-Matrix Addition
10-Matrix Substraction
11-Matrix Multiplication
12-Varaince
13-Permutation
14-combination 
Enter the operation : 10
Enter the row size of  matrix : 2
Enter the col size of  matrix : 2
Enter the 1st number : 1
Enter the 1st number : 2
Enter the 1st number : 3
Enter the 1st number : 4
Enter the 2nd number : 4
Enter the 2nd number : 5
Enter the 2nd number : 6
Enter the 2nd number : 7
[-3, -3]
[-3, -3]
Do you want to continue : y/ny
The available operations are :
0-Arithmetic Expression
1-Addition
2-substraction
3-Multiplication
4-Division
5-Integer Division
6-Modulus
7-Power
8-Factorial
9-Matrix Addition
10-Matrix Substraction
11-Matrix Multiplication
12-Varaince
13-Permutation
14-combination 
Enter the operation : 11
Enter the row size of 1st matrix : 2
Enter the col size of 1st matrix : 2
Enter the number : 1
Enter the number : 2
Enter the number : 3
Enter the number : 4
Enter the row size of 2st matrix : 2
Enter the col size of 2st matrix : 2
Enter the number : 6
Enter the number : 5
Enter the number : 4
Enter the number : 7
[14, 19]
[34, 43]
Do you want to continue : y/ny
The available operations are :
1-Addition
2-substraction
3-Multiplication
4-Division
5-Integer Division
6-Modulus
7-Power
8-Factorial
9-Matrix Addition
10-Matrix Substraction
11-Matrix Multiplication
12-Varaince
13-Permutation
14-combination 
Enter the operation : 12
Enter the number of elements : 6
Enter the 1 element : 1
Enter the 2 element : 2
Enter the 3 element : 3
Enter the 4 element : 4
Enter the 5 element : 5
Enter the 6 element : 6
Sum of elements :  21
Mean of elements :  3.5
Variance of elements :  3.5
Standard Deviation of elements :  1.707825127659933
Do you want to continue : y/ny
The available operations are :
1-Addition
2-substraction
3-Multiplication
4-Division
5-Integer Division
6-Modulus
7-Power
8-Factorial
9-Matrix Addition
10-Matrix Substraction
11-Matrix Multiplication
12-Varaince
13-Permutation
14-combination 
Enter the operation : 13
Enter the number of elements : 3
Enter the 1 element : 1
Enter the 2 element : 2
Enter the 3 element : 3
Enter the length1
The permutations of size 1 are 
(1,)
(2,)
(3,)
Do you want to continue : y/ny
The available operations are :
1-Addition
2-substraction
3-Multiplication
4-Division
5-Integer Division
6-Modulus
7-Power
8-Factorial
9-Matrix Addition
10-Matrix Substraction
11-Matrix Multiplication
12-Varaince
13-Permutation
14-combination 
Enter the operation : 3
Enter the first number : 1
Enter the second number : 2
1.0 * 2.0 = 2.0
Do you want to continue : y/ny
The available operations are :
1-Addition
2-substraction
3-Multiplication
4-Division
5-Integer Division
6-Modulus
7-Power
8-Factorial
9-Matrix Addition
10-Matrix Substraction
11-Matrix Multiplication
12-Varaince
13-Permutation
14-combination 
Enter the operation : 14
Enter the number of elements : 3
Enter the 1 element : 1
Enter the 2 element : 2
Enter the 3 element : 3
Enter the length2
The combinations of size 2 are
(1, 2)
(1, 3)
(2, 3)
Do you want to continue : y/nn'''

