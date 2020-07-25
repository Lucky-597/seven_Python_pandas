'''用来修改 galpair_AB3_LAMOST_Av_info_class_mass.csv的Class_my
    -1 => 0         1 => 1       2 => 2       3,4 => 3
'''

import pandas as pd


def main():
    csv_file = pd.read_csv('../galpair_AB3_LAMOST_Av_info_class_mass.csv')
    # class_my为-1的对应的下标
    list_fu1 = csv_file[csv_file.class_my == -1]['class_my'].index.tolist()
    list_4 = csv_file[csv_file.class_my == 4]['class_my'].index.tolist()

    for i in list_fu1:
        csv_file.loc[i, 'class_my'] = 0

    for i in list_4:
        csv_file.loc[i, 'class_my'] = 3

    csv_file.to_csv('galpair_AB3_LAMOST_Av_info_class_mass_new.csv', index=False)

if __name__ == '__main__':
    main()