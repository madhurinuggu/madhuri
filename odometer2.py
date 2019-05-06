l = []
k = int(input("enter number:"))
for i in range(12,90):
    m = i % 10
    n = i // 10
    if m != 0 and n != 0 and n < m and n != m:
        l.append(i)
print(l) 
g = k % 10
h = k // 10
if g == 0 or h == 0 or h > g or h == g:
    print("invalid")
else:
    for j in range(len(l)):
        if k == l[j]:
            if j == len(l) - 1:
                l [j] = l[0]
                print(l[j],l[j - 1])
                break
            elif j == 0:
                l[j - 1] = l[len(l) - 1]
                print(l[j + 1],l[j - 1])
                break
            else:
                print(l[j + 1],l[j - 1])
                break
             
            
