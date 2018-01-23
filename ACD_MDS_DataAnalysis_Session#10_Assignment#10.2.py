# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 08:11:59 2018

@author: HP
"""
import pandas as pd
def count_diff(inp_arr):
    global z 
    z = 0
    leninp = len(inp_arr)
    out_arr = [0] * leninp
    for i in range(leninp):
        diff = 0
        for j in range (i, -1, -1):
            z = j
            diff = diff + 1
            if (inp_arr[j] == 0):
                break;
        if (z == 0):
            out_arr[i] = i + 1
        else:    
            out_arr[i] = diff - 1
    return(out_arr)
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
X_arr = df['X'] 
x_arr = df['X']
Y_arr = count_diff(X_arr)
df['X'] = x_arr
df['Y'] = Y_arr
print(df)