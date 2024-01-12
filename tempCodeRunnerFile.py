import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/ayesh/Downloads/Employee data.csv") #print(df)
df.plot(kind="hist")
plt.title('DISTRIBUTION OF SALARIES')
plt.show()  #show the plot
#or
df_can = df.drop(df.columns[[0,2,3,4,6,7,8,9]], axis=1)
# print(df_can.head())
df_can.plot(kind="hist")
plt.title("DIstribution of Salaries based on GENDER")
plt.show()