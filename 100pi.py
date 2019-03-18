"""
Run the algorithm below using CPython, Cython, PyPy and Numba and compare 
their performance.

(This is implementing a spigot algorithm by A. Sale, 
D. Saada, S. Rabinowitz, mentioned on
http://mail.python.org/pipermail/edu-sig/2012-December/010721.html).
"""

def pi_digits(n):
    "Generate n digits of Pi."
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while n > 0:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
        d, d1 = a / b, a1 / b1
        while d == d1 and n > 0:
            yield int(d)
            n -= 1
            a, a1 = 10 * (a % b), 10 * (a1 % b1)
            d, d1 = a / b, a1 / b1

phi = list(pi_digits(100))
print(phi)
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]