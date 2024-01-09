import math

hourIn, minIn, hourOut, minOut = map(int,input().split())
time_in = (hourIn*60) + minIn
time_out = (hourOut*60) + minOut
Time =  time_out - time_in
if hourIn < 7 or hourIn >= 23 or hourOut < 7 or hourOut >= 23 or minIn > 60 or minOut > 60 or hourIn > hourOut or Time > 960:
    print("ERROR")
elif Time <= 15:
    print("0")
elif 15 < Time <= 180:
    sum = (math.ceil(Time/60))*10
    print(sum)
elif 180 < Time <= 360:
    sum = ((math.ceil(Time/60))*20)-30
    print(sum)
else:
    print("200")