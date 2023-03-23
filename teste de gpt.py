# Código

# Fibonacci Sequence
# o primeiro número da sequencia é 0
# o segundo número da sequencia é 1
n1 = 0
n2 = 1
count = 0
nterms = int(input('informe o numero de termos: '))
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence com",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence com",nterms,":")
   while count < nterms:
       print(n1,end=' → ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1