x=int(input('enter the point:'))
y=int(input('enter the point:'))
if x>0 and y>0:
    print('it lies in fist quadrant')
elif x<0 and y>0:
    print('it lies in second quadrant')
elif x<0 and y<0:
    print('it lies in third quadrant')
elif x>0 and y<0:
    print('it lies in forth quadrant')
elif x==0 and y==0:
    print('it lies at origin')
elif x==0 and y>0:
    print('it lies on +ve y-axis')
elif x==0 and y<0:
    print('it lies on -ve y-axis')
elif x>0 and y==0:
    print('it lies on +ve x-axis')
elif x<0 and y==0:
    print('it lies on -ve x-axis')
