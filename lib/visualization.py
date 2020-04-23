import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

from lib import dict

matplotlib.rcParams['font.family'] = 'FangSong'


def compare_with_yesterday(y1, y2):
    if y1 >= y2:
        return '+' + str(y1 - y2)
    else:
        return '-' + str(y1 - y2)


if __name__ == '__main__':
    current_stat = dict.PPP

    # 以第一行、第一列为DataFrame的行列信息
    data = pd.read_csv('./export.csv', header=0, index_col=0)
    x = data.index
    # print(x)

    plt.title('Twitter Followers Statistics for Poppin\'Party Members')
    for i in range(0, 5):
        plt.plot(x, data[current_stat[i]['name']], color=current_stat[i]['color'], label=current_stat[i]['id'])
    plt.xticks(x, x, rotation=30)
    plt.legend()
    plt.show()

    print('Poppin\'Party声优Twitter关注者数统计')
    # 哪里NMD有时间啊害搁着百京时间
    print('百京时间' + data.index[len(data) - 1] + '记录')
    for i in range(0, 5):
        print(current_stat[i]['name'] + ': ' + str(
            data[current_stat[i]['name']][len(data) - 1]) + ' (' + compare_with_yesterday(
            data[current_stat[i]['name']][len(data) - 1], data[current_stat[i]['name']][len(data) - 2]) + ')')
    print('*无需授权，随意转载')
    print('*技术支持：申必壬')
    plt.savefig('./temp.png')
