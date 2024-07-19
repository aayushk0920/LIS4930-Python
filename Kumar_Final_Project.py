import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the trading data file
def load_data(file_path):
    try:
        df = pd.read_excel(file_path, sheet_name=0, header=1)
        return df
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

# Convert columns to appropriate data types
def preprocess_data(df):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Entry Time'] = pd.to_datetime(df['Entry Time'], format='%H:%M', errors='coerce').dt.time
    df['Time to 15 pips (mins)'] = pd.to_numeric(df['Time to 15 pips (mins)'], errors='coerce')
    df['Drawdown Time (mins)'] = pd.to_numeric(df['Drawdown Time (mins)'], errors='coerce')
    df['4hr Bias'] = df['4hr Bias'].astype(str)
    df['1hr Bias'] = df['1hr Bias'].astype(str)
    return df

# Analysis functions
def analyze_profitability(df):
    profitable_entries = df[df['Win or Loss'] == 'Win']
    average_entry_time = profitable_entries['Entry Time'].apply(lambda x: x.hour * 60 + x.minute).mean()
    avg_entry_hours = average_entry_time // 60
    avg_entry_minutes = average_entry_time % 60
    return avg_entry_hours, avg_entry_minutes

def analyze_drawdown(df):
    return df['Drawdown Time (mins)'].mean()

def analyze_profitable_days(df):
    profitable_entries = df[df['Win or Loss'] == 'Win']
    profitable_days = profitable_entries['D.O.W'].value_counts()
    return profitable_days

def calculate_win_percentage(df):
    total_trades = len(df)
    total_wins = len(df[df['Win or Loss'] == 'Win'])
    return (total_wins / total_trades) * 100

def analyze_bias_alignment(df):
    df['Bias Alignment'] = (df['4hr Bias'] == df['1hr Bias'])
    alignment_win_rate = df[df['Bias Alignment'] & (df['Win or Loss'] == 'Win')].shape[0] / df[df['Bias Alignment']].shape[0] * 100
    non_alignment_win_rate = df[~df['Bias Alignment'] & (df['Win or Loss'] == 'Win')].shape[0] / df[~df['Bias Alignment']].shape[0] * 100
    return alignment_win_rate, non_alignment_win_rate

# Plotting functions
def plot_profitable_days(profitable_days):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=profitable_days.index, y=profitable_days.values, palette='viridis')
    plt.title('Number of Profitable Trades per Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Profitable Trades')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def plot_average_drawdown(df):
    plt.figure(figsize=(10, 6))
    average_drawdown_per_day = df.groupby('D.O.W')['Drawdown Time (mins)'].mean()
    sns.barplot(x=average_drawdown_per_day.index, y=average_drawdown_per_day.values, palette='viridis')
    plt.title('Average Drawdown Time per Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Drawdown Time (mins)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def plot_win_rate(alignment_win_rate, non_alignment_win_rate):
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

# Main function to run the analysis
def main():
    file_path = r'D:\Aayush School\Summer 2024\LIS 4930 Pyth\Trading Model Backtesting.xlsx'
    df = load_data(file_path)
    if df is not None:
        df = preprocess_data(df)

        avg_entry_hours, avg_entry_minutes = analyze_profitability(df)
        print(f"\nThe most profitable time to enter a trade is around {int(avg_entry_hours)}:{int(avg_entry_minutes):02d}.")

        avg_drawdown_time = analyze_drawdown(df)
        print(f"The average drawdown time of each trade is {avg_drawdown_time:.2f} minutes.")

        profitable_days = analyze_profitable_days(df)
        most_profitable_day = profitable_days.idxmax()
        print(f"The most profitable day of the week to enter a trade is {most_profitable_day}.")

        win_percentage = calculate_win_percentage(df)
        print(f"Win percentage: {win_percentage:.2f}%")

        average_time_in_trade = df['Time to 15 pips (mins)'].mean()
        print(f"Average time in a trade: {average_time_in_trade:.2f} minutes")

        proportion_more_than_15_pips = (df['Time to 15 pips (mins)'] > 15).mean() * 100
        print(f"The likelihood of achieving more than 15 pips per trade is {proportion_more_than_15_pips:.2f}%.")

        alignment_win_rate, non_alignment_win_rate = analyze_bias_alignment(df)
        print(f"\nWin rate when Biases are aligned: {alignment_win_rate:.2f}%")
        print(f"Win rate when Biases are not aligned: {non_alignment_win_rate:.2f}%")

        plot_profitable_days(profitable_days)
        plot_average_drawdown(df)
        plot_win_rate(alignment_win_rate, non_alignment_win_rate)

# Run the main function
if __name__ == "__main__":
    main()
