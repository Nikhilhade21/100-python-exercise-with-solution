'''Write a program that computes the value of a+aa+aaa+aaaa with a given digit
as the value of a.'''

a = input("Enter: ")
total, tmp = 0, str() 

for i in range(4):
    tmp += a
    total += int(tmp)

print(total)