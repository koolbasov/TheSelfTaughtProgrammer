# Также можно использовать встроенный модуль statistics, чтобы подсчи-
#тать среднее значение, медиану и моду в итерируемом объекте, состоящем из
# чисел.

import statistics

nums = [1, 5, 33, 12, 46, 33, 2]

# среднее
print(statistics.mean(nums))

# медиана
print(statistics.median(nums))

# мода
print(statistics.mode(nums))
