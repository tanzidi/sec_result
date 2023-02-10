from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import os
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

def lg_cal(n):
        if (n < 2.00):
            return "F"
        elif (n < 2.25):
            return "C-"
        elif (n < 2.50):
            return "C"
        elif (n < 2.75):
            return "C+"
        elif (n < 3.00):
            return "B-"
        elif (n < 3.25):
            return "B"
        elif (n < 3.50):
            return "B+"
        elif (n < 3.75):
            return "A-"
        elif (n < 4.00):
            return "A"
        else:
            return "A+"

def gradesheet(request):

    first_sem_full = []
    first_sem_final = {}
    second_sem_full = []
    second_sem_final = {}
    third_sem_full = []
    third_sem_final = {}
    fourth_sem_full = []
    fourth_sem_final = {}
    fifth_sem_full = []
    fifth_sem_final = {}
    sixth_sem_full = []
    sixth_sem_final = {}
    seventh_sem_full = []
    seventh_sem_final = {}
    eighth_sem_full = []
    eighth_sem_final = {}
    eighth_sem_re_full = []
    eighth_sem_re_final = {}
    
    reg = 2015331503

    try:
        df = pd.read_excel(staticfiles_storage.path('data/Q_GPA_1st.xlsx'))

        idx = df.columns
        df1 = df.loc[df[idx[1]] == reg]
        name = df1[idx[2]].values[0]

        # 1st semester
        first_sem_code = []
        first_sem_lg = []
        first_sem_gp = []
        first_sem_cr = []
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
        first_sem_final['cr_cur'] = (df1['Credit_1st'].values[0])
        first_sem_final['gp_cur'] = (df1['GPA_1st'].values[0])
        first_sem_final['lg_cur'] = (lg_cal(df1['GPA_1st'].values[0]))
        first_sem_final['cr_com'] = (df1['Credit_1st'].values[0])
        first_sem_final['gp_com'] = (df1['GPA_1st'].values[0])
        first_sem_final['lg_com'] = (lg_cal(df1['GPA_1st'].values[0]))
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
        df = pd.read_excel(staticfiles_storage.path('data/Q_GPA_2nd.xlsx'))
        idx = df.columns
        df1 = df.loc[df[idx[1]] == reg]
        name = df1[idx[2]].values[0]
        second_sem_code = []
        second_sem_lg = []
        second_sem_gp = []
        second_sem_cr = []
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

        second_sem_final['cr_cur'] = (df1['Credit_2nd'].values[0])
        second_sem_final['gp_cur'] = (df1['GPA_2nd'].values[0])
        second_sem_final['lg_cur'] = (lg_cal(df1['GPA_2nd'].values[0]))
        second_sem_final['cr_com'] = (df1['Total_C'].values[0])
        second_sem_final['gp_com'] = (df1['CGPA'].values[0])
        second_sem_final['lg_com'] = (lg_cal(df1['CGPA'].values[0]))

        # print(second_sem_code, second_sem_gp, second_sem_lg, second_sem_cr, second_sem_final)
        for i in range(0, len(second_sem_code)):
            dict = {}
            dict['code'] = second_sem_code[i]
            dict['title'] = "nothing"
            dict['gp'] = second_sem_gp[i]
            dict['lg'] = second_sem_lg[i]
            dict['cr'] = second_sem_cr[i]
            second_sem_full.append(dict)
    except:
        print("no result for sem 2")

    try:
        # 3rd semester
        df = pd.read_excel(staticfiles_storage.path('data/Q_CGPA_3rd.xlsx'))
        idx = df.columns
        df1 = df.loc[df[idx[1]] == reg]
        name = df1[idx[2]].values[0]

        third_sem_code = []
        third_sem_lg = []
        third_sem_gp = []
        third_sem_cr = []
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

        third_sem_final['cr_cur'] = (df1['T_Credit'].values[0])
        third_sem_final['gp_cur'] = (df1['GPA_3rd'].values[0])
        third_sem_final['lg_cur'] = (lg_cal(df1['GPA_3rd'].values[0]))
        third_sem_final['cr_com'] = (df1['Credit_1st_3rd'].values[0])
        third_sem_final['gp_com'] = (df1['CGPA_3rd'].values[0])
        third_sem_final['lg_com'] = (lg_cal(df1['CGPA_3rd'].values[0]))

        # print(third_sem_code, third_sem_gp, third_sem_lg, third_sem_cr, third_sem_final)
        for i in range(0, len(third_sem_code)):
            dict = {}
            dict['code'] = third_sem_code[i]
            dict['title'] = "nothing"
            dict['gp'] = third_sem_gp[i]
            dict['lg'] = third_sem_lg[i]
            dict['cr'] = third_sem_cr[i]
            third_sem_full.append(dict)

    except:
        print("no result for sem 3")

    try:
        # 4th semester
        df = pd.read_excel(staticfiles_storage.path('data/Q_CGPA_4th.xlsx'))
        idx = df.columns
        df1 = df.loc[df[idx[1]] == reg]
        name = df1[idx[2]].values[0]
    

        fourth_sem_code = []
        fourth_sem_lg = []
        fourth_sem_gp = []
        fourth_sem_cr = []

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
            
        fourth_sem_final['cr_cur'] = (df1['T_Credit'].values[0])
        fourth_sem_final['gp_cur'] = (df1['GPA_4th'].values[0])
        fourth_sem_final['lg_cur'] = (lg_cal(df1['GPA_4th'].values[0]))
        fourth_sem_final['cr_com'] = (df1['Total_Credit'].values[0])
        fourth_sem_final['gp_com'] = (df1['CGPA'].values[0])
        fourth_sem_final['lg_com'] = (lg_cal(df1['CGPA'].values[0]))

        # print(fourth_sem_code, fourth_sem_gp, fourth_sem_lg, fourth_sem_cr, fourth_sem_final)
        for i in range(0, len(fourth_sem_code)):
            dict = {}
            dict['code'] = fourth_sem_code[i]
            dict['title'] = "nothing"
            dict['gp'] = fourth_sem_gp[i]
            dict['lg'] = fourth_sem_lg[i]
            dict['cr'] = fourth_sem_cr[i]
            fourth_sem_full.append(dict)
    except:
        print("no result for sem 4")

    try:
        # 5th semester
        df = pd.read_excel(staticfiles_storage.path('data/Q_CGPA_5th.xlsx'))
        idx = df.columns
        df1 = df.loc[df[idx[1]] == reg]
        name = df1[idx[2]].values[0]
    

        fifth_sem_code = []
        fifth_sem_lg = []
        fifth_sem_gp = []
        fifth_sem_cr = []

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
            
        fifth_sem_final['cr_cur'] = (df1['T_Credit'].values[0])
        fifth_sem_final['gp_cur'] = (df1['GPA_5th'].values[0])
        fifth_sem_final['lg_cur'] = (lg_cal(df1['GPA_5th'].values[0]))
        fifth_sem_final['cr_com'] = (df1['Credit_1st_5th'].values[0])
        fifth_sem_final['gp_com'] = (df1['CGPA_5th'].values[0])
        fifth_sem_final['lg_com'] = (lg_cal(df1['CGPA_5th'].values[0]))

        # print(fifth_sem_code, fifth_sem_gp, fifth_sem_lg, fifth_sem_cr, fifth_sem_final)
        for i in range(0, len(fifth_sem_code)):
            dict = {}
            dict['code'] = fifth_sem_code[i]
            dict['title'] = "nothing"
            dict['gp'] = fifth_sem_gp[i]
            dict['lg'] = fifth_sem_lg[i]
            dict['cr'] = fifth_sem_cr[i]
            fifth_sem_full.append(dict)
    except:
        print("no res for sem 5\n")

    try:
        # 6th semester
        df = pd.read_excel(staticfiles_storage.path('data/Q_CGPA_6th.xlsx'))
        idx = df.columns
        df1 = df.loc[df[idx[1]] == reg]
        name = df1[idx[2]].values[0]
    

        sixth_sem_code = []
        sixth_sem_lg = []
        sixth_sem_gp = []
        sixth_sem_cr = []

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

        sixth_sem_final['cr_cur'] = (df1['T_Credit'].values[0])
        sixth_sem_final['gp_cur'] = (df1['GPA_6th'].values[0])
        sixth_sem_final['lg_cur'] = (lg_cal(df1['GPA_6th'].values[0]))
        sixth_sem_final['cr_com'] = (df1['Total_Credit'].values[0])
        sixth_sem_final['gp_com'] = (df1['CGPA_6th'].values[0])
        sixth_sem_final['lg_com'] = (lg_cal(df1['CGPA_6th'].values[0]))

        # print(sixth_sem_code, sixth_sem_gp, sixth_sem_lg, sixth_sem_cr, sixth_sem_final)
        for i in range(0, len(sixth_sem_code)):
            dict = {}
            dict['code'] = sixth_sem_code[i]
            dict['title'] = "nothing"
            dict['gp'] = sixth_sem_gp[i]
            dict['lg'] = sixth_sem_lg[i]
            dict['cr'] = sixth_sem_cr[i]
            sixth_sem_full.append(dict)
    except:
        print("no res for sem 6\n")

    try:
        # 7th semester
        df = pd.read_excel(staticfiles_storage.path('data/Q_CGPA_7th.xlsx'))
        idx = df.columns
        df1 = df.loc[df[idx[1]] == reg]
        name = df1[idx[2]].values[0]
    

        seventh_sem_code = []
        seventh_sem_lg = []
        seventh_sem_gp = []
        seventh_sem_cr = []

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

        seventh_sem_final['cr_cur'] = (df1['T_Credit'].values[0])
        seventh_sem_final['gp_cur'] = (df1['GPA_7th'].values[0])
        seventh_sem_final['lg_cur'] = (lg_cal(df1['GPA_7th'].values[0]))
        seventh_sem_final['cr_com'] = (df1['Total_Credit'].values[0])
        seventh_sem_final['gp_com'] = (df1['CGPA_7th'].values[0])
        seventh_sem_final['lg_com'] = (lg_cal(df1['CGPA_7th'].values[0]))

        # print(seventh_sem_code, seventh_sem_gp, seventh_sem_lg, seventh_sem_cr, seventh_sem_final)
        for i in range(0, len(seventh_sem_code)):
            dict = {}
            dict['code'] = seventh_sem_code[i]
            dict['title'] = "nothing"
            dict['gp'] = seventh_sem_gp[i]
            dict['lg'] = seventh_sem_lg[i]
            dict['cr'] = seventh_sem_cr[i]
            seventh_sem_full.append(dict)

    except:
        print("no res for sem 7")

    try:
        # 8th semester
        df = pd.read_excel(staticfiles_storage.path('data/Q_CGPA_8th.xlsx'))
        idx = df.columns
        df1 = df.loc[df[idx[1]] == reg]
        name = df1[idx[2]].values[0]
    

        eighth_sem_code = []
        eighth_sem_lg = []
        eighth_sem_gp = []
        eighth_sem_cr = []

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

        eighth_sem_final['cr_cur'] = (df1['T_Credit'].values[0])
        eighth_sem_final['gp_cur'] = (df1['GPA_8th'].values[0])
        eighth_sem_final['lg_cur'] = (lg_cal(df1['GPA_8th'].values[0]))
        eighth_sem_final['cr_com'] = (df1['Total_Credit'].values[0])
        eighth_sem_final['gp_com'] = (df1['CGPA_8th'].values[0])
        eighth_sem_final['lg_com'] = (lg_cal(df1['CGPA_8th'].values[0]))

        # print(eighth_sem_code, eighth_sem_gp, eighth_sem_lg, eighth_sem_cr, eighth_sem_final)
        for i in range(0, len(eighth_sem_code)):
            dict = {}
            dict['code'] = eighth_sem_code[i]
            dict['title'] = "nothing"
            dict['gp'] = eighth_sem_gp[i]
            dict['lg'] = eighth_sem_lg[i]
            dict['cr'] = eighth_sem_cr[i]
            eighth_sem_full.append(dict)
    except:
        print("no res for sem 8")

    try:
        # 8th semester extra
        df = pd.read_excel(staticfiles_storage.path('data/Q_CGPA_8th Repeat.xlsx'))
        idx = df.columns
        df1 = df.loc[df[idx[1]] == reg]
        name = df1[idx[2]].values[0]
    

        eight_extra_sem_code = []
        eight_extra_sem_lg = []
        eight_extra_sem_gp = []
        eight_extra_sem_cr = []

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

        eighth_sem_re_final['cr_cur'] = (df1['T_Credit'].values[0])
        eighth_sem_re_final['gp_cur'] = (df1['GPA_8th'].values[0])
        eighth_sem_re_final['lg_cur'] = (lg_cal(df1['GPA_8th'].values[0]))
        eighth_sem_re_final['cr_com'] = (df1['Total_Credit'].values[0])
        eighth_sem_re_final['gp_com'] = (df1['CGPA_8th'].values[0])
        eighth_sem_re_final['lg_com'] = (lg_cal(df1['CGPA_8th'].values[0]))

        # print(eight_extra_sem_code, eight_extra_sem_gp, eight_extra_sem_lg, eight_extra_sem_cr, eight_extra_sem_final)
        for i in range(0, len(eight_extra_sem_code)):
            dict = {}
            dict['code'] = eight_extra_sem_code[i]
            dict['title'] = "nothing"
            dict['gp'] = eight_extra_sem_gp[i]
            dict['lg'] = eight_extra_sem_lg[i]
            dict['cr'] = eight_extra_sem_cr[i]
            eighth_sem_re_full.append(dict)
    except:
        print("no res for sem 8 ex")

    context = {
        "name" : name,
        "reg" : reg,
        "session" : "2015-16",
        "year" : "2016",
        "h1" : "held1",
        "h2" : "held2", 
        "h3" : "held3", 
        "h4" : "held4", 
        "h5" : "held5", 
        "h6" : "held6", 
        "h7" : "held7", 
        "h8" : "held8", 
        "sem1" : first_sem_full,
        "sem1_final" : first_sem_final,
        "sem2" : second_sem_full,
        "sem2_final" : second_sem_final,
        "sem3" : third_sem_full,
        "sem3_final" : third_sem_final,
        "sem4" : fourth_sem_full,
        "sem4_final" : fourth_sem_final,
        "sem5" : fifth_sem_full,
        "sem5_final" : fifth_sem_final,
        "sem6" : sixth_sem_full,
        "sem6_final" : sixth_sem_final,
        "sem7" : seventh_sem_full,
        "sem7_final" : seventh_sem_final,
        "sem8" : eighth_sem_full,
        "sem8_final" : eighth_sem_final,
        "sem8_ex" : eighth_sem_re_full,
        "sem8_ex_final" : eighth_sem_re_final,
    }
    print(context['sem8_final'])
    return render (request, 'index.html', context)


def search(request):
    return render (request, 'search.html')