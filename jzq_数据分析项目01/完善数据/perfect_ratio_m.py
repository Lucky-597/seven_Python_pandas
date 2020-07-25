'''完善数据
此程序的理解是，对原来项目galpair_info_arr_dp_ratiom 无质量的-9999
根据ZFLAG_A 与 ZFLAG_B这两列有3的，在galpair_AB3_LAMOST_Av_info_class_mass中搜索Member的A或者B对应的mess，进行质量补充
那么在galpair_sdss_mass_new就能找到另一个星系的质量，得到A/B的质量比

'''

import pandas as pd

num = 0

def seek_AB(i, csv_t,csv_AB, ZFLAG_T, Member_T, csv_main):
    # 初始化 A，B质量
    Quality_1 = -9999
    Quality_2 = -9999

    global num

    # 我们去获取这里面id相等的记录 （因为我不确定，每一个-9999都可以在这找到对应的id）
    for j in Member_T.index:
        id_1 = csv_t.loc[i, 'id']
        if id_1 == Member_T.loc[j, 'id']:

            # 得到A质量 或 B质量
            Quality_1 = Member_T.loc[j, 'mass']
            # print(Quality_1)
            # print(id_1)

            # 当我得到一个质量的时候，我去另一张表去寻找 另一个的质量， 因为我已经知道了id，我可以通过id去锁定它的下标
            list_t = csv_AB[csv_AB.id == id_1].index.tolist()
            if list_t != []:
                Quality_2 = csv_AB.loc[list_t[0], 'lgm_tot_p50']
                # print(Quality_2)
            break

    if Quality_1 == -9999 or Quality_2 == -9999:
        ratio_m = -9999
    else:
        if ZFLAG_T == 'ZFLAG_A':
            ratio_m = Quality_1 / Quality_2
        else:
            ratio_m = Quality_2 / Quality_1
            print(ratio_m)

        index = csv_main[csv_main.id == id_1].index.tolist().pop()
        csv_main.loc[index, 'ratio_m'] = ratio_m

        num += 1
        print(index,num)




def main():
    csv_main = pd.read_csv('../galpair_info_arr_dp_ratiom.csv')
    csv_AB1 =  pd.read_csv('../sort/galpair_AB3_LAMOST_Av_info_class_mass_sort.csv')
    csv_AB2 =  pd.read_csv('../sort/galpair_sdss_mass_new.csv_sort.csv')


    #筛选出  没有质量的记录
    csv_t = csv_main[csv_main['ratio_m'] == -9999]

    #Member等于A的组
    Member_A = csv_AB1.groupby('Member').get_group('A')
    #Member等于B的组
    Member_B = csv_AB1.groupby('Member').get_group('B')


    for i in csv_t.index:
        if csv_t.loc[i, 'ZFLAG_A'] == 3:
            seek_AB(i, csv_t, csv_AB2, 'ZFLAG_A', Member_A, csv_main)
        elif csv_t.loc[i, 'ZFLAG_B'] == 3:
            seek_AB(i, csv_t, csv_AB2, 'ZFLAG_B', Member_B, csv_main)
        else:
            continue
    csv_main.to_csv('galpair_info_arr_dp_ratiom_new.csv', index=False)


if __name__ == '__main__':
    main()