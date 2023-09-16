#########################################################################################
#print 1 to n numbers using recursion
x=0 
def chr(i,n):
    if i>n:
        return
    print(i)
    chr(i+1,n)
n=int(input())
chr(1,n)
####$########################
#input = 5
#output 
1
2
3
4
5

##########################################################################################
#print n to 1 numbers using recursion
x=0 
def chr(i,n):
    if i<1:
        return
    print(i)
    chr(i-1,n)
n=int(input())
chr(n,n)
####$########################
#input = 5
#output 
5
4
3
2
1
##########################################################################################
#print 1 to n numbers without using i+1 using recursion
#just write print statement after fuction call
x=0 
def chr(i,n):
    if i<1:
        return
    chr(i-1,n)
    print(i)
n=int(input())
chr(n,n)
####$########################
#input = 5
#output 
1
2
3
4
5
##########################################################################################
#print n to 1 numbers without using i-1 using recursion
#just write print statement after fuction call
def chr(i,n):
    if i>n:
        return
    chr(i+1,n)
    print(i)
  
n=int(input())
chr(1,n)
####$########################
#input = 5
#output 
5
4
3
2
1
##########################################################################################
