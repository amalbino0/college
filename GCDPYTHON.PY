A=int(input("enter a number:"))
B=int(input("enter a number:"))
r=1   
if A<B:
    A,B=B,A
if(A==0):
    print("gcd(",A,",",B,")=",B)
elif(B==0):
    print("gcd(",A,",",B,")=",A)
else:
    while(r!=0):
        r=A%B
        A,B=B,r
        print("gcd(",A,",",B,")=",A)
    
  

    
