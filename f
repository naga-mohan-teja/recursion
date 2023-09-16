x=0 
def chr(i,n):
    global x
    if i>n:
        print(x)
        return
    x+=i
    chr(i+1,n)
  
n=int(input())
chr(1,n)
