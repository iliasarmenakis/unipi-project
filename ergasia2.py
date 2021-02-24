import random 
n=int(input('> '))
y=0
n1=0 
n2=1
nteliko=0
if n<0:
  print('o' , n , 'ος ορος ειναι αρνητικος')
elif n<=2:
 print('o',n, 'ος ορος δεν ειναι πρωτος ')
else:
  for i in range(n-1):
    nteliko = n1 + n2 
    n1 = n2
    n2 = nteliko  
  for i in range(20):
    a=random.randint(0,100000)
    if (a ** nteliko ) % nteliko == (a % nteliko ):
      y=y+1
    else:
      print('o',n, 'ος ορος δεν ειναι πρωτος ')
      break    
  if y==20:
    print('o', n, 'ος ορος ειναι πρωτος')
