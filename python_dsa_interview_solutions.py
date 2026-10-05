# 1. FizzBuzz Challenge
# Iterate from 1 to 50.

def fizz_buzz(n=50):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# 2. Leap Year Logic

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# 3. Identity vs Equality
# == compares values.
# is checks whether two variables refer to the same object.

def identity_vs_equality():
    L1 = [1, 2, 3]
    L2 = [1, 2, 3]

    print(f"L1 == L2 (Value Equality): {L1 == L2}")
    print(f"L1 is L2 (Object Identity): {L1 is L2}")


# 4. Bitwise Swap (Advanced)
# Swap two numbers using XOR without a third variable.

def bitwise_swap(a: int, b: int):
    print(f"Before swap: a = {a}, b = {b}")

    a = a ^ b
    b = a ^ b
    a = a ^ b

    print(f"After swap:  a = {a}, b = {b}")

    return a, b


# 5. Prime Number Finder
# Find the first 10 prime numbers using a while loop.

def find_first_n_primes(n=10):
    primes = []
    num = 2

    while len(primes) < n:
        is_prime = True

        for p in primes:
            if p * p > num:
                break

            if num % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

        num += 1

    return primes


# 6. The Loop Breaker
# 1 to 20:
# - Divisible by 4 -> pass
# - 13 -> continue
# - 18 -> break

def loop_breaker():
    for i in range(1, 21):

        if i == 18:
            break

        if i % 4 == 0:
            pass
        elif i == 13:
            continue

        print(i, end=" ")

    print()


# 7. Nested Conditionals
# A: 90+
# B: 80-89
# C: 70-79
# Fail: Below 70

def get_grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "Fail"


# 8. Reverse an Integer
# Reverse digits using // and %.

def reverse_integer(n: int) -> int:
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return reversed_num


# 9. Runner-Up Score
# Find the second-highest DISTINCT score without sorting.

def get_runner_up(scores):
    first = float("-inf")
    second = float("-inf")

    for score in scores:
        if score > first:
            second = first
            first = score

        elif first > score > second:
            second = score

    if second == float("-inf"):
        return None

    return second


# 10. Duplicate Removal
# dict.fromkeys() preserves the original order.

def remove_duplicates(arr):
    return list(dict.fromkeys(arr))


# 11. List Intersection
# Find common elements using the membership operator "in".

def list_intersection(list1, list2):
    return [item for item in list1 if item in list2]


# 12. Tuple Immutability Test
# Attempt to change the second element of a tuple.

def test_tuple_immutability():
    my_tuple = (1, 2, 3)

    try:
        my_tuple[1] = 10

    except TypeError as e:
        print(f"Caught expected TypeError: {e}")

# 13. Character Frequency Counter
# Count how many times each character appears.

def char_frequency(s: str):
    frequency = {}

    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency


# 14. List Comprehension
# Squares of all even numbers from 1 to 20.

def even_squares():
    return [x ** 2 for x in range(1, 21) if x % 2 == 0]


# 15. Dictionary Comprehension
# Keep only dictionary items whose values are greater than 2.

def filter_dict():
    original = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }

    return {key: value for key, value in original.items() if value > 2}


# TEST ALL SOLUTIONS

if __name__ == "__main__":

    print("==========================================")
    print("PYTHON DSA INTERVIEW SOLUTIONS")
    print("==========================================")

    print("\n1. FizzBuzz:")
    fizz_buzz()

    print("\n2. Leap Year:")
    print(is_leap_year(2024))

    print("\n3. Identity vs Equality:")
    identity_vs_equality()

    print("\n4. Bitwise Swap:")
    bitwise_swap(10, 20)

    print("\n5. First 10 Prime Numbers:")
    print(find_first_n_primes(10))

    print("\n6. Loop Breaker:")
    loop_breaker()

    print("\n7. Grade:")
    print(get_grade(85))

    print("\n8. Reverse Integer:")
    print(reverse_integer(12345))

    print("\n9. Runner-Up Score:")
    print(get_runner_up([10, 20, 4, 45, 99, 99]))

    print("\n10. Remove Duplicates:")
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

    print("\n11. List Intersection:")
    print(list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))

    print("\n12. Tuple Immutability:")
    test_tuple_immutability()

    print("\n13. Character Frequency:")
    print(char_frequency("hello"))

    print("\n14. Even Squares:")
    print(even_squares())

    print("\n15. Dictionary Comprehension:")
    print(filter_dict())

    print("\n==========================================")
    print("All 15 solutions executed successfully!")
    print("==========================================")