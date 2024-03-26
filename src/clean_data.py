import pandas as pd
import numpy as np

def clean_data(save='data/processed/cleaned_data.csv'):
    # Read merged data and clean the data
    # Save cleaned data into {save}
    # Default saved in data/processed/cleaned_data.csv
    # Make sure merged data has been saved in data/processed/merged_data.csv

    merged_data = pd.read_csv('data/processed/merged_data.csv')

    # Drop 'unknown', '-'
    drop_unknown_data = merged_data[~(merged_data == 'unknown').any(axis=1)]
    drop_unknown_data = drop_unknown_data[drop_unknown_data['Theaters'] != '-']

    # Drop NaN
    drop_na_data = drop_unknown_data.dropna()

    # Select columns we are interested in 
    columns = ['Release', 'Gross', 'Theaters', 'openingGross', 
            'openingTheaters', 'IMDb_Rating', 'IMDb_numVotes', 
            'rt_audiencescore', 'rt_tomatometerscores']
    data = drop_na_data.copy()[columns]

    # convert object into number  $187,131,806
    data['Gross'] = data['Gross'].map(lambda x: int(x.replace('$', '').replace(',', '')))
    data['openingGross'] = data['openingGross'].map(lambda x: int(x.replace('$', '').replace(',', '')))
    data['Theaters'] = data['Theaters'].map(lambda x: int(x.replace(',', '')))
    data['openingTheaters'] = data['openingTheaters'].map(lambda x: int(x.replace(',', '')))
    data['rt_audiencescore'] = data['rt_audiencescore'].astype('int')
    data['rt_tomatometerscores'] = data['rt_tomatometerscores'].astype('int')

    data.to_csv(save, index=False)

    return data


if __name__ == '__main__':
    data = clean_data(save='data/processed/cleaned_data.csv')

    print(data)
    print(len(data))
