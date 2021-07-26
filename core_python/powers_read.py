f = open('powers.txt','r')
squares,cubed,fourth = [],[],[]
for line in f.readlines():
    field = line.split(',')
    squares.append(int(field[1]))
    cubed.append(int(field[2]))
    fourth.append(int(field[3]))
f.close()
n= 457 
print(n ,'cubed is ',cubed[n-1])