# ########################################
# # Arithmetic Operators
# a = 10
# b = 3

# # Addition
# addition = a + b
# print("Addition:", addition)

# # Subtraction
# subtraction = a - b
# print("Subtraction:", subtraction)

# # Multiplication
# multiplication = a * b
# print("Multiplication:", multiplication)

# # Division (returns a float)
# division = a / b
# print("Division:", division)

# # Floor Division (returns an integer)
# floor_division = a // b
# print("Floor Division:", floor_division)

# # Modulus (remainder of division)
# modulus = a % b
# print("Modulus:", modulus)

# # Exponentiation
# exponentiation = a ** b
# print("Exponentiation:", exponentiation)




# ########################################
# # Initialize variables
# x = 10
# y = 5

# # Assignment: =
# a = x
# print("a:", a)  # Output: 10

# # Addition Assignment: +=
# x += y                          # x = x + y
# print("x after addition:", x)  # Output: 15

# # Subtraction Assignment: -=
# x -= y
# print("x after subtraction:", x)  # Output: 10

# # Multiplication Assignment: *=
# x *= y
# print("x after multiplication:", x)  # Output: 50

# # Division Assignment: /=
# x /= y
# print("x after division:", x)  # Output: 10.0

# # Modulus Assignment: %=
# x %= y
# print("x after modulus:", x)  # Output: 0.0

# # Exponentiation Assignment: **=
# x = 2
# y = 3
# x **= y
# print("x after exponentiation:", x)  # Output: 8

# # Floor Division Assignment: //=
# x = 17
# y = 3
# x //= y
# print("x after floor division:", x)  # Output: 5


# ########################################
# # Comparison operators

# # Initialize variables
# x = 10
# y = 5

# # Equal to: ==
# is_equal = x == y
# print("x is equal to y:", is_equal)  # Output: False

# # Not equal to: !=
# is_not_equal = x != y
# print("x is not equal to y:", is_not_equal)  # Output: True

# # Greater than: >
# is_greater_than = x > y
# print("x is greater than y:", is_greater_than)  # Output: True

# # Less than: <
# is_less_than = x < y
# print("x is less than y:", is_less_than)  # Output: False

# # Greater than or equal to: >=
# is_greater_equal = x >= y
# print("x is greater than or equal to y:", is_greater_equal)  # Output: True

# # Less than or equal to: <=
# is_less_equal = x <= y
# print("x is less than or equal to y:", is_less_equal)  # Output: False

# ########################################
# # Logical operators

# # Initialize variables
# p = True
# q = False

# # Logical AND: and
# logical_and = p and q
# print("Logical AND:", logical_and)  # Output: False

# # Logical OR: or
# logical_or = p or q
# print("Logical OR:", logical_or)  # Output: True

# # Logical NOT: not
# logical_not_p = not p
# logical_not_q = not q
# print("Logical NOT p:", logical_not_p)  # Output: False
# print("Logical NOT q:", logical_not_q)  # Output: True


# ########################################
# # Identity operators

# # Initialize variables
# x = [1, 2, 3]
# y = x  # y refers to the same object as x
# z = [1, 2, 3]  # z is a different object with the same content as x

# # Identity check using is
# is_x_same_as_y = x is y
# is_x_same_as_z = x is z

# # Identity check using is not
# is_x_not_same_as_z = x is not z

# print("is_x_same_as_y:", is_x_same_as_y)  # Output: True
# print("is_x_same_as_z:", is_x_same_as_z)  # Output: False
# print("is_x_not_same_as_z:", is_x_not_same_as_z)  # Output: True


# ##########################################
# # Membership operators

# # Initialize a list of fruits
# fruits = ["apple", "banana", "orange", "grape", "kiwi"]

# # Membership check using in
# is_banana_in_fruits = "banana" in fruits
# is_mango_in_fruits = "mango" in fruits

# # Membership check using not in
# is_cherry_not_in_fruits = "cherry" not in fruits
# is_grape_not_in_fruits = "grape" not in fruits

# print("is_banana_in_fruits:", is_banana_in_fruits)  # Output: True
# print("is_mango_in_fruits:", is_mango_in_fruits)  # Output: False
# print("is_cherry_not_in_fruits:", is_cherry_not_in_fruits)  # Output: True
# print("is_grape_not_in_fruits:", is_grape_not_in_fruits)  # Output: False


# ##########################################
# # Bitwise operators

# # Initialize variables
# x = 10   # Binary: 1010
# y = 6    # Binary: 0110

# # Bitwise AND: &
# bitwise_and = x & y   # Binary: 0010 (2 in decimal)

# # Bitwise OR: |
# bitwise_or = x | y    # Binary: 1110 (14 in decimal)

# # Bitwise XOR: ^
# bitwise_xor = x ^ y   # Binary: 1100 (12 in decimal)

# # Bitwise NOT: ~
# bitwise_not_x = ~x    # Binary: 11111111111111111111111111110101 (-11 in decimal)

# # Bitwise Left Shift: <<
# bitwise_left_shift = x << 2   # Binary: 101000 (40 in decimal)

# # Bitwise Right Shift: >>
# bitwise_right_shift = x >> 1  # Binary: 101 (5 in decimal)

# print("Bitwise AND:", bitwise_and)           # Output: 2
# print("Bitwise OR:", bitwise_or)             # Output: 14
# print("Bitwise XOR:", bitwise_xor)           # Output: 12
# print("Bitwise NOT x:", bitwise_not_x)       # Output: -11
# print("Bitwise Left Shift:", bitwise_left_shift)     # Output: 40
# print("Bitwise Right Shift:", bitwise_right_shift)   # Output: 5


##########################################
# Operators precedence

# Initialize variables
a = 10
b = 5
c = 3

# Operators precedence: *, +, and -
result = a + b * c
print("a + b * c:", result)  # Output: 25

# Parentheses can change the order of operations
result_with_parentheses = (a + b) * c
print("(a + b) * c:", result_with_parentheses)  # Output: 45

# Operators precedence: **, *, and /
result_exponentiation = a * b ** c
print("a * b ** c:", result_exponentiation)  # Output: 1250

# Operators precedence: /, //, and %
result_division = a // b / c
print("a // b / c:", result_division)  # Output: 0.6666666666666666

