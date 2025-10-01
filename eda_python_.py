from src.cleaning import clean_311
from src.data_load import merge_weather
from src.eda_plots import generate_plots

if __name__=='__main__':
 clean_311(); merge_weather(); generate_plots()
