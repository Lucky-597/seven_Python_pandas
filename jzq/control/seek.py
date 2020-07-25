'''寻找control样本集'''

import pandas as pd
import numpy as np
from scipy import stats


def main():
    # 记录次数
    count = 0

    # 读取G表与B表
    Gcsv = pd.read_csv('../galpair_AB3_LAMOST_Av_info_class_mass.csv')
    Bcsv = pd.read_csv('../before_control_mass_test.csv')

    array_z = np.array(Bcsv['z'].tolist())
    array_m = np.array(Bcsv['lgm_tot_p50'].tolist())
    Bindexs = np.array(Bcsv.index.tolist())

    print(Bindexs)

    while True:
        count += 1

        # 根据b表的列创建dataframe对象
        control = pd.DataFrame(columns=Bcsv.columns)

        # 生成control  (循环G表，找出与其每一行的最小diff)
        for i in Gcsv.index:
            print(i,count)
            #找到最小值的位置
            index_t = np.argmin( (abs(array_z - Gcsv['z_obj'][i])) / Gcsv['z_obj'][i] + abs(array_m - Gcsv['mass'][i]) / Gcsv['mass'][i])
            #根据位置， 将此值添加到 control (control中应该存储的最小的diff表示b表的数据)
            control = control.append(Bcsv.loc[ Bindexs[index_t]])

             # 删除操作
            array_z = np.delete(array_z, index_t, axis=0)
            array_m = np.delete(array_m, index_t, axis=0)
            Bindexs = np.delete(Bindexs, index_t, axis=0)

        #保存control_count.csv文件
        control.to_csv('control_' + str(count) + 'LAMOST.csv', index=False)

        #重新保存b表
        # Bcsv.to_csv("before_control_mass_test.csv", index=False)

        #提出G表和 control的 z 列
        G_zlist = Gcsv['z_obj'].tolist()
        C_clidt = control['z'].tolist()
        #ks检验
        sta1, p_value = stats.ks_2samp(G_zlist, C_clidt)
        if p_value < 0.3:   #<0.3程序结束  表示不是同一分布
            break

        # 提出G表和 control的 mass与 lgm_tot_p50 列
        G_lgmlist = Gcsv['mass'].tolist()
        C_lgmlist = control['lgm_tot_p50'].tolist()
        #ks检验
        sta2, p_value = stats.ks_2samp(G_lgmlist, C_lgmlist)
        if p_value < 0.03:
            break

if __name__ == '__main__':
    main()