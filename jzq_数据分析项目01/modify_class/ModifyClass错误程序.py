'''用来修改 My——class的值
-1 => 0         1 => 1       2 => 2       3,4 => 3
galpair_sdss_mass_Line_classMy.此表的 class_my只有 0，1，2，3的情况

'''

import pandas as pd


def main():
    csv_main = pd.read_csv('../galpair_AB3_LAMOST_Av_info_class_mass.csv')
    csv_query = pd.read_csv('../galpair_sdss_mass_Line_classMy.csv')

    # 将class_my的值进行分组
    class0 = csv_query.groupby('class_my').get_group(0)
    class1 = csv_query.groupby('class_my').get_group(1)
    class2 = csv_query.groupby('class_my').get_group(2)
    class3 = csv_query.groupby('class_my').get_group(3)


    for i in csv_main.index:

        # galpair_AB3_LAMOST_Av_info_class_mass的记录与此纪录id对应 galpair_sdss_mass_Line_classMy的id
        id_t = csv_main.loc[i,'id']

        # 根据id找到下标
        list_t = csv_query[csv_query.id == id_t].index.tolist()
        if list_t != []:
            index = list_t.pop()

            #因为 此表3，4都会判断 另一张表是否为3  所以这里把 4转回3，
            if csv_main.loc[i, 'class_my'] == -1  and csv_query.loc[index, 'class_my'] == 0 :
                csv_main.loc[i, 'class_my'] = 0

            if csv_main.loc[i, 'class_my'] == 4 and csv_main.loc[i, 'class_my'] == 3:
                csv_main.loc[i, 'class_my'] = 3

            #class_my为1，2, 3的时候没变化
            # if csv_main.loc[i, 'class_my'] == csv_query.loc[index, 'class_my']:
    csv_main.to_csv('galpair_AB3_LAMOST_Av_info_class_mass_old.csv')

        # print(list_t)







if __name__ == '__main__':
    main()