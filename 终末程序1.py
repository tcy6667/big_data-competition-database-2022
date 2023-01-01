import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import missingno as msno
import statsmodels.api as sm
from statsmodels.formula.api import ols


def zhuan_huan():  # 打开文件（附件一改为test1直接存放在D盘）
    list1 = list(range(0, 36))
    xunlian = pd.read_csv('d:/test1.txt', sep='\t', names=list1)
    xunlian.to_csv('d:/test01.csv')
    print('文件格式转换完成')


def cha_kong_zhi():  # 查找空值
    df = pd.DataFrame(pd.read_csv('d:\\test01.csv'))
    jieguo1 = (df.isnull().sum(axis=0) / df.shape[0])
    jieguo1.to_csv('d:/guocheng1.csv')
    print('查找空值完成')


def ke_shi_hua():  # 空值分布可视化
    list2 = [0, 1]
    df1 = pd.read_csv('d:/guocheng1.csv')
    df1.drop([0], axis=0, inplace=True)
    df1.columns = list2
    df1.plot(kind='bar', x=0, y=1)
    plt.show()
    print('空值可视化完成')


def yu_chu_li():  # 数据预处理
    df = pd.DataFrame(pd.read_csv('d:\\test01.csv'))
    df.drop(['23', '26', '34'], axis=1, inplace=True)
    df['36'] = df['35'] / df['19']
    df['30'] = df['30'].values.astype(str)
    for x in range(0, 30000):
        if df.loc[x, '36'] > 1:
            df.drop(x, axis=0, inplace=True)
    df['1'] = pd.to_datetime(df['1'], format='%Y-%m-%d')
    df['11'] = pd.to_datetime(df['11'], format='%Y-%m-%d')
    df['37'] = ((df['1'] - df['11']) / pd.Timedelta(1, 'D')).fillna(0)
    df.to_csv('d:\\test01.csv', index=False)
    print('数据预处理完成')


def yi_chang():  # 异常值可视式化处理
    df = pd.DataFrame(pd.read_csv('d:\\test01.csv'))
    for m in range(1, 38):
        df.plot(kind='scatter', x='Unnamed: 0', y=m)
        plt.show()
    print('异常值分析图绘制完成')


def nian_kuan():  # 分析年款和保值率的关系
    df = pd.DataFrame(pd.read_csv('d:\\test01.csv'))
    df.plot(kind='scatter', x='15', y='36')
    plt.show()
    print('年款数据初步分析完成')


def ni_ming():  # 可视化分析匿名数据中年份数据
    df = pd.DataFrame(pd.read_csv('d:\\test01.csv'))
    df.plot(kind='scatter', x='32', y='36')
    plt.show()
    print('匿名数据初步分析完成')


def ji_suan_xi_shu():  # 计算斯皮尔曼相关系数并排序
    df = pd.DataFrame(pd.read_csv('d:\\test01.csv'))
    df1 = df.corr(method='spearman')
    df1.sort_values(by='36', ascending=False, inplace=True)
    print('相关系数计算完成')


def jian_mo():  # 构建模型并预测
    list1 = ['a','b','c','d','e','f','g','h','i']
    df = pd.DataFrame(pd.read_csv('d:\\test01.csv'))
    df1 = df[['15', '32', '35', '27', '6', '8', '5', '37', '36']]
    df1.columns = list1
    print(df1)
    muxing = ols('i~ a + b + c + d + e + f + g + h',data=df1).fit()
    list2 = list(range(0, 36))
    df4 = pd.read_csv('d:/test2.txt', sep='\t', names=list2)
    df4.to_csv('d:/test02.csv')
    df3 = pd.DataFrame(pd.read_csv('d:\\test02.csv'))
    df3.drop(['23', '26', '34'], axis=1, inplace=True)
    df3['36'] = df3['35'] / df3['19']
    df3['1'] = pd.to_datetime(df3['1'], format='%Y-%m-%d')
    df3['11'] = pd.to_datetime(df3['11'], format='%Y-%m-%d')
    df3['37'] = ((df3['1'] - df3['11']) / pd.Timedelta(1, 'D')).fillna(0)
    df3.to_csv('d:\\test02.csv', index=False)
    print(muxing.predict(df3[['15', '32', '35', '27', '6', '8', '5', '37', '36']]))



def start():  # 上述函数的执行集合
    zhuan_huan()
    cha_kong_zhi()
    ke_shi_hua()
    yu_chu_li()
    ji_suan_xi_shu()
    jian_mo()


def ke_xuan():  # 部分用于中间分析的函数的集合
    yi_chang()
    nian_kuan()
    ni_ming()


start()


def cao_gao():  # 草稿函数，永不执行（手动狗头）
    lll
