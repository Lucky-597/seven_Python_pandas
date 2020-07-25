import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def drawing(gcsv, gclassMy, control_csv):
    # 设置dp的区间
    x = np.arange(0, max(gcsv['dp']), 20)  # max(gcsv['dp'])  =  214.34940189999998  min 9.963992042000001
    x = np.append(x, int(max(gcsv['dp'])))

    dp_min = min(gcsv['dp'])
    y = np.array([])
    yerrMax = np.array([])
    yerrMin = np.array([])

    y_c = np.array([])
    yerrMax_c = np.array([])
    yerrMin_c = np.array([])

    sum = len(gclassMy)

    for i in range(len(x) - 1):
        xx = np.arange(x[i], x[i + 1], 3)
        xx = np.append(xx, x[i + 1])  # 因为不能整除3，最后有余数

        yy = []
        yy_c = []
        for j in range(len(xx) - 1):
            print("dp,", xx[j], " ", xx[j + 1])
            if xx[j] < dp_min:
                print("continue")
                continue
            result_csv = gcsv[(gcsv['dp'] >= xx[j]) & (gcsv['dp'] <= xx[j + 1])]  # 筛选

            # 根据id从gclassMy中找
            res_arr = result_csv['id'].tolist()
            g_csv = gclassMy[gclassMy['id'].isin(res_arr)].sort_values(by=['id'])

            # 根据galpair_index找
            galpair_index_arr = g_csv['galpair_index'].tolist()
            c_csv = control_csv[control_csv['galpair_index'].isin(galpair_index_arr)]

            # 根据clsaaMy筛选
            g_csv = g_csv[g_csv.class_my == 3]
            c_csv = c_csv[c_csv.class_my == 3]
            yy.append(len(g_csv) / sum)
            yy_c.append(len(c_csv) / sum)

        # 四分位
        arr = np.percentile(yy, [25, 50, 75])
        y = np.append(y, arr[1])

        arr_c = np.percentile(yy_c, [25, 50, 75])
        y_c = np.append(y_c, arr_c[1])

        yerrMax = np.append(yerrMax, arr[2] - arr[1])
        yerrMax_c = np.append(yerrMax_c, arr_c[2] - arr_c[1])

        yerrMin = np.append(yerrMin, arr[1] - arr[0])
        yerrMin_c = np.append(yerrMin_c, arr_c[1] - arr_c[0])
    x = np.arange(10, 220, 20)  # 设置x坐标

    plt.errorbar(x, y, yerr=[yerrMin, yerrMax], xerr=10, fmt='o', ecolor='black', color='black', elinewidth=2,
                 capsize=4)
    plt.errorbar(x, y_c, yerr=[yerrMin_c, yerrMax_c], xerr=10, fmt='o', mec='black', ecolor='red', color='w',
                 elinewidth=2, capsize=4)

    # fmt :   'o' ',' '.' 'x' '+' 'v' '^' '<' '>' 's' 'd' 'p'
    plt.xlim(0, 220, 10)
    plt.ylim(-0.0075, 0.0075)
    plt.xticks(x)
    plt.show()


def main():
    gcsv = pd.read_csv('../完善数据/galpair_info_arr_dp_ratiom_new.csv')
    gclassMy = pd.read_csv('../完善数据/galpair_sdss_mass_Line_classMy_new.csv')
    control_csv = pd.read_csv('../完善数据/control_Line_classMy_new.csv')
    drawing(gcsv, gclassMy, control_csv)

if __name__ == '__main__':
    main()

