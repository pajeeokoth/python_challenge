# Import Dependencies
import pandas as pd

# File to Load
bank_path = "Resources/budget_data.csv"

# Read the modified Comic Books csv and store into Pandas DataFrame
bank_df = pd.read_csv(bank_path, encoding='utf-8')

#rename the column Profit/Loss
bank_df.rename(columns={'Profit/Losses':'profit'}, inplace=True)

#calculate net profit or loss
net_profit = bank_df['profit'].sum()

#Count the number of months
net_profit_loss = bank_df['profit'].sum()
no_months = bank_df.shape[0]

#create a column in the dataframe to store the calculated change
bank_df['change'] = bank_df['profit'].diff(periods=1)

#Calculate the average profit/loss, the lagest and smallestchange 
average = round(bank_df['change'].mean(), 2)
largest = int(bank_df['change'].max())
smallest = int(bank_df['change'].min())
day1 = bank_df['Date'][79]
day2 = bank_df['Date'][49]

#print the output as required
print(f'Total Months: {no_months} \n Total: ${net_profit} \n Average Change: ${average} \n Greatest Increase in Profits: {day1} (${largest}) \n Greatest Decrease in Profits: {day2} (${smallest})')

#print results to txt file
with open('bank.txt', 'a') as f:
    print(f'Total Months: {no_months} \n Total: ${net_profit} \n Average Change: ${average} \n Greatest Increase in Profits: {day1} (${largest}) \n Greatest Decrease in Profits: {day2} (${smallest})', file=f)
