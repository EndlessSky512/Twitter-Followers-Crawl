import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
data = pd.read_csv("PPP.csv",header=None)
plt.title("Poppin'Party Members' Twitter Followers Data Chart")
x = data[0].values.tolist()
for i in range(1,6):
    y[i] = data[i * 2].values.tolist()
plt.plot(x,y[1],color='red',label="aimi_sound")
plt.plot(x,y[2],color='purple',label="ayasa_ito")
plt.plot(x,y[3],color='pink',label="Rimi_nsmt")
plt.plot(x,y[4],color='blue',label="OSae1010")
plt.plot(x,y[5],color='yellow',label="AyakaOhashi")
plt.xticks(x, x, rotation=30)
plt.legend()

def compare(y1,y2):
    if (y1 >= y2):
        return "+" + str(y1 - y2)
    else:
        return str(y1-y2)

print("Poppin'Party声优Twitter关注者数统计")
print("百京时间2020年4月23日16：25记录")
nameOfPPP = [' ','爱美','伊藤彩沙','西本里美','大冢纱英','大桥彩香']
for i in range(1,6):
    print(nameOfPPP[i] + " " + compare(y[i][-1],y[i][-2]) + " " + str(y[i][-1]))
print("*无需授权，随意转载")
print("*技术支持：申必壬")
plt.savefig('temp.png')