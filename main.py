
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# ******************************
num3 = [ ]
if len(num1) < len(num2):
    numm = num2
else:
    numm = num1
for i in range (len(numm)):
    try:
        num3.append(num1[i])
    except:
        continue
    try:
        num3.append(num2[i])
    except:
        continue

print(num3)
# ******************************

# print (num3) 
