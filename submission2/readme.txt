1. What does scraper.py do.
    This script is used to scrape movie data from https://www.boxofficemojo.com/year/2023/.
    There are 200 movies in this page.
    The script scrapes all 200 movies overal data from this page. 
    Also, the script scrapes opening data from information page of each movie.
    Then it stores these data in a Pandas DataFrame.

2. How does scraper.py work.
    a. Use pandas.read_html() to get all movies shown on https://www.boxofficemojo.com/year/2023/.
    b. Extract and format useful data, including urls of movie information page.
    c. Use request and bs4 to extract opening revenue and theaters from movie information page.
        In this step, it is too slow to request one by one which cost 130 seconds.
        So, I use thread pool to make it faster which cost 6 seconds only.
    d. Combine overal data and opening data together to get the final csv.

3. How to use scraper.py.
    a. python scraper.py
        It will scrape the complete data and show it.
    b. python scraper.py --scrape N
        It will scrape N records and show it.
    c. python scraper.py --save <path>
        It will save the data in <path> as csv, without showing it.
    d. python scraper.py --scrape N --save <path>
        It will scrape N records and save the data in <path> as csv, without showing it.
