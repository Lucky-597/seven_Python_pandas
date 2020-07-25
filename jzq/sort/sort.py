'''作用对文件进行排序alpair_A12_sdss_all_Av.csv galpair_B12_sdss_all_Av.csv'''



import pandas as pd


#对一些特别的文件进行排序
def sort_csvT(file_name,flie_name,field):
    dataT = file_name.sort_values(field, ascending=True)
    dataT.to_csv(flie_name, index=False)


def main():
    # df_t = pd.read_csv('../galpair_AB3_LAMOST_Av_info_class_mass.csv')
    # sort_csvT(df_t, 'galpair_AB3_LAMOST_Av_info_class_mass_sort.csv', 'id')

    df_t = pd.read_csv('../galpair_sdss_mass_new.csv')
    sort_csvT(df_t, 'galpair_sdss_mass_new.csv_sort.csv', 'id')

if __name__ == '__main__':
    main()