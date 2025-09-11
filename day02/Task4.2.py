j=0
x=0
y=1
while round(x,7)!=round(y,7):
    y=x
    x=0
    j=j+1
    for i in range(j,0,-1):
        x=((2*i-1)**2/(6+x))
print(x+3)