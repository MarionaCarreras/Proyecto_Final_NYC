import pandas as pd, matplotlib.pyplot as plt

def generate_plots(final_csv='data/final/nyc_311_weather_final.csv'):
    df=pd.read_csv(final_csv, parse_dates=['created_date','closed_date'])
    daily=df.groupby('date').size()
    plt.figure(figsize=(10,4)); plt.plot(daily.index,daily.values); plt.title('Daily Incidents')
    plt.tight_layout(); plt.savefig('reports/figs/daily_incidents.png'); plt.close()
    top=df['complaint_type'].value_counts().head(10)
    plt.figure(figsize=(7,4)); top.sort_values().plot(kind='barh'); plt.title('Top Complaints')
    plt.tight_layout(); plt.savefig('reports/figs/top_complaints.png'); plt.close()

if __name__=='__main__':
    generate_plots()
