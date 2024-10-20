for i in range(10):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    for j in range(5):
        print(i, j)

# * 0
# ** 1
# *** 2
# **** 3
# ***** 4

for i in range(1, 6):  # 1, 2, 3, 4, 5
    print("*" * i)


# ***** 4
# **** 3
# *** 2
# ** 1
# * 0

print("=============== Reverse pattern ===============")

for i in range(5, 0, -1):  # 5, 4, 3, 2, 1
    print("*" * i)


# * Assignment

# ***** 0
# ***** 1
# ***** 2
# ***** 3
# ***** 4
