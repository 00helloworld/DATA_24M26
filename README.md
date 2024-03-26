# Install Requirements  
Directly required:
```
pandas
numpy
matplotlib
seaborn
requests
BeautifulSoup
re
random
concurrent
```
```
pip install -r requirements.txt
```
# How to Run
## Get Data
**Note**: `title.ratings.tsv` can be downloaded from https://datasets.imdbws.com/  
**Note**: To scrape data from Rotten Tomatoes, `user_agent in src/utils.py` should be updated, or it would be blocked by Rotten Tomatoes.
```
step1. Download IMDb data from https://datasets.imdbws.com/
step2. Update `user_agent in src/utils.py` if necessary
step3. python src/get_raw_data.py
```
Raw data will be saved in `data/raw/`.

## Integrate Data Sources
**Note**: Previous steps shoud be done.
```
python src/integrate_data.py
```
Mearged data will be saved in `data/processed/merged_data.csv`

## Clean Data
**Note**: Previous steps shoud be done.
```
python src/integrate_data.py
```
Cleaned data will be saved in `data/processed/cleaned_data.csv`

## Analysis and Visualization
All analysis and visualization can be found in `results/analyze_visualize.ipynb`.
Source code can be found in `src/analyze_visualize.py`