'''完善 galpair_sdss_mass_Line_classMy 与 control_Line_classMy.csv'''

import pandas as pd

# 对样本进行合并
def concat_control(file_name, csv_main, csv_t):
    frames = [csv_main, csv_t]
    all_csv = pd.concat(frames)
    print(all_csv)
    all_csv.to_csv(file_name, index=False)

# 对另一个进行合并
def concat_gsml(file_name, csv_main, csv_t):

    # 删除不需要的列
    csv_t = csv_t.drop(['fitsname_1', 'age_lightW', 'metal_lightW', 'snrr', 'AV_SFD', 'Member'], axis=1)
    # 修改列名
    csv_t.rename(columns={'mass': 'lgm_tot_p50', 'objra': 'ra', 'objdec': 'dec', 'z_obj': 'z'}, inplace=True)
    print(csv_t)
    frames = [csv_main, csv_t]
    all_csv = pd.concat(frames)
    print(all_csv)
    all_csv.to_csv(file_name, index=False)

def main():
    csv_control_mian = pd.read_csv('../control_Line_classMy.csv')
    csv_control_t = pd.read_csv('../control/control_1_LAMOST.csv')
    concat_control( 'control_Line_classMy_new.csv', csv_control_mian, csv_control_t)

    csv_gsml_mian = pd.read_csv('../galpair_sdss_mass_Line_classMy.csv')
    csv_gsml_t = pd.read_csv('../control/galpair_AB3_LAMOST_Av_info_class_mass_new.csv')
    concat_gsml('galpair_sdss_mass_Line_classMy_new.csv', csv_gsml_mian, csv_gsml_t)

if __name__ == '__main__':
    main()