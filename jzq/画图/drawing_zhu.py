'''画柱状图'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():

    csv_file = pd.read_csv('../完善数据/galpair_info_arr_dp_ratiom_new.csv')

    plt.figure(figsize=(8,6))

    plt.subplots_adjust(wspace=0.4, hspace=0.4)  #调整子图之间的距离
    plt.rcParams['xtick.direction'] = 'in'      #将x的刻度线方向设置内向
    plt.rcParams['ytick.direction'] = 'in'      #将y的刻度线方向设置内向


    #################################################################
    ADIS = np.array(csv_file['ADIS'].tolist())
    plt.subplot(2,2,1)
    plt.tick_params(top='on', right='on', which='major')#显示上侧和右侧的刻度

    plt.hist(ADIS, histtype='bar', range=(0,600), edgecolor='black', color='white') # 画图
    plt.xlim(0,600)#设置x轴分布范围


    plt.xlabel('Angular separation (arcsec)')
    plt.ylabel('Number of galaxies')

    #############################################     2

    dp = np.array(csv_file['dp'].tolist())
    plt.subplot(2, 2, 2)
    plt.hist(dp, histtype='bar', edgecolor='black', color='w')
    # plt.hist(dp,histtype='bar',range=(0,200),edgecolor='black',color='w')
    plt.xlabel('Projected separation(kpc)')
    plt.ylabel('Number of galaxies')
    plt.xlim(min(dp), max(dp))  # 设置x轴分布范围

    plt.tick_params(top='on', right='on', which='major')  # 显示上侧和右侧的刻度

    ##############################################      3
    DV = np.array(csv_file['DV'].tolist())
    plt.subplot(2, 2, 3)
    plt.hist(DV, histtype='bar', edgecolor='black', color='w')
    plt.xlabel('$\Delta$V(km/s)')
    plt.ylabel('Number of galaxies')
    plt.tick_params(top='on', right='on', which='major')  # 显示上侧和右侧的刻度
    plt.xlim(min(DV), max(DV))  # 设置x轴分布范围

    #################################################################       4
    ratio_m = np.array(csv_file[csv_file.ratio_m != -9999]['ratio_m'].tolist())
    plt.subplot(2, 2, 4)
    plt.hist(ratio_m, histtype='bar', range=(0.8, 1.2), edgecolor='black', color='w')
    plt.xlabel('Log mass ratio')
    plt.ylabel('Number of galaxies')
    plt.tick_params(top='on', right='on', which='major')  # 显示上侧和右侧的刻度
    plt.xlim(0.8, 1.2)  # 设置x轴分布范围

    # plt.savefig("fenlei.png")

    plt.show()

if __name__ == '__main__':
    main()