"""s
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

"""

def compute():
    ans = max(i*j
    for i in range(100, 1000)
    for j in range(100, 1000)
    if str(i*j)==str(i*j)[::-1])
    return str(ans)

if __name__ == '__main__':
    print(compute())