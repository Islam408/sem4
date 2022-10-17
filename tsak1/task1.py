# Число  Фибоначчи чернез с помощью лямбда-функции
from functools import reduce



print('**'*30)
x = int(input('Введите число: '))
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
								range(n-2), [0, 1])

fib2 = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
								range(n-2), [0, -1])

print(fib2(x))
print(fib(x))

