#Напишете програма, която намира всички прости числа в диапазона от 2 до 50, използвайки вложени цикли. (Едно число е просто, ако се дели само на 1 и на себе си).

#1. Класически алгоритъм с вложени цикли

print("Простите числа от 2 до 50 са:")

for num in range(2, 51):  # Обхождаме числата от 2 до 50
    is_prime = True  # Приемаме, че числото е просто
    for divisor in range(2, int(num ** 0.5) + 1):  # Проверяваме делимост само до √num
        if num % divisor == 0:
            is_prime = False  # Числото не е просто
            break  # Прекратяваме проверката
    if is_prime:
        print(num, end=" ")  # Извеждаме простото число

print("\n")
print("Чрез Решетото на Ератостен:")
#2. Решетото на Ератостен:

n = 50
prime = [True] * (n + 1)  # Създаваме списък от булеви стойности
prime[0] = prime[1] = False  # 0 и 1 не са прости

for p in range(2, int(n ** 0.5) + 1):  # Проверяваме само до √n
    if prime[p]:  # Ако p е просто число
        for multiple in range(p * p, n + 1, p):  # Махаме кратните на p
            prime[multiple] = False

for i in range(2, n + 1):
    if prime[i]:  # Ако числото е просто
        print(i, end=" ")  # Извеждаме простото число


#3. Оптимизирано Решето на Ератостен
#Пропуска всички четни числа освен 2 (намалява паметта наполовина).

def optimized_sieve(n):
    if n < 2:
        return []
    primes = [2]  # Започваме с 2
    sieve = [True] * ((n - 1) // 2)  # Само нечетни числа
    for i in range(1, int(n ** 0.5 / 2) + 1):  # Проверяваме до √n
        if sieve[i]:
            p = 2 * i + 1
            for j in range((p * p - 1) // 2, len(sieve), p):
                sieve[j] = False
    primes.extend([2 * i + 1 for i, is_prime in enumerate(sieve) if is_prime and 2 * i + 1 <= n])
    return primes

#4. Решето на Аткин
#ВНИМАНИЕ!!! По-сложен за разбиране:

def atkin_sieve(limit):
    import math
    primes = [2, 3] if limit >= 3 else [2] if limit == 2 else []
    sieve = [False] * (limit + 1)
    sqrt = int(math.sqrt(limit)) + 1

    for x in range(1, sqrt):
        for y in range(1, sqrt):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and n % 12 in (1, 5):
                sieve[n] ^= True
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True
            if x > y:
                n = 3 * x ** 2 - y ** 2
                if n <= limit and n % 12 == 11:
                    sieve[n] ^= True

    for r in range(5, sqrt):
        if sieve[r]:
            for i in range(r * r, limit + 1, r * r):
                sieve[i] = False

    primes += [i for i in range(5, limit + 1) if sieve[i]]
    return primes

print("\n")
print("Чрез Оптимизирано Решето на Ератостен: ")
print(*optimized_sieve(50))
print()
print("Чрез Решето на Аткин")
print(*atkin_sieve(50))