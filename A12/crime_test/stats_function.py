import pandas as pd
def calculate_mean_and_median(df):
    
    if 'Vict Age' not in df.columns:
        raise ValueError("Missing 'Vict Age' column")

    
    numeric_data = pd.to_numeric(df['Vict Age'], errors='coerce')
    valid_data = numeric_data.dropna()

    if valid_data.empty:
        raise ValueError("No valid numeric data in 'Vict Age'")

    mean = valid_data.mean()
    median = valid_data.median()
    return mean, median


