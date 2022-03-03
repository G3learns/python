import pandas as pd
import numpy as np
fil=pd.DataFrame({"Name":["aa","bb","cc"],"Salary":[10,20,30]})
print(fil.loc[1,"Name"])
print(fil.sort_index(axis=1,ascending=False))
print(fil.loc[1:3,["Name","Salary"]])
dt=pd.date_range('20200401',periods=10)
df=pd.DataFrame(np.random.randn(10,4),index=dt,columns=list('ABCD'))
print(df)