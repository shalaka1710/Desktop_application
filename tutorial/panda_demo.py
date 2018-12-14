import pandas as pd
import matplotlib.pyplot as plt

web_history={'day': [1,2,4,5],'bouns_rate':[12,2,3,2],'visitor':[100,33,3,3]}
df = pd.DataFrame(web_history)
print(df)
print(df.head(2)) # first 2 rows
print("Last twe rows :",df.tail(2)) # last 2 rows

# merging
df1 = pd.DataFrame({"HPI":[4,5,61,7],"int1":[23,23,23,23],"check":[23,45,33,22]},
                        index = [2001,2002,2003,2004])

df2 = pd.DataFrame({"HPI":[4,5,61,7],"int":[23,23,23,23],"check":[23,45,33,22]},
                          index = [2001,2002,2003,2006])

#merge=pd.merge(df1,df2,on="check")
#print(merge)

df1 = pd.DataFrame({"HPI_df1":[4,5,61,7],"int_df1":[23,23,23,23],"check_df1":[23,45,33,22]},
                        index = [2001,2002,2003,2004])

df2 = pd.DataFrame({"HPI_df2":[4,5,61,7],"int_df2":[23,23,23,23],"check_df2":[23,45,33,22]},
                          index = [2001,2002,2003,2006])

join = df1.join(df2)
print(join)

df3 = pd.DataFrame({"HPI":[4,5,61,7],"int":[23,23,23,23],"check":[23,45,33,22]},
                          index = [2001,2002,2003,2006])
print(df3.set_index("check"))
#print(df3.set_index("check" inplace="true"))
df3.plot()
plt.show()

df3 = df3.rename(columns={"check":"Users"})
print(df3)

cancat = pd.concat([df1,df2],sort=False)

print("Concatenation result is :: ",cancat)


# read csv File
csv_data = pd.read_csv("D:\demo_file.csv",index_col=0)
print("CSV Data :",csv_data)
csv_data.to_html('html_file.html')

data_frame1 =pd.DataFrame(csv_data)
print("csv data from data frame",data_frame1)
data_frame1.plot()
plt.show()
