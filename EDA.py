import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r'C:/Users/91981/Desktop/projects/EDA/Python_Diwali_Sales_Analysis-main/Python_Diwali_Sales_Analysis-main/Diwali Sales Data.csv' , encoding='latin-1')
print(df.shape)
print(df.head(10))
print(df.info())
df.drop(['Status' , 'unnamed1'], axis=1, inplace=True) #inplace is used to save those values
print(df.info())
print(pd.isnull(df)) #give false values
print(pd.isnull(df).sum())
df.dropna(inplace=True)
print(pd.isnull(df).sum())


#df['Status']=df['Status'].astype('int') #it will show error because it is removed
#print(df['Status'])

df['Amount']=df['Amount'].astype('int') #astype function is used to change the data type
print(df['Amount'])
print(df.columns)
#rename columns
df.rename(columns = {'Cust_name':'customer'} , inplace=True)
print(df.columns)
#describe function describe the mathematical functions of all numeric columns in data frame
print(df.describe())

#to describe for particular columns
print(df[['Age','Orders','Amount']].describe())

#EXPLORATORY DATA ANALYSIS (EDA)
#sns is seaborn
#we have to make a countplot i.e it will count

#GENDER

ax = sns.countplot(x = 'Gender', data = df)
for bars in ax.containers:
    print(ax.bar_label(bars))
    plt.show()

#groupby us used to split the dataframe into groups based on one or more columns
#groupby creates subgroups for each unique value 
#as_index represents orignal data frames columns are preserved
#sum will give the total amount of men and women here

result = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
print(result)
sns.barplot(x = 'Gender', y='Amount', data = result)
plt.show()

#AGE
sns.countplot(x = 'Age Group', data = df)
plt.show() 

#if we want to know how many male and femaile in each category we can add hue = 'Gender' in above line of code
ax = sns.countplot(x = 'Age Group', data = df, hue ='Gender')
for bars in ax.containers:
    print(ax.bar_label(bars))
    plt.show()

age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
print(age)
sns.barplot(x = 'Age Group', y='Amount', data = age)
plt.show()

#Now we want to state wise order
#STATE
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False) #to show value of 10 states add head(10)
print(sales_state)
#to show data correctly statewise
sns.set(rc={'figure.figsize':(5,25)})
#15 is width and 5 is height

sns.barplot(x = 'Orders', y='State', data=sales_state)
plt.show()

#MARITAL STATUS
sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')
plt.show()

#OCCUPATION
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)
    plt.show()
plt.show()
#PRODUCT CATEGORY
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Amount',y= 'Product_Category')
plt.show()
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')
plt.show()


