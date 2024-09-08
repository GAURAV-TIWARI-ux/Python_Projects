def slope_intrct(x1,y1,x2,y2):
    if x1==x2:
        return (None,x1)
    elif y1==y2:
        return (0,y1)
    else:
        slope=(y2-y1)/(x2-x1)
        intercept=y1-(slope*x1)
        return (slope,intercept)
x1=float(input('enter the point:'))
y1=float(input('enter the point:'))
x2=float(input('enter the point:'))
y2=float(input('enter the point:'))
print(slope_intrct(x1,y1,x2,y2))
