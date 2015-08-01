from __future__ import print_function

# to print a tree
print("   *")
print("  ***")
print(" *****")
print("*******")


# 1
print(" " * 3 + "*")
print(" " * 2 + "*" * 3)
print(" " * 1 + "*" * 5)
print(" " * 0 + "*" * 7)


# 2
print(("*" * 1).center(10))
print(("*" * 3).center(10))
print(("*" * 5).center(10))
print(("*" * 7).center(10))


# Use Loop in future example

# 3.0

name = 'Tim'
print("Hi " + name + "How do you do")


name = "Tim"
print( "Hi {}, How do you do".format(name)  )


# 3.3 multiline

letter = """
  Hi {}

    We Will go to your yard to eat your brain

             Zombie
"""


print(letter.format('Martin'))


