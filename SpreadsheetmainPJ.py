import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

# Load the CSV file
file_path = 'sales.csv'
sales_data = pd.read_csv(file_path)
# Task 2: Collect all sales from each month into a single list
sales_list = sales_data['sales'].tolist()
# Task 3: Calculate the total sales across all months
total_sales = sum(sales_list)

#***************OUTPUT OF MONTHLY TOTAL SALES AS 'BAR PLOT'****************
# Ensure months are in correct chronological order
month_order = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
sales_data['month'] = pd.Categorical(sales_data['month'], categories=month_order, ordered=True)
# Sort data by month for proper plotting
sales_data = sales_data.sort_values('month')
# Set the figure size
plt.figure(figsize=(12, 8))
# Create a bar plot for sales by month, assigning x as both hue and x variable to get a color palette
bar_plot = sbn.barplot(x='month', y='sales', data=sales_data, palette='coolwarm', hue='month', legend=False)
# Add exact sales numbers on top of each bar
for index, row in sales_data.iterrows():
    bar_plot.text(index, row['sales'] + 100, f'{row["sales"]}', color='black', ha="center")
# Add labels and title
plt.title('Detailed Monthly Sales Data', fontsize=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales (in units)', fontsize=14)
# Customize the ticks for better readability
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# Show the grid for better visual clarity
plt.grid(axis='y', linestyle='--', alpha=0.7)
# Show the plot
plt.tight_layout()
plt.show()

#*************MONTHLY SALES PERCENTAGE IN PIE CHART*************
###PIE CHART###
df = pd.read_csv('sales.csv')
sales_col = df['sales']#choose specific Sales column
#Pie charts are created using with Matplotlib's plt.pie() function
labels = 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
#autopct=A string or function used to generate labels inside the wedges 'showing their numeric value as percentage'.
#pctdistance= control the distance of the percents and
#labeldistance= control the distance of the labels from the center of the pie
plt.figure(figsize=(8, 8))
plt.pie(sales_col, labels=labels, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.03)
plt.title("Monthly Sales as PIE chart",weight='bold')
plt.show()
#************EXTENSIONS*******************************************************
#****EXTENSION-- MONTHS WITH HIGHEST & LOWEST SALES**************************
# Convert the data to a Pandas DataFrame
sales_data1 = pd.read_csv(file_path)
df_salesinmonth = pd.DataFrame(sales_data1)
#Reading & Displaying month and sales data of dataframe
monthly_sales =df_salesinmonth[['month','sales']]
#Set the DataFrame index using existing columns ie display dataframe of month and sales without index.
monthly_salesOP=monthly_sales.set_index(['month'],inplace=False,drop=True)
# loc() : Locating the month with the highest and lowest sales  and
# idxmax() and idxmin() : return the row label of max and min values
min_sales_month = monthly_sales.loc[monthly_sales['sales'].idxmin()]
max_sales_month = monthly_sales.loc[monthly_sales['sales'].idxmax()]

#******EXTENSION -- MONTHLY CHANGE AS PERCENTAGE % & THE AVERAGE CALCULATION **********
#*******EXTENSION = Monthly changes as a Percentage *****************************
sales_col = df['sales']#choose specific Sales column
#load sales data into a DataFrame object and assign it to variable : df:
df_sales=pd.DataFrame(sales_col)
#The pct_change() method returns a DataFrame with the percentage difference between
# the two consecutive row values
df_percentagechange= df_sales.pct_change()
#********EXTENSION--CALCULATING AVERAGE AND ROUNDING*******************************
df_avg= pd.read_csv('sales.csv')
avg = df_avg['sales'].mean()
##Rounding the Average to 2 decimal places
rounding_avg = round(df_avg['sales'].mean(),2)
#********RESULTS IN CSV SPREADSHEET*******************
with open('result.csv', 'w') as op_csv:
    op_csv.write('******Result of SPREADSHEET ANALYSIS PROJECT******************')
    op_csv.write(f'\nSales from each month :\n{monthly_salesOP}')
    op_csv.write('\n************************************')
    op_csv.write(f'\nSales from each month as a list :\n{sales_list}')
    op_csv.write('\n************************************')
    op_csv.write(f'\nTotal Sales : {total_sales}')
    op_csv.write('\n************************************')
    op_csv.write(f'\nMinimum Sales Month :\n{str(min_sales_month)}')
    op_csv.write('\n************************************')
    op_csv.write(f'\nMaximum Sales Month :\n{str(max_sales_month)}')
    op_csv.write('\n************************************')
    op_csv.write(f'\nSales Average: {avg}')
    op_csv.write('\n************************************')
    op_csv.write(f'\nAverage rounded to 2 decimal places: {rounding_avg}')
    op_csv.write('\n************************************')
    op_csv.write(f'\nMonthly change as Percentage:\n{str(df_percentagechange)}')
    op_csv.write('\n************************************')
    op_csv.write('\n******THANK YOU**********')

