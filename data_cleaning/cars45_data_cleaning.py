#import libraries
import pandas as pd
import numpy as np
import re

cars_df = pd.read_csv('./webscraping/cars_data.csv')

def clean_data():
    cars_df.columns = ['make', 'mileage(Km)', 'year', 'condition', 'price(₦)']
    for column in cars_df.columns:
        if column == 'make':
            cars_df[column]= cars_df[column].replace(regex=True,to_replace=' ', value = r'').replace(regex=True,to_replace=r'[1-3][0-9]{3}',value=r'')
        elif column == 'mileage(Km)':
            #remove unwanted characters and white spaces in mileage column
            cars_df['mileage(Km)'] = cars_df['mileage(Km)'].replace(regex=True,to_replace=r'\r''\n',value=r'').replace(regex=True,to_replace=r',',value=r'').replace(regex=True,to_replace=r' ',value=r'').replace(regex=True,to_replace=r'Km',value=r'')
        elif column == 'year':
            #remove unwanted characters and white spaces in year column
            cars_df['year'] = cars_df['year'].replace(regex=True,to_replace=r'\r''\n',value=r'').replace(regex=True,to_replace=' ', value = r'')
            #drop rows without year values
            cars_df.drop(cars_df.index[list(
                map(lambda x: x.startswith('N'), cars_df['year']))], inplace=True)
        elif column == 'condition':
            #remove unwanted characters and white spaces in price column
            cars_df['condition'] = cars_df['condition'].replace(regex=True,to_replace=' ',value=r'').replace(regex=True,to_replace='  ', value = r'')
            
        elif column == 'price(₦)':
            #remove unwanted characters and white spaces in price column
            cars_df['price(₦)'] = cars_df['price(₦)'].replace(regex=True,to_replace=r'\r''\n',value=r'').replace(regex=True,to_replace='                                                                            ', value = r'').replace(regex=True,to_replace=',', value = r'').replace(regex=True,to_replace=' ', value = r'')
            
        else:
            column
            
            
if __name__ == "__main__":
    clean_data()
    cars_df.to_csv('cars45_car_data.csv', index=False)
    # 1 80