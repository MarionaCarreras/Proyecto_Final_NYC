import pandas as pd

def clean_311(input_path='data/raw/nyc_311_sample.csv', output_path='data/interim/nyc_311_cleaned.csv'):
    df = pd.read_csv(input_path, parse_dates=['created_date','closed_date'])
    df['time_to_close_days'] = (df['closed_date'] - df['created_date']).dt.days
    df['date'] = df['created_date'].dt.date
    df.to_csv(output_path, index=False)
    print('Cleaned data saved to', output_path)

if __name__=='__main__':
    clean_311()
