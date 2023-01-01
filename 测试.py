import pandas as pd
import numpy as np

# 数据读取
file1 = pd.DataFrame(pd.read_excel("D:\大数据竞赛/2022/2022年MathorCup大数据竞赛-赛道B初赛\附件1语音业务用户满意度数据.xlsx"))
file2 = pd.DataFrame(pd.read_excel("D:\大数据竞赛/2022/2022年MathorCup大数据竞赛-赛道B初赛\附件2上网业务用户满意度数据.xlsx"))
file3 = pd.DataFrame(pd.read_excel("D:\大数据竞赛/2022/2022年MathorCup大数据竞赛-赛道B初赛\附件3语音业务用户满意度预测数据.xlsx"))
file4 = pd.DataFrame(pd.read_excel("D:\大数据竞赛/2022/2022年MathorCup大数据竞赛-赛道B初赛\附件4上网业务用户满意度预测数据.xlsx"))
resultfile = pd.DataFrame(pd.read_excel("D:\大数据竞赛/2022/2022年MathorCup大数据竞赛-赛道B初赛/result.xlsx"))
print("data reading......done")


# 对附件一进行数据预处理（分类、筛查）
def shaicha1():
    print("附件1的规格（行，列）\n:",file1.shape)
    print("附件1的数据类型：\n",file1.describe())


# 执行控制
shaicha1()
#双向修改测试1
