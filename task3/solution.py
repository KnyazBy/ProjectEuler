"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?

"""
n = 600851475143
a = 1
while n!=1:
    a+=1
    if n%a==0:
        n/=a

print(a)