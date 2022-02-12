# write a program to print the sun from 1 to n
n=int(input('Enter the value of n:'))
sum=0
for i in range(1,n+1):
    sum=sum+i
print('total sum from 1 to {} is {}'.format(n,sum))