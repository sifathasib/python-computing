''' F: move forward one unit 
    L: turn left counterclockwise(90 degree)
    R: turn right clockwise(90 degree)
    S: stop
    '''
command = 'FFFFFLFFFLFFFFRRRFXFFFFFFS'
#current location and current facing direction 
x,y = 0,0
dx,dy = 1,0
locs=[(0,0)]

for cmd in command:
    if cmd == "S":
        break
    if cmd == "F":
        #move forward to the current direction 
        x += dx 
        y += dy
        if(x,y) in locs:
            print("path crosses itself at:({},{})".format(x,y))
        locs.append((x,y))
        continue
    if cmd == "L":
        #turn to the left 
        #(1,0)->(0,1)->(-1,0)->(0,-1)->(1,0)
        dx,dy = -dy,dx 
        continue
    if cmd == "R":
        #turn to the right 
        # (1,0)->(0,-1)->(-1,0)->(0,1)->(1,0) 
        dx,dy = dy,-dx
        continue
    print("unknown command:",cmd)
else:
    print("instruction ended without stop")
print(locs)   
x,y = zip(*locs)

xmin,xmax = min(x),max(x)
ymin,ymax = min(y),max(y)

#grid size for plotting 
nx = xmax - xmin + 1
ny = ymax - ymin + 1

for iy in reversed(range(ny)):
    for ix in range(nx):
        if(ix+xmin,iy+ymin) in locs:
            print("*",end='')
        else:
            print(' ',end='')
    print()