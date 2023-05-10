import pandas as pd
localtemp=9
def make_data_frame(data1,data2,dates):
    s1=pd.Series(data1,name='source1_val')
    s2=pd.Series(data2,name='source2_val')
    s3=pd.Series(dates,name='dates')
    df=pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
    return df 
# ndf=make_data_frame([1,2,3],[4,5,6],['23','22','21'])

# ndf.to_csv('result_of_script.csv',index=False)
# data=pd.read_csv('result_of_script.csv')
# print(data)