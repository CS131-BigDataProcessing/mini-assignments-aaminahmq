import pandas as pd
def validate_vict_age(df):
    
    if 'Vict Age' not in df.columns:
        raise ValueError("Missing 'Vict Age' column")

    
    numeric_data = pd.to_numeric(df['Vict Age'], errors='coerce')

    if numeric_data.isnull().any():
        raise TypeError("Non-numeric values found in 'Vict Age' column")

    valid = (numeric_data >= 1) & (numeric_data <= 100)
    return valid.all()

def validate_vict_sex(df):
    
    if 'Vict Sex' not in df.columns:
        raise ValueError("Missing 'Vict Sex' column")
    valid = df['Vict Sex'].isin(['M', 'F'])
    return valid.all()

