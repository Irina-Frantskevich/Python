# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# n = int(input("Введите число: "))
# i = 2
# result = 1
# while i <= n:
#     result *= i # result = result * i
#     i += 1
# print(f'{n}! = {result}')

# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# n = int(input("Введите число: "))
# a0 = 0
# a1 = 1
# a2 = 0
# i = 2
# while a2 < n:
#     a2 = a1 + a0 # Для того чтобы найти 3-ое число, мы складываем 1-ое и 2-ое
#     a0 = a1 # Для того чтобы найти 4-ое число, мы складываем 2-ое и 3-е
#     a1 = a2
#     i += 1
#     if a2 > n:
#         i = -1
# if i == -1:
#     print(i)
# else:
#     print(i)



# for (int i = 0; i <= 10; i++)

for i in 1, True, "Hello", 4.57:
    print(i)

# range()
print(list(range(5)))
for i in [0, 1, 2, 3, 4]:
    print(i)

begin = 10
end = 0
step = -1
print(list(range(begin, end, step)))
print(list(range(5))) # begin = 0           step = +1
print(list(range(10, 20)))