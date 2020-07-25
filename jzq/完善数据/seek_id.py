'''用来验证两个表的id'''
import pandas as pd

def main():
    csv_1 = pd.read_csv('../control_3LAMOST.csv')
    csv_2 =  pd.read_csv('../galpair_AB3_LAMOST_Av_info_class_mass.csv')

    id_1 = csv_1['plateid'].tolist()
    id_2 = csv_2['id'].tolist()


    id_1.sort()
    print(id_1)
    id_2.sort()
    print(id_2)

if __name__ == '__main__':
    main()