import pandas as pd
import numpy as np
import re

cars_df = pd.read_csv('./webscraping/cars_data.csv')

cars_df['price'] = cars_df['price'].replace(regex=True,to_replace=r'\r''\n',value=r'').replace(regex=True,to_replace='                                                                            ', value = r'').replace(regex=True,to_replace=',', value = r'').replace(regex=True,to_replace=' ', value = r'')

print(cars_df.head())