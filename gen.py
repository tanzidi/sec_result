import pandas as pd
import numpy as np

first_sem_full = []
reg = 2015331503

try:
    df = pd.read_excel('data/Q_GPA_1st.xlsx')
    idx = df.columns

    df1 = df.loc[df[idx[1]] == reg]
    name = df1[idx[2]].values[0]

    # 1st semester
    first_sem_code = []
    first_sem_lg = []
    first_sem_gp = []
    first_sem_cr = []
    first_sem_final = []
    for i in range(1, len(idx)):
        raw = idx[i].split("_")
        if raw[0] != 'GP':
            continue
        if (str(df1[idx[i]].values[0]) == 'nan'):
            continue
        first_sem_code.append(raw[1])
        first_sem_gp.append(df1[idx[i]].values[0])
        first_sem_lg.append(df1[idx[i + 1]].values[0])
        first_sem_cr.append(df1[idx[i + 2]].values[0])
    first_sem_final.append(df1['Credit_1st'].values[0])
    first_sem_final.append(df1['GPA_1st'].values[0])
    # first_sem_final.append(lg_cal(df1['GPA_1st'].values[0]))
    first_sem_final.append(df1['Credit_1st'].values[0])
    first_sem_final.append(df1['GPA_1st'].values[0])
    # first_sem_final.append(lg_cal(df1['GPA_1st'].values[0]))

    # print(first_sem_code, first_sem_gp, first_sem_lg, first_sem_cr, first_sem_final)
    for i in range(0, len(first_sem_code)):
        dict = {}
        dict['code'] = first_sem_code[i]
        dict['title'] = "nothing"
        dict['gp'] = first_sem_gp[i]
        dict['lg'] = first_sem_lg[i]
        dict['cr'] = first_sem_cr[i]
        first_sem_full.append(dict)
except:
    print("no resutl for 1st sem")




try:
    # 2nd semester
    df = pd.read_excel('data/Q_GPA_2nd.xlsx')
    idx = df.columns
    df1 = df.loc[df[idx[1]] == reg]
    name = df1[idx[2]].values[0]
    second_sem_code = []
    second_sem_lg = []
    second_sem_gp = []
    second_sem_cr = []
    second_sem_final = []
    for i in range(1, len(idx)):
        raw = idx[i].split("_")
        if raw[0] != 'GP':
            continue
        if (str(df1[idx[i]].values[0]) == 'nan'):
            continue
        second_sem_code.append(raw[1])
        second_sem_gp.append(df1[idx[i]].values[0])
        second_sem_lg.append(df1[idx[i + 1]].values[0])
        second_sem_cr.append(df1[idx[i + 2]].values[0])

    second_sem_final.append(df1['Credit_2nd'].values[0])
    second_sem_final.append(df1['GPA_2nd'].values[0])
    # second_sem_final.append(lg_cal(df1['GPA_2nd'].values[0]))
    second_sem_final.append(df1['Total_C'].values[0])
    second_sem_final.append(df1['CGPA'].values[0])
    # second_sem_final.append(lg_cal(df1['CGPA'].values[0]))

    # print(second_sem_code, second_sem_gp, second_sem_lg, second_sem_cr, second_sem_final)
except:
    print("no result for sem 2")

try:
    # 3rd semester
    df = pd.read_excel('data/Q_CGPA_3rd.xlsx')
    idx = df.columns
    df1 = df.loc[df[idx[1]] == reg]
    name = df1[idx[2]].values[0]

    third_sem_code = []
    third_sem_lg = []
    third_sem_gp = []
    third_sem_cr = []
    third_sem_final = []
    for i in range(1, len(idx)):
        raw = idx[i].split("_")
        if raw[0] != 'GP':
            continue
        if (str(df1[idx[i]].values[0]) == 'nan'):
            continue
        third_sem_code.append(raw[1])
        third_sem_gp.append(df1[idx[i]].values[0])
        third_sem_lg.append(df1[idx[i + 1]].values[0])
        third_sem_cr.append(df1[idx[i + 2]].values[0])
        
    third_sem_final.append(df1['T_Credit'].values[0])
    third_sem_final.append(df1['GPA_3rd'].values[0])
    # third_sem_final.append(lg_cal(df1['GPA_3rd'].values[0]))
    third_sem_final.append(df1['Credit_1st_3rd'].values[0])
    third_sem_final.append(df1['CGPA_3rd'].values[0])
    # third_sem_final.append(lg_cal(df1['CGPA_3rd'].values[0]))

    # print(third_sem_code,"\n", third_sem_gp,"\n", third_sem_lg,"\n", third_sem_cr,"\n", third_sem_final)
except:
    print("no result for sem 3")

try:
    # 4th semester
    df = pd.read_excel('data/Q_CGPA_4th.xlsx')
    idx = df.columns
    df1 = df.loc[df[idx[1]] == reg]
    name = df1[idx[2]].values[0]
   

    fourth_sem_code = []
    fourth_sem_lg = []
    fourth_sem_gp = []
    fourth_sem_cr = []
    fourth_sem_final = []

    for i in range(1, len(idx)):
        raw = idx[i].split("_")
        if raw[0] != 'GP':
            continue
        if (str(df1[idx[i]].values[0]) == 'nan'):
            continue
        fourth_sem_code.append(raw[1])
        fourth_sem_gp.append(df1[idx[i]].values[0])
        fourth_sem_lg.append(df1[idx[i + 1]].values[0])
        fourth_sem_cr.append(df1[idx[i + 2]].values[0])
        
    fourth_sem_final.append(df1['T_Credit'].values[0])
    fourth_sem_final.append(df1['GPA_4th'].values[0])
    # fourth_sem_final.append(lg_cal(df1['GPA_4th'].values[0]))
    fourth_sem_final.append(df1['Total_Credit'].values[0])
    fourth_sem_final.append(df1['CGPA'].values[0])
    # fourth_sem_final.append(lg_cal(df1['CGPA'].values[0]))

    # print(fourth_sem_code,"\n", fourth_sem_gp,"\n", fourth_sem_lg,"\n", fourth_sem_cr,"\n", fourth_sem_final)
except:
    print("no result for sem 4")

try:
    # 5th semester
    df = pd.read_excel('data/Q_CGPA_5th.xlsx')
    idx = df.columns
    df1 = df.loc[df[idx[1]] == reg]
    name = df1[idx[2]].values[0]
   

    fifth_sem_code = []
    fifth_sem_lg = []
    fifth_sem_gp = []
    fifth_sem_cr = []
    fifth_sem_final = []

    for i in range(1, len(idx)):
        raw = idx[i].split("_")
        if raw[0] != 'GP':
            continue
        if (str(df1[idx[i]].values[0]) == 'nan'):
            continue
        fifth_sem_code.append(raw[1])
        fifth_sem_gp.append(df1[idx[i]].values[0])
        fifth_sem_lg.append(df1[idx[i + 1]].values[0])
        fifth_sem_cr.append(df1[idx[i + 2]].values[0])
        
    fifth_sem_final.append(df1['T_Credit'].values[0])
    fifth_sem_final.append(df1['GPA_5th'].values[0])
    # fifth_sem_final.append(lg_cal(df1['GPA_5th'].values[0]))
    fifth_sem_final.append(df1['Credit_1st_5th'].values[0])
    fifth_sem_final.append(df1['CGPA_5th'].values[0])
    # fifth_sem_final.append(lg_cal(df1['CGPA_5th'].values[0]))

    # print(fifth_sem_code,"\n", fifth_sem_gp,"\n", fifth_sem_lg,"\n", fifth_sem_cr,"\n", fifth_sem_final)
except:
    print("no res for sem 5\n")

try:
    # 6th semester
    df = pd.read_excel('data/Q_CGPA_6th.xlsx')
    idx = df.columns
    df1 = df.loc[df[idx[1]] == reg]
    name = df1[idx[2]].values[0]
   

    sixth_sem_code = []
    sixth_sem_lg = []
    sixth_sem_gp = []
    sixth_sem_cr = []
    sixth_sem_final = []

    for i in range(1, len(idx)):
        raw = idx[i].split("_")
        if raw[0] != 'GP':
            continue
        if (str(df1[idx[i]].values[0]) == 'nan'):
            continue
        sixth_sem_code.append(raw[1])
        sixth_sem_gp.append(df1[idx[i]].values[0])
        sixth_sem_lg.append(df1[idx[i + 1]].values[0])
        sixth_sem_cr.append(df1[idx[i + 2]].values[0])
        
    sixth_sem_final.append(df1['T_Credit'].values[0])
    sixth_sem_final.append(df1['GPA_6th'].values[0])
    # sixth_sem_final.append(lg_cal(df1['GPA_6th'].values[0]))
    sixth_sem_final.append(df1['Total_Credit'].values[0])
    sixth_sem_final.append(df1['CGPA_6th'].values[0])
    # sixth_sem_final.append(lg_cal(df1['CGPA_6th'].values[0]))

    # print(sixth_sem_code,"\n", sixth_sem_gp,"\n", sixth_sem_lg,"\n", sixth_sem_cr,"\n", sixth_sem_final)
except:
    print("no res for sem 6\n")

try:
    # 7th semester
    df = pd.read_excel('data/Q_CGPA_7th.xlsx')
    idx = df.columns
    df1 = df.loc[df[idx[1]] == reg]
    name = df1[idx[2]].values[0]
   

    seventh_sem_code = []
    seventh_sem_lg = []
    seventh_sem_gp = []
    seventh_sem_cr = []
    seventh_sem_final = []

    for i in range(1, len(idx)):
        raw = idx[i].split("_")
        if raw[0] != 'GP':
            continue
        if (str(df1[idx[i]].values[0]) == 'nan'):
            continue
        seventh_sem_code.append(raw[1])
        seventh_sem_gp.append(df1[idx[i]].values[0])
        seventh_sem_lg.append(df1[idx[i + 1]].values[0])
        seventh_sem_cr.append(df1[idx[i + 2]].values[0])
        
    seventh_sem_final.append(df1['T_Credit'].values[0])
    seventh_sem_final.append(df1['GPA_7th'].values[0])
    # seventh_sem_final.append(lg_cal(df1['GPA_7th'].values[0]))
    seventh_sem_final.append(df1['Total_Credit'].values[0])
    seventh_sem_final.append(df1['CGPA_7th'].values[0])
    # seventh_sem_final.append(lg_cal(df1['CGPA_7th'].values[0]))

    # print(seventh_sem_code,"\n", seventh_sem_gp,"\n", seventh_sem_lg,"\n", seventh_sem_cr,"\n", seventh_sem_final)
except:
    print("no res for sem 7")

try:
    # 8th semester
    df = pd.read_excel('data/Q_CGPA_8th.xlsx')
    idx = df.columns
    df1 = df.loc[df[idx[1]] == reg]
    name = df1[idx[2]].values[0]
   

    eighth_sem_code = []
    eighth_sem_lg = []
    eighth_sem_gp = []
    eighth_sem_cr = []
    eighth_sem_final = []

    for i in range(1, len(idx)):
        raw = idx[i].split("_")
        if raw[0] != 'GP':
            continue
        if (str(df1[idx[i]].values[0]) == 'nan'):
            continue
        eighth_sem_code.append(raw[1])
        eighth_sem_gp.append(df1[idx[i]].values[0])
        eighth_sem_lg.append(df1[idx[i + 1]].values[0])
        eighth_sem_cr.append(df1[idx[i + 2]].values[0])
        
    eighth_sem_final.append(df1['T_Credit'].values[0])
    eighth_sem_final.append(df1['GPA_8th'].values[0])
    # eighth_sem_final.append(lg_cal(df1['GPA_8th'].values[0]))
    eighth_sem_final.append(df1['Total_Credit'].values[0])
    eighth_sem_final.append(df1['CGPA_8th'].values[0])
    # eighth_sem_final.append(lg_cal(df1['CGPA_8th'].values[0]))

    # print(eighth_sem_code,"\n", eighth_sem_gp,"\n", eighth_sem_lg,"\n", eighth_sem_cr,"\n", eighth_sem_final)
except:
    print("no res for sem 8")

try:
    # 8th semester extra
    df = pd.read_excel('data/Q_CGPA_8th Repeat.xlsx')
    idx = df.columns
    df1 = df.loc[df[idx[1]] == 2013331546]
    name = df1[idx[2]].values[0]
   

    eight_extra_sem_code = []
    eight_extra_sem_lg = []
    eight_extra_sem_gp = []
    eight_extra_sem_cr = []
    eight_extra_sem_final = []

    # print(df1.shape())

    for i in range(1, len(idx)):
        raw = idx[i].split("_")
        if raw[0] != 'GP':
            continue
        if (str(df1[idx[i]].values[0]) == 'nan'):
            continue
        eight_extra_sem_code.append(raw[1])
        eight_extra_sem_gp.append(df1[idx[i]].values[0])
        eight_extra_sem_lg.append(df1[idx[i + 1]].values[0])
        eight_extra_sem_cr.append(df1[idx[i + 2]].values[0])
        
    eight_extra_sem_final.append(df1['T_Credit'].values[0])
    eight_extra_sem_final.append(df1['GPA_8th'].values[0])
    # eight_extra_sem_final.append(lg_cal(df1['GPA_8th'].values[0]))
    eight_extra_sem_final.append(df1['Total_Credit'].values[0])
    eight_extra_sem_final.append(df1['CGPA_8th'].values[0])
    # eight_extra_sem_final.append(lg_cal(df1['CGPA_8th'].values[0]))

    # print(eight_extra_sem_code,"\n", eight_extra_sem_gp,"\n", eight_extra_sem_lg,"\n", eight_extra_sem_cr,"\n", eight_extra_sem_final)
except:
    print("no res for sem 8 ex")

print(first_sem_full)