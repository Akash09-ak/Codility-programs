#Find longest sequence of zeros in binary representation of an integer
def solution(N):
   b=bin(N)
   l=list(b)
   print (b)
   l = l[2:]
   c = 0
   d = 0
   for i in range(0, len(l)):

       if l[i] == '1':
           if(c>d):
               d=c
           c=0

       else:
           c=c+1

   print(d)
   return l

print(solution(32))
#another example
print(solution (79))