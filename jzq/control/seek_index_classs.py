'''在control_1LAMOST.csv中的每条数据声明，对应G表的id'''

import pandas as pd

def main():
    csv_file = pd.read_csv('control_1LAMOST.csv')
    csv_t = pd.read_csv('../galpair_AB3_LAMOST_Av_info_class_mass.csv')

    csv_file['galpair_index'] = 0
    csv_file['class_my'] = -2
    csv_t['galpair_index'] =0
    for i in csv_file.index:
        csv_file.loc[i,'galpair_index'] = i + 770000
        csv_t.loc[i,'galpair_index'] = i + 770000
        csv_file.loc[i,'class_my'] = csv_t.loc[i,'class_my']

    csv_file.to_csv('control_1_LAMOST.csv', index=False)
    csv_t.to_csv('galpair_AB3_LAMOST_Av_info_class_mass_new.csv', index=False)

    print(csv_file)
    # csv_file.to_csv('control_1_LAMOST.csv', index=False)

if __name__ == '__main__':
    main()