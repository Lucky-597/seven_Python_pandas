import pandas as pd
import numpy as np
import openpyxl


# 查找缺省值
def avg(writer, excel_t):
    # print(excel_t)
    groupYear = excel_t.groupby('年份')

    # 根据年份分组
    for year,groupyear in  groupYear:
        print(year)

        # 根据楼号分组
        groupLou = groupyear.groupby('楼号')
        for lou, grouplou in groupLou:

            # 记录缺省用水量的坐标
            index_empty = []
           # 用水总和和数量
            sum = 0
            count = 0
            print(year, '年', '='*30, '查找缺省值', lou, '='*30)
            for i in grouplou.index:
                if pd.isnull(excel_t.loc[i, '用水量（立方）']):
                    index_empty.append(i)
                else:
                    sum += excel_t.loc[i, '用水量（立方）']
                    count += 1
            avg = sum/count
            for inx in index_empty:
                excel_t.loc[inx,'用水量（立方）'] = avg
    excel_t.to_excel(writer, sheet_name='居民用水统计总表', index=False)


# 统计用户年度用水量 / 楼年度用水量
def statistic(writer, excel_t, ls_firstvalue, lou_hu, sheet ):
    # print(excel_t)

    #创建列表，用来遍历 存储行名
    list_year = [ls_firstvalue]

    #根据户号/楼号 与年份分组
    lou_hu_group = excel_t.groupby(lou_hu)
    year_group = excel_t.groupby('年份')

    # 创建存储用户用水情况的Dataframe

    for i,group_t in year_group:
        list_year.append(i)
    excel_hu_sum = pd.DataFrame(columns=list_year)

    # 首先把第一列用来对应独立的用户/对立楼房
    line_count = 0
    for hu, group_t in lou_hu_group:
        excel_hu_sum.loc[line_count, ls_firstvalue] = hu
        line_count += 1

    # 统计每年每户用户用水总量
    for year,groupY in year_group:
        print('='*15, year, '='*15)
        lou_hu_group_Y = groupY.groupby(lou_hu)
        for lou_hu_t, groupH in lou_hu_group_Y:
            print('+'*15, lou_hu, '+'*15)
            sum_hu_lou = 0
            for index in groupH.index:
                sum_hu_lou += excel_t.loc[index, '用水量（立方）']
            print(year,'年,用户/楼:',lou_hu_t,'用水',sum_hu_lou)

            # 将用户用水/楼  每年用水量和存储
            excel_hu_sum.loc[excel_hu_sum[ls_firstvalue] == lou_hu_t, year]= sum_hu_lou
    excel_hu_sum.to_excel(writer, sheet_name=sheet, index=False)
    return excel_hu_sum


#统计年度用水量最多的用户
def big_hu(writer, excel_water_t):
    excel_big = pd.DataFrame(columns=['年份', '用水量最大房号'])
    year_list = ['2015', '2016', '2017', '2018', '2019']
    for i in range(len(year_list)):
        # 保存年份
        excel_big.loc[i, '年份'] = year_list[i]

        # 寻找最大值的下标
        list_t = excel_water_t[year_list[i]].tolist()
        write_lists = np.array(list_t)
        maxindex = np.argmax(write_lists)

        # 年份对应的最大值
        excel_big.loc[i, '用水量最大房号'] = excel_water_t.loc[maxindex, '房号/年份']

    excel_big.to_excel(writer, sheet_name= '年度用水量最大业主', index=False)




def main():
    # 以字符串的格式读取日期与房号
    excel_water = pd.read_excel('用水情况.xlsx', converters={u'房号':str, '日期':str})

    excel_water['年份'] = excel_water['日期'].str[:4]
    excel_water['楼号'] = excel_water['房号'].str[:2]

    with pd.ExcelWriter('用水情况（完成版）.xlsx') as writer:
        avg(writer,excel_water)
        excel_water_t = statistic(writer, excel_water, '房号/年份', '房号', '用户年度用水')
        statistic(writer, excel_water, '楼号/年份', '楼号', '楼年度用水')
        big_hu(writer, excel_water_t)

if __name__ == '__main__':
    main()