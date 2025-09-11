x=0
for i in range(10000000):
    if i%2==0:
        x+=(1/(2*(i+1)-1))
    else:
        x-=(1/(2*(i+1)-1))
print(x*4)