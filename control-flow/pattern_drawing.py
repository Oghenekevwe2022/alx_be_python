# i=0
# size = int(input("Enter the size of the pattern:"))
# while i < size:
#     for j in range(i + 1):
#         print("*", end="")
#     print()
#     i += 1

pattern_size = int(input("Enter the size of the pattern: "))

i = 0
while i <= pattern_size:
    for j in range(pattern_size):
        print("*", end="")
    print("\n")
    i += 1