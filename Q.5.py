import math
for i in range (0,346,15):
    a=round(math.sin(math.radians(i)),4)
    b=round(math.cos(math.radians(i)),4)
    print (i,"-----",a," ",b)
    
