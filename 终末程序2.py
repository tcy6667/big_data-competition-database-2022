import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import missingno as msno


def zhuan_huan():  # 打开文件（附件四改为test4直接存放在D盘）
    list1 = list(range(1, 7))
    xunlian = pd.read_csv('d:/test4.txt', sep='\t', names=list1)
    xunlian.to_csv('d:/test04.csv')
    print('文件格式转换完成')


def cha_kong_zhi():  # 查找空值
    data = pd.read_csv('d:\\test04.csv')
    df = pd.DataFrame(data)
    jieguo1 = (df.isnull().sum(axis=0) / df.shape[0])
    jieguo1.to_csv('d:/guocheng4.csv')
    print('查找空值完成')


def yu_chu_li():  # 数据预处理
    data = pd.read_csv('d:\\test04.csv')
    df = pd.DataFrame(data)
    df['2'] = pd.to_datetime(df['2'], format='%Y-%m-%d')
    df['5'] = pd.to_datetime(df['5'], format='%Y-%m-%d')
    df['6'] = pd.to_datetime(df['6'], format='%Y-%m-%d')
    for m in range(0, 10000):
        if df.loc[m, '6'] != None:
            df.loc[m, '7'] = ((df[m, '6'] - df[m, '2']) / pd.Timedelta(1, 'D')).fillna(0)
        else:
            continue
    df.to_csv('d:\\test04.csv', index=False)
    print('数据预处理完成')


def yi_chang():  # 异常值可程式化处理
    data = pd.read_csv('d:\\test01.csv')
    df = pd.DataFrame(data)
    for m in range(1, 38):
        df.plot(kind='scatter', x='Unnamed: 0', y=m)
        plt.show()
    print('异常值分析图绘制完成')


def ji_suan_xi_shu():  # 计算斯皮尔曼相关系数
    data = pd.read_csv('d:\\test04.csv')
    df = pd.DataFrame(data)
    print(df.corr(method='spearman'))
    print('相关系数计算完成')


def start():  # 上述函数的执行集合
    zhuan_huan()
    cha_kong_zhi()
    ji_suan_xi_shu()


def ke_xuan():  # 部分用于中间分析的函数的集合
    yi_chang()
    yu_chu_li()


start()


def cao_gao():  # 草稿函数，永不执行（手动狗头）
    lll
