from django.shortcuts import render
from django.http import HttpResponse
import datetime
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


def gen (df, reg, credit_list, title_list):
    sem_full = []
    sem_final = {}
    idx = df.columns
    df1 = df.loc[df[idx[1]] == reg]
    name = df1[idx[2]].values[0]

    # 1st semester
    sem_code = []
    sem_lg = []
    sem_gp = []
    for i in range(1, len(idx)):
        raw = idx[i].split("_")
        if raw[0] != 'GP':
            continue
        if (str(df1[idx[i]].values[0]) == 'nan'):
            continue
        st = raw[1]
        a = ""
        b = ""
        for c in st:
            if c >= 'A' and c <= 'Z':
                a = a + c
            elif c >= '0' and c <= '9':
                b = b + c
        st1 = a + " " + b
        # print(st1)
        sem_code.append(st1)
        sem_gp.append(df1[idx[i]].values[0])
        sem_lg.append(df1[idx[i + 1]].values[0])

        # sem_cr.append(df1[idx[i + 2]].values[0])
    sem_final['cr_cur'] = (df1['Credit'].values[0])
    sem_final['gp_cur'] = (df1['GPA'].values[0])
    sem_final['lg_cur'] = (lg_cal(df1['GPA'].values[0]))
    sem_final['cr_com'] = (df1['CCredit'].values[0])
    sem_final['gp_com'] = (df1['CGPA'].values[0])
    sem_final['lg_com'] = (lg_cal(df1['CGPA'].values[0]))
    # print(sem_code, sem_gp, sem_lg, sem_cr, sem_final)
    for i in range(0, len(sem_code)):
        dict = {}
        dict['code'] = sem_code[i]
        if sem_code[i] in title_list:
            dict['title'] = title_list[sem_code[i]]
        else: 
            dict['title'] = "nothing"
        dict['gp'] = sem_gp[i]
        dict['lg'] = sem_lg[i]
        if sem_code[i] in credit_list:
            dict['cr'] = credit_list[sem_code[i]]
        else:
            dict['cr'] = "nan"
        sem_full.append(dict)
    ret = {}
    ret['sem_full'] = sem_full
    ret['sem_final'] = sem_final
    ret['name'] = name
    return ret


def gradesheet(request):
    
    files = os.listdir(staticfiles_storage.path('data'))
    # print(files)
    title = pd.read_excel(staticfiles_storage.path('data/courses.xlsx'))
    # print(title)
    title_list = {}
    credit_list = {}
    for i in range(0, title.shape[0]):
        title_list[title.iloc[i]['Code']] = title.iloc[i]['Title']
        credit_list[title.iloc[i]['Code']] = title.iloc[i]['Credit']

    try:
        reg = request.GET['reg']
        reg = int(reg)
        name = ""
        # reg = 2015331503
        all = []
        try:
            for i in range(0, 8):
                df = pd.read_excel(staticfiles_storage.path('data/' + files[i]))
                # print(df)
                # print(df)
                ret = gen(df=df, reg=reg, credit_list=credit_list, title_list=title_list)
                # print(ret)
                name = ret['name']
                all.append(ret)
                # print(ret)
            extra = pd.read_excel(staticfiles_storage.path('data/' + files[8]))
            # print(extra)
            if extra.empty:
                ret = {}
                ret['sem_full'] = []
                ret['sem_final'] = []
                ret['name'] = ""
                all.append(ret)
            else:
                ret = gen(df=df, reg=reg, credit_list=credit_list, title_list=title_list)
                name = ret['name']
                all.append(ret)
            # print(all[8])
        except:
            print("No result found")

        held = pd.read_excel(staticfiles_storage.path('data/held.xlsx'))
        x = datetime.datetime.now()
        now = x.strftime("%d") + "-" + x.strftime("%b") + "-" + x.strftime("%y")
        context = {
            "name" : name,
            "reg" : reg,
            "session" : "2017-18",
            "year1" : "2018",	
            "year2" : "2018",	
            "year3" : "2019",	
            "year4" : "2019",	
            "year5" : "2020",	
            "year6" : "2020",	
            "year7" : "2021",	
            "year8" : "2021",	
            "year9" : "2021",
            "now" : now,
            "h1" : held.iloc[0]["Held"],
            "h2" : held.iloc[1]["Held"], 
            "h3" : held.iloc[2]["Held"], 
            "h4" : held.iloc[3]["Held"], 
            "h5" : held.iloc[4]["Held"], 
            "h6" : held.iloc[5]["Held"],  
            "h7" : held.iloc[6]["Held"],  
            "h8" : held.iloc[7]["Held"], 
            "h8_ex" : held.iloc[8]["Held"],  
            "sem1" : all[0]['sem_full'],
            "sem1_final" : all[0]['sem_final'],
            "sem2" : all[1]['sem_full'],
            "sem2_final" : all[1]['sem_final'],
            "sem3" : all[2]['sem_full'],
            "sem3_final" : all[2]['sem_final'],
            "sem4" : all[3]['sem_full'],
            "sem4_final" : all[3]['sem_final'],
            "sem5" : all[4]['sem_full'],
            "sem5_final" : all[4]['sem_final'],
            "sem6" : all[5]['sem_full'],
            "sem6_final" : all[5]['sem_final'],
            "sem7" : all[6]['sem_full'],
            "sem7_final" : all[6]['sem_final'],
            "sem8" : all[7]['sem_full'],
            "sem8_final" : all[7]['sem_final'],
            "sem8_ex" : all[8]['sem_full'],
            "sem8_ex_final" : all[8]['sem_final'],
        }
        return render (request, 'index.html', context)
    except:
        return render (request, 'search.html', {"err":"Please enter a valid registration."})
    

def search(request):
    return render(request, 'search.html')