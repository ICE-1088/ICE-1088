import pandas as pd
import numpy as np

def read_csv():
    PATH = "data/new_data.csv"
    with open(PATH,encoding='utf-8') as f:
        DATA = pd.read_csv(f,low_memory=False)
    return DATA

def picture1(month):
    DATA = read_csv()
    leibie = ['百货食品', '服装鞋包', '家居建材', '家用电器', '美妆饰品',
                             '母婴用品', '汽配摩托', '生活服务', '手机数码', '数字阅读',
                             '文化玩乐', '游戏话费', '运动户外', '其他']
    xiaoliang = [0 for i in range(14)]
    jiage = [0 for i in range(14)]
    quanbu = [0 for i in range(14)]
    for i in range(len(DATA['DATA_MONTH'])):
        if(DATA['DATA_MONTH'][i]==month):
            if(DATA['label_1'][i]=="价格异常")and(DATA['label_2'][i]=="销量正常"):
                for j in range(14):
                    if(DATA['CATE_NAME_LV1'][i]==leibie[j]):
                        jiage[j]+=1
                        break
                if DATA['CATE_NAME_LV1'][i]== "其他商品" or DATA['CATE_NAME_LV1'][i] is np.nan:
                    jiage[13] += 1

            if (DATA['label_1'][i] == "价格正常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(14):
                    if (DATA['CATE_NAME_LV1'][i] == leibie[j]):
                        xiaoliang[j] += 1
                        break
                if DATA['CATE_NAME_LV1'][i]== "其他商品" or DATA['CATE_NAME_LV1'][i] is np.nan:
                    xiaoliang[13] += 1
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(14):
                    if (DATA['CATE_NAME_LV1'][i] == leibie[j]):
                        quanbu[j] += 1
                        break
                if DATA['CATE_NAME_LV1'][i]== "其他商品" or DATA['CATE_NAME_LV1'][i] is np.nan:
                    quanbu[13] += 1
        if(month=="quanbu"):
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量正常"):
                for j in range(14):
                    if (DATA['CATE_NAME_LV1'][i] == leibie[j]):
                        jiage[j] += 1
                        break
                if DATA['CATE_NAME_LV1'][i]== "其他商品" or DATA['CATE_NAME_LV1'][i] is np.nan:
                    jiage[13] += 1
            if (DATA['label_1'][i] == "价格正常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(14):
                    if (DATA['CATE_NAME_LV1'][i] == leibie[j]):
                        xiaoliang[j] += 1
                        break
                if DATA['CATE_NAME_LV1'][i]== "其他商品" or DATA['CATE_NAME_LV1'][i] is np.nan:
                    xiaoliang[13] += 1
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(14):
                    if (DATA['CATE_NAME_LV1'][i] == leibie[j]):
                        quanbu[j] += 1
                        break
                if DATA['CATE_NAME_LV1'][i]== "其他商品" or DATA['CATE_NAME_LV1'][i] is np.nan:
                    quanbu[13] += 1

    return leibie,jiage,quanbu,xiaoliang


def picture2(leibie):
    DATA = read_csv()
    month = [202106,202107,202108,202109]
    xiaoliang = [0 for i in range(4)]
    jiage = [0 for i in range(4)]
    quanbu = [0 for i in range(4)]
    for i in range(len(DATA['CATE_NAME_LV1'])):
        if (DATA['CATE_NAME_LV1'][i] == leibie):
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量正常"):
                for j in range(4):
                    if (DATA['DATA_MONTH'][i] == month[j]):
                        jiage[j] += 1
                        break
            if (DATA['label_1'][i] == "价格正常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(4):
                    if (DATA['DATA_MONTH'][i] == month[j]):
                        xiaoliang[j] += 1
                        break
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(4):
                    if (DATA['DATA_MONTH'][i] == month[j]):
                        quanbu[j] += 1
                        break
        if (leibie=="quanbu"):
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量正常"):
                for j in range(4):
                    if (DATA['DATA_MONTH'][i] == month[j]):
                        jiage[j] += 1
                        break
            if (DATA['label_1'][i] == "价格正常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(4):
                    if (DATA['DATA_MONTH'][i] == month[j]):
                        xiaoliang[j] += 1
                        break
            if (DATA['label_1'][i] == "价格异常") and (DATA['label_2'][i] == "销量异常"):
                for j in range(4):
                    if (DATA['DATA_MONTH'][i] == month[j]):
                        quanbu[j] += 1
                        break

    return month,jiage,quanbu,xiaoliang


print(picture1(202106))
print(picture1('quanbu'))

print(picture2("百货食品"))
print(picture2("quanbu"))