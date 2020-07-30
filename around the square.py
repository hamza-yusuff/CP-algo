import math
while True:
    try:
      s=list(map(int,input().split()))
      pi=3.14159
      areacircle=0.25*pi*(s[1]**2+s[2]**2+s[3]**2+s[4]**2)
      square=s[0]**2-areacircle
      print('{:.3f}'.format(square))
    except:
        break
