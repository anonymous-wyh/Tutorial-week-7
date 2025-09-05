phrase = input("Enter a phrase: ")
num = 0

for ch in phrase:
    if ch.lower() in "aeiou":  # 转小写，避免大小写问题
        num += 1

print("Number of vowels:", num)

##phrase = input()
##num = 0
##for i in (len(phrase)-1, -1):
##    if phrase[i] == 'a' | 'i' | 'e' | 'o' | 'u':
##        ++i
##print(i)


##i = 10
##while i <= 30:
##    f = (9/5*i)+32
##    print(int(f))
##    i = i + 5


##L = ["sentence", "contains", "five", "words."]
##L.insert(0, "This")
##print(" ".join(L))
##
##del L[3]
##L.insert(3, "six")
##L.insert(4, "different")
##print(" ".join(L))

##num = 5
##for i in range(num, 2*num - 2):
##    print(i)
##
##print("\n")
##
##num = 1
##for i in range(num, 9):
##    print(num)
##    num += 2
##print("\n")
##
##num = 1
##while num <= 9:
##    print(num)
##    num += 2
