from bs4 import BeautifulSoup
import re
import ssl
import time
import urllib.request

from lib import dict


def get_followers(id):
    """
    获取指定Twitter账号的Follower数量
    :param id: Twitter账号ID
    :return: Follower数量
    """
    req = urllib.request.urlopen('https://twitter.com/' + id)
    html = req.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    href = soup.find('a', href=re.compile('followers'))
    href = str(href)
    fo = re.search('data-count="\d+"', href)
    fo = re.sub(r'\D', '', fo.group(0))
    return fo


def write_to_file(current_statistics, followers):
    """
    将获取到的信息写入文件
    :param current_statistics: 当前统计的企划。这决定了生成文件的列名。目前因为文件是事先建立的，这个参数传进来还没什么卯月。
    :param followers: 各成员Follower数量的数组
    """
    f = open('../export.csv', 'a', encoding='utf-8')
    localtime = time.strftime('%y-%m-%d', time.localtime())
    f.write(localtime + ',')
    for i in range(0, len(followers) - 1):
        f.write(followers[i] + ',')
    f.write(followers[len(followers) - 1])
    f.write('\n')
    f.close()


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    current_statistics = dict.PPP
    followers = []
    for i in range(0, 5):
        followers.append(get_followers(current_statistics[i]['id']))
    write_to_file(current_statistics, followers)
