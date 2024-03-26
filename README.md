# Install Requirements  
```
pip install -r requirements.txt
```
# How to Run
### Get Data
Note: `title.ratings.tsv` can be downloaded from https://datasets.imdbws.com/  
Note: To scrape data from Rotten Tomatoes, `user_agent in src/utils.py` should be updated, or it would be blocked by Rotten Tomatoes.
```
step1. Download IMDb data from https://datasets.imdbws.com/
step2. Update `user_agent in src/utils.py` if necessary
step2. python src/get_raw_data.py
```
Raw data will be saved in `data/raw`.