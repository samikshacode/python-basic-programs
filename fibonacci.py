def fibonacci(n):
 
   [a,b]=[0,1]

   print(a,b,end=' ')

   for i in range(2, n):
    next_term=a+b

    print(next_term,end=' ')

    a,b=b,next_term


n=int(input("Enter the number of terms:"))

fibonacci(n)
