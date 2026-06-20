#=========================#    
#      SCORE TRACKER      #
#=========================#

names = ["Jayanth","Vihaan","Atharva","Dheemanth","Yashwanth","Kenisha","Aris Ahad"]
scores = [86,84,79,82,68,95,65]

n = len(scores)
print("SCORE TRACKER (n=",n, "players )===")
for i in range(n):
    print("i +1, ","Name: ",names[i],", Score: ",scores[i], sep="")

print()




# PART 2 #

steps = 1
print("Score at index 0: ", scores[0], "| steps = ", steps, "| Theta(1) - tight bound")
print("This is a constant time operation, so the time complexity is O(1).")
print()

target = "Jayanth"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print("Searching for ", target, " | steps = ", steps, "| Omega(1) - best case lower bound")

target = "Aris Ahad"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break

print("Searching for ", target, " | steps = ", steps, "| O(n) - worst case upper bound")
print()


steps = 0
target_sum = 150
print("Searching for a pair of scores that add up to ", target_sum, ":")
for i in range(n):
    for j in range(i+1, n):
        steps += 1
        if scores[i] + scores[j] == target_sum:
            print("Found a pair: ", scores[i], " + ", scores[j], " = ", target_sum, sep="")
            break
print("Total comparisons :", steps, "| O(n^2) drop constants, keep n^2")
print()

print("Asymptotic Notation Summary:")

print("Theta(1) - index access, always 1 step tight bound")
print("Omega(1) - best case, foun in 1 step, lower bound")
print("O(n) - worst case search,found after n=",n," steps, upper bound")
print("O(n^2) : pair check - n*(n-1)/2 =", n* (n-1) // 2,
"comparisons")
print()
print("Drop constants. Keep the dominant term. That is asymptotic analysis!")