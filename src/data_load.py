import pandas as pd

def merge_weather(incidents_file='data/interim/nyc_311_cleaned.csv', weather_file='data/raw/nyc_weather_sample.csv', output_file='data/final/nyc_311_weather_final.csv'):
    df = pd.read_csv(incidents_file, parse_dates=['created_date','closed_date'])
    weather = pd.read_csv(weather_file, parse_dates=['date'])
    df['date'] = pd.to_datetime(df['date']).dt.date
    weather['date'] = weather['date'].dt.date
    merged = df.merge(weather, on='date', how='left')
    merged['temp_avg']=(merged['tmin']+merged['tmax'])/2
    merged['rainy_day']=(merged['precipitation']>0.2).astype(int)
    merged.to_csv(output_file, index=False)
    print('Final dataset saved to', output_file)

if __name__=='__main__':
    merge_weather()
