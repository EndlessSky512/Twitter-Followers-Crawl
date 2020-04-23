from bs4 import BeautifulSoup
import urllib.request
import re
import time
def get_followers(id):
    req = urllib.request.urlopen('https://twitter.com/'+id)
    html = req.read().decode('utf-8')
    soup = BeautifulSoup(html,'html.parser') 
    href = soup.find('a',href=re.compile('followers'))
    href=str(href)
    followers = re.search('data-count="\d+"',href)
    followers = re.sub(r'\D', "", followers.group(0))
    return followers
def writedata():
    accountOfPPP = ['aimi_sound','ayasa_ito','Rimi_nsmt','OSae1010','AyakaOhashi']
    nameOfPPP = ['爱美','伊藤彩沙','西本里美','大冢纱英','大桥彩香']
    f = open("PPP.csv",'a',encoding='utf-8')
    localtime = time.strftime("%y-%m-%d", time.localtime())
    print(localtime)
    f.write(localtime + ',')
    for i in range(0,5):
        output = nameOfPPP[i] + "," + get_followers(accountOfPPP[i])
        print(output)
        f.write(output + ',')
    f.write('\n')
    f.close()
