import matplotlib.pyplot as plt
import math

n = list(range(1, 50))

o_1 = [x * 0.5 for x in n]                 # масштабируем
o_log_n = [math.log2(x) * 2 for x in n]
o_n = [x for x in n]
o_nlogn = [x * math.log2(x) for x in n]
o_n2 = [x**2 / 10 for x in n]              # уменьшаем
o_2n = [2**x / 1000 for x in range(1, 15)] # ограничиваем

plt.plot(n, o_1, label="O(1)")
plt.plot(n, o_log_n, label="O(log n)")
plt.plot(n, o_n, label="O(n)")
plt.plot(n, o_nlogn, label="O(n log n)")
plt.plot(n, o_n2, label="O(n²)")
plt.plot(range(1, 15), o_2n, label="O(2ⁿ)")

plt.xlabel("Размер входных данных (n)")
plt.ylabel("Рост функции")
plt.title("Рост алгоритмов Big-O")
plt.legend()
plt.grid(True)

plt.show()
