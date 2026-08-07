# Question no 1:Reverse a list without using reverse().
l1 = [9,8,7,6,5,4,3,2,1]

reverse_list = l1[::-1] #[1,2,3,4,5,6,7,8,9]
print(reverse_list)
# Explanation :
"""
What is [::-1] in Python?

It's called slicing.
General format:
list[start : end : step]

🔹 Now your case: [::-1]
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])

👉 Output:

[5, 4, 3, 2, 1]
🔍 Breakdown of [::-1]
Part	Meaning
start	empty → start from beginning
end	    empty → go till end
step    = -1	go backwards
🔹 Why it reverses?

Normally Python moves:

→ 1 → 2 → 3 → 4 → 5

With -1 step:

← 5 ← 4 ← 3 ← 2 ← 1
"""
# Question no 2:Remove duplicates from a list.

l2 = [1,2,32,4,23,5,2,5,3,6,5,6,8,9]
remove_duplicate = list(set(l2))
print(remove_duplicate)

# Question no 3:Find the second largest number in a list.

num = [1,4,67,45,78,35,67,2,98,9,90,99]

sec_largest = list(set(num))
sec_largest.sort()

print(sec_largest[-2])