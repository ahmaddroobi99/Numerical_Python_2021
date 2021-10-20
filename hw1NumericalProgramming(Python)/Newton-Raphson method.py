import math

def u(x, y):

    f=(x-1)**3 +.512/y
    return f


def v( x,y):

    f= x-2*math.sqrt(x*y)
    return f

def ux( x,  y):

    return 3*(x-1)**2


def uy( x,  y):

    return -0.512/(y)**2


def vx( x,y):

    return 1-math.sqrt(y/x)


def vy( x,  y):

    return -math.sqrt(x/y)


def abso(x):

    if (x < 0):
        x=-x
    return x




x1=5
y1=1
i=10
while(1):

        x2=x1-(u(x1,y1)*vy(x1,y1)-v(x1,y1)*uy(x1,y1))/(ux(x1,y1)*vy(x1,y1)-uy(x1,y1)*vx(x1,y1))
        y2=y1-(v(x1,y1)*ux(x1,y1)-u(x1,y1)*vx(x1,x1))/(ux(x1,y1)*vy(x1,y1)-uy(x1,y1)*vx(x1,y1))
        eax=(x2-x1)/x2
        eay=(y2-y1)/y2
        print(i,x2,y2,eax,eay,0x0A)
        x1=x2
        y1=y2
        i=i-1
        if(i<=0) :
            break
