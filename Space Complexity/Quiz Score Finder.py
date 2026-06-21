scores = [12, 25, 33, 41, 50, 67, 72, 85, 91, 98]
n, target = len(scores), 98
print("=== Quiz Score Finder(n =", n, "scores) ===")
print("Scores:", scores, "Target:", target)
print()

steps = 0 
for i in range(n):
    steps += 1
    if scores[i] == target:
        print("Linear Search :  index =", i," | steps =", steps, "| O(n)")
        break
print()

lo, hi, steps = 0, n - 1, 0
while lo <= hi:
    mid = (lo + hi) // 2
    steps += 1
    if scores[mid] == target:
        print("Binary Search : index =", mid," | steps =", steps, "| O(log n)")
        break
    elif scores[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1

print()

def binary_search_recursive(scores, target, lo, hi, steps=0):
    if lo > hi:
        return -1, steps
    mid = (lo + hi) // 2
    steps += 1
    if scores[mid] == target:
        return mid, steps
    elif scores[mid] < target:
        return binary_search_recursive(scores, target, mid + 1, hi, steps)
    else:
        return binary_search_recursive(scores, target, lo, mid - 1, steps)
    
result, steps = binary_search_recursive(scores, target, 0, n - 1)
print("Binary Search (Recursive) : index =", result," | steps =", steps, "| O(log n)")
print()

print("=== Space and Complexity Summary ===")
print("Iterative : O(1) space - only lo, hi, mid")
print("Recursive: O(log n) space-", steps, "stack frames for n =", n)
print()

print("Complexity ladder (n =", n, "):")
print("O(1) :", 1, "step - constant, does not grow with n")
print("O(log n):", steps, "steps - halving, grows slowly")
print("O(n) :", n, "steps - linear, grows with n")
print("O(n^2) :", n*n, "steps quadratic, grows fast!")