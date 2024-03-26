import pandas as pd

def integrate(save='data/processed/merged_data.csv'):
    # Integrate datasets in data/raw/ and save result in {save} 
    # Default saved in data/processed/merged_data.csv
    # Make sure all raw data have been scraped and saved in data/raw/**.csv
    movies_2023_boxoffice = pd.read_csv('data/raw/movies_2023_boxoffice.csv')
    IMDb_Ratings = pd.read_csv('data/raw/IMDb_Ratings.csv')
    RT_Ratings = pd.read_csv('data/raw/RT_Ratings.csv')

    stage_1 = pd.merge(movies_2023_boxoffice, IMDb_Ratings, on='uid', how='left')
    result = pd.merge(stage_1, RT_Ratings, on='Release', how='left')

    result.to_csv(save, index=False)

    return result


if __name__ == '__main__':
    merged_data = integrate(save='data/processed/merged_data.csv')
    print(merged_data)
    print(len(merged_data))

