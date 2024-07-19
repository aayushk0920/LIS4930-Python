import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the trading data file
file_path = r'D:\Aayush School\Summer 2024\LIS 4930 Pyth\Trading Model Backtesting.xlsx'

try:
    #Read the Excel file with the correct header row
    df = pd.read_excel(file_path, sheet_name=0, header=1)  # Adjust header if necessary

    #Print column names to verify
    print("Columns in DataFrame:")
    print(df.columns)

    #Display the first few rows to understand the structure of the data
    print("\nInitial Data:")
    print(df.head())

    #Convert relevant columns to the appropriate data types
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Entry Time'] = pd.to_datetime(df['Entry Time'], format='%H:%M', errors='coerce').dt.time
    df['Time to 15 pips (mins)'] = pd.to_numeric(df['Time to 15 pips (mins)'], errors='coerce')
    df['Drawdown Time (mins)'] = pd.to_numeric(df['Drawdown Time (mins)'], errors='coerce')
    df['4hr Bias'] = df['4hr Bias'].astype(str)  # Ensure Bias columns are strings
    df['1hr Bias'] = df['1hr Bias'].astype(str)

    #Analysis: Most profitable time to enter a trade
    profitable_entries = df[df['Win or Loss'] == 'Win']
    average_entry_time = profitable_entries['Entry Time'].apply(lambda x: x.hour * 60 + x.minute).mean()
    average_entry_time_hours = average_entry_time // 60
    average_entry_time_minutes = average_entry_time % 60

    print(f"\nThe most profitable time to enter a trade is around {int(average_entry_time_hours)}:{int(average_entry_time_minutes):02d}.")

    #Analysis: Average drawdown time
    average_drawdown_time = df['Drawdown Time (mins)'].mean()
    print(f"The average drawdown time of each trade is {average_drawdown_time:.2f} minutes.")

    #Analysis: Most profitable day of the week
    profitable_days = profitable_entries['D.O.W'].value_counts()
    most_profitable_day = profitable_days.idxmax()

    print(f"The most profitable day of the week to enter a trade is {most_profitable_day}.")

    #Win percentage
    total_trades = len(df)
    total_wins = len(profitable_entries)
    win_percentage = (total_wins / total_trades) * 100
    print(f"Win percentage: {win_percentage:.2f}%")

    #Average time in a trade (assuming 'Time to 15 pips (mins)' represents time in trade)
    average_time_in_trade = df['Time to 15 pips (mins)'].mean()
    print(f"Average time in a trade: {average_time_in_trade:.2f} minutes")

    #Likelihood of achieving more than 15 pips per trade
    trades_more_than_15_pips = df['Time to 15 pips (mins)'] > 15
    proportion_more_than_15_pips = trades_more_than_15_pips.mean() * 100
    print(f"The likelihood of achieving more than 15 pips per trade is {proportion_more_than_15_pips:.2f}%.")

    #Determine alignment of Biases
    df['Bias Alignment'] = (df['4hr Bias'] == df['1hr Bias'])

    #Calculate win rates based on Bias alignment
    alignment_win_rate = df[df['Bias Alignment'] & (df['Win or Loss'] == 'Win')].shape[0] / df[df['Bias Alignment']].shape[0] * 100
    non_alignment_win_rate = df[~df['Bias Alignment'] & (df['Win or Loss'] == 'Win')].shape[0] / df[~df['Bias Alignment']].shape[0] * 100

    print(f"\nWin rate when Biases are aligned: {alignment_win_rate:.2f}%")
    print(f"Win rate when Biases are not aligned: {non_alignment_win_rate:.2f}%")

except UnicodeDecodeError as e:
    print("A UnicodeDecodeError occurred:", e)
except Exception as e:
    print("An error occurred:", e)

#Plotting
#Bar plot for the most profitable days of the week
plt.figure(figsize=(10, 6))
profitable_days = profitable_entries['D.O.W'].value_counts()
sns.barplot(x=profitable_days.index, y=profitable_days.values, palette='viridis')
plt.title('Number of Profitable Trades per Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Profitable Trades')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

#Bar plot for average drawdown time per day of the week
plt.figure(figsize=(10, 6))
average_drawdown_per_day = df.groupby('D.O.W')['Drawdown Time (mins)'].mean()
sns.barplot(x=average_drawdown_per_day.index, y=average_drawdown_per_day.values, palette='viridis')
plt.title('Average Drawdown Time per Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Drawdown Time (mins)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

#Bar plot for win rate based on Bias alignment
plt.figure(figsize=(8, 6))
alignment_win_rates = {
    'Bias Aligned': alignment_win_rate,
    'Bias Not Aligned': non_alignment_win_rate
}
sns.barplot(x=list(alignment_win_rates.keys()), y=list(alignment_win_rates.values()), palette='viridis')
plt.title('Win Rate Based on Bias Alignment')
plt.xlabel('Bias Alignment')
plt.ylabel('Win Rate (%)')
plt.ylim(0, 100)
plt.grid(True)
plt.show()
