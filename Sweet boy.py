import pandas as pd

print("---- Part 1: Pandas Series -----")
scores = [98500, 87000, 92000, 100000, 75000]
players = pd.Series(scores, index=['Snow_bundas', 'Bunnychow_cartel', ' Starbl@ze', 'Ner_MAchine567', 'Bopsy'])
print(players)

print()
print("---- Part 2: Pandas DataFrame -----")
data = {
    'Player': ['Snow_bundas', 'Bunnychow_cartel', ' Starbl@ze', 'Nerd_MAchine567', 'Bopsy'],
    'Level': [45, 38, 42, 50, 30],
    'Score': [98500, 87000, 92000, 100000, 75000],
    'Wins': [150, 120, 130, 200, 80]
}
df = pd.DataFrame(data)
print(df)

print()
print('---- Part 3: Accessing rows -----')
print("Row 0 (top player): ")
print(df.loc[0])
print()
print('Row 2 and 3:')
print(df.loc[2:3])

print("---- Part 4: Accessing columns -----")
full_df = pd.read_csv('Leaderboard.csv')
print('First 5 rows (Head):')
print(full_df.head())
print()
print("dataset info:")
print(full_df.info())

print()
print("---- Part 5: Cleaning Data -----")
print("Rows with misssing values removed (dropna):")
clean_df = full_df.dropna()
print(clean_df.to_string())
print()
print("Rows with missing values filled with 0 (fillna):")
filled_df = full_df.fillna(0)
print(filled_df.to_string())