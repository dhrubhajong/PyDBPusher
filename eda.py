import pandas as pd
import numpy as np
import csv
import json
import warnings
warnings.filterwarnings('ignore')
import re
import matplotlib.pyplot as plt
import seaborn as sns

def extract(x):
    if x is np.nan:
        return np.nan
    else:
        x = re.sub(r'K', '000', x, flags=re.IGNORECASE)
        x = re.sub(r'[~ €, ^a-zA-Z !/ - + ₹]', "", str(x))
        return x

def clean_data(input_file_path,output_file_path):
    df=pd.read_csv(input_file_path)
    df['rating_count'] = df['rating_count'].apply(extract)
    df['cost_column']=df['cost_column'].apply(extract)
    df['cost_column']= df['cost_column'].fillna(df['cost_column'].median())
    df = df.dropna()
    df['rating_count']=df['rating_count'].astype('int64')
    df.to_json(output_file_path, orient='records')
    return df

df = clean_data('C:/Users/lenovo/Downloads/analytical/swiggy.csv', 'swiggy.json')

# sns.distplot(df['cost'])

# sns.boxplot(df.rating_count)

