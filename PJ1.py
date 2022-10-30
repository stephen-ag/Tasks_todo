import pandas as pd
import os
import io
import xlsxwriter
from tkinter import filedialog
fpath = filedialog.askopenfilename()

df2 = pd.read_csv(fpath, skiprows=0)
print('Dataframe created')
df2 = df2[df2.filter(regex='^(?!Unnamed)').columns] 
print(df2)

dfp=df2.copy()


dfp.drop(dfp.columns[[0,1]], axis = 1, inplace = True)
#dfp.drop(['Load Steps'], axis = 1, inplace = True)
print('dropped')
print(dfp)

df4=dfp.values.tolist()  #!! this gets the list of I,C, O values
ser= pd.Series(df4)
#ser.columns = 'values'
dfff=pd.DataFrame(ser)
dfff.columns =['Load_steps']

dfa=df2.filter(['Load Steps','CMMx'])

print(dfff)
print(dfa)

dfa['Load_steps']=dfff
sort_df =dfa.explode('Load_steps') #!!!!! converts all values x,y,z to single column dataframe

maxValue = sort_df['Load Steps'].max()

col1=sort_df['CMMx']
col1.reset_index(inplace = True, drop = True)

##!!!! slicing into different sections
for i in range(1,maxValue+1):
  globals()["df_"+str(i)] = sort_df.loc[sort_df['Load Steps'] == i]
  globals()["df_"+str(i)].reset_index(inplace = True, drop = True)


dfadd = pd.concat([df_1,df_2,df_3,df_4,df_5,df_6,df_7,df_8,], axis = 'columns')

dfdata=dfadd.drop(['Load Steps','CMMx'], axis=1)

dfdata.columns =['LS1', 'LS2', 'LS3', 'LS4','LS5','LS6','LS7','LS8']

###pd.options.mode.chained_assignment = None ### will suppress the warning entirely, for a SettingWithCopyError!!!

dfdata['CMMX']=col1
pd.options.mode.chained_assignment = None
dfdata.set_index('CMMX', inplace=True)
      
print("  compilation complete !! refer to output file name First_Task_To.xlsx")
dfdata.to_excel('First_Task_To.xlsx')

   