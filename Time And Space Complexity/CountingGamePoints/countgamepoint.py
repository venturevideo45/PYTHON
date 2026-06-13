n = 4 
print("=== Counting Game Points (n = ", n, "rounds)===")
print()

total = n * (n + 1) // 2
print("Formula way : total=",total, "| steps = 1")

total = 0
steps = 0
for round_num in range(1, n + 1):
    total += round_num
    steps += 1
print("Loop way : total=",total, "| steps =", steps)

total = 0
steps = 0
for round_num in range(1, n + 1):
    for point in range(1, round_num + 1):
        total += 1
        steps += 1
print("Nested loop way : total=",total, "| steps =", steps)


n = 10
nested_steps = 0
for round_num in range(1, n + 1):
    for point in range(1, round_num + 1):
        nested_steps += 1

print()
print("=== Now with n = ", n, "rounds ===")
print("Formula Way : steps = 1 (always 1 step!)")
print("Loop Way : steps =", n, "(grows much faster)")
print("Nested Loop Way : steps =", nested_steps, "(grows much faster than the loop way!)")

print()
print("Same Answer, but very different costs. That is the time complextity")