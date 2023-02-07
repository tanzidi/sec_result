import pandas as pd
import numpy as np

reg = 2015331501

df = pd.read_excel('data/Q_GPA_1st.xlsx')
idx = df.columns

df1 = df.loc[df[idx[1]] == reg]
name = df1[idx[2]].values[0]
print(name)

# 1st semester
first_sem_code = []
first_sem_lg = []
first_sem_gp = []
first_sem_cr = []
first_sem_final = []
for i in range(4, len(idx), 4):
    first_sem_gp.append(df1[idx[i]].values[0])
    first_sem_lg.append(df1[idx[i + 1]].values[0])
    first_sem_cr.append(df1[idx[i + 2]].values[0])
    raw = idx[i].split("_")
    first_sem_code.append(raw[1])
    if (i >= 44):
        break
first_sem_final.append(df1['Credit_1st'].values[0])
first_sem_final.append(df1['GPA_1st'].values[0])
# first_sem_final.append(lg_cal(df1['GPA_1st'].values[0]))
first_sem_final.append(df1['Credit_1st'].values[0])
first_sem_final.append(df1['GPA_1st'].values[0])
# first_sem_final.append(lg_cal(df1['GPA_1st'].values[0]))

# print(first_sem_code, first_sem_gp, first_sem_lg, first_sem_cr, first_sem_final)


# 2nd semester
df = pd.read_excel('data/Q_GPA_2nd.xlsx')
idx = df.columns
df1 = df.loc[df[idx[1]] == reg]

second_sem_code = []
second_sem_lg = []
second_sem_gp = []
second_sem_cr = []
second_sem_final = []
for i in range(4, len(idx), 4):
    second_sem_gp.append(df1[idx[i]].values[0])
    second_sem_lg.append(df1[idx[i + 1]].values[0])
    second_sem_cr.append(df1[idx[i + 2]].values[0])
    raw = idx[i].split("_")
    second_sem_code.append(raw[1])
    if (i >= 36):
        break
second_sem_final.append(df1['Credit_2nd'].values[0])
second_sem_final.append(df1['GPA_2nd'].values[0])
# second_sem_final.append(lg_cal(df1['GPA_2nd'].values[0]))
second_sem_final.append(df1['Total_C'].values[0])
second_sem_final.append(df1['CGPA'].values[0])
# second_sem_final.append(lg_cal(df1['CGPA'].values[0]))

# print(second_sem_code, second_sem_gp, second_sem_lg, second_sem_cr, second_sem_final)


# 3rd semester
df = pd.read_excel('data/Q_CGPA_3rd.xlsx')
idx = df.columns
df1 = df.loc[df[idx[1]] == reg]

third_sem_code = []
third_sem_lg = []
third_sem_gp = []
third_sem_cr = []
third_sem_final = []
for i in range(3, len(idx), 3):
    if (str(df1[idx[i]].values[0]) == 'nan'):
        continue
    if (i == 36):
        i = 35
        continue
    if (i >= 65):
        break
    third_sem_gp.append(df1[idx[i]].values[0])
    third_sem_lg.append(df1[idx[i + 1]].values[0])
    third_sem_cr.append(df1[idx[i + 2]].values[0])
    raw = idx[i].split("_")
    third_sem_code.append(raw[1])
    
third_sem_final.append(df1['T_Credit'].values[0])
third_sem_final.append(df1['GPA_3rd'].values[0])
# third_sem_final.append(lg_cal(df1['GPA_3rd'].values[0]))
third_sem_final.append(df1['Credit_1st_3rd'].values[0])
third_sem_final.append(df1['CGPA_3rd'].values[0])
# third_sem_final.append(lg_cal(df1['CGPA_3rd'].values[0]))

# print(third_sem_code,"\n", third_sem_gp,"\n", third_sem_lg,"\n", third_sem_cr,"\n", third_sem_final)


# 4th semester
df = pd.read_excel('data/Q_CGPA_4th.xlsx')
idx = df.columns
df1 = df.loc[df[idx[1]] == reg]

fourth_sem_code = []
fourth_sem_lg = []
fourth_sem_gp = []
fourth_sem_cr = []
fourth_sem_final = []

# for i in range(4, len(idx), 4):
#     if (str(df1[idx[i]].values[0]) == 'nan'):
#         continue
#     print(idx[i])
#     if (i > 24):
#         break
#     fourth_sem_gp.append(df1[idx[i]].values[0])
#     fourth_sem_lg.append(df1[idx[i + 1]].values[0])
#     fourth_sem_cr.append(df1[idx[i + 2]].values[0])
#     raw = idx[i].split("_")
#     fourth_sem_code.append(raw[1])

for i in range(27, len(idx), 3):
    if (str(df1[idx[i]].values[0]) == 'nan'):
        continue
    print(idx[i])
    if (i >= 33):
        break
    fourth_sem_gp.append(df1[idx[i]].values[0])
    fourth_sem_lg.append(df1[idx[i + 1]].values[0])
    fourth_sem_cr.append(df1[idx[i + 2]].values[0])
    raw = idx[i].split("_")
    fourth_sem_code.append(raw[1])
fourth_sem_final.append(df1['T_Credit'].values[0])
fourth_sem_final.append(df1['GPA_4th'].values[0])
# fourth_sem_final.append(lg_cal(df1['GPA_4th'].values[0]))
fourth_sem_final.append(df1['Total_Credit'].values[0])
fourth_sem_final.append(df1['CGPA'].values[0])
# fourth_sem_final.append(lg_cal(df1['CGPA'].values[0]))

print(fourth_sem_code,"\n", fourth_sem_gp,"\n", fourth_sem_lg,"\n", fourth_sem_cr,"\n", fourth_sem_final)