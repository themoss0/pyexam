c = 0
for line in open('task9/2671/2671.txt'):
    a = [int(x) for x in line.split()]
    u1 = (0 in a)
    u2 = (a[0]+a[1] == 0 or a[1]+a[2]==0 or a[0]+a[2]==0)
    u3=(a[0]+a[1]+a[2]==0)
    if (u1 or u2 or u3):
        c+=1
print(c) 

