import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup
import argparse

def format_movies_2023_boxoffice(data):
    # Extract what we want from raw data 

    data['Info_url'] = data['Release'].map(lambda value: value[1])
    data['Release'] = data['Release'].map(lambda value: value[0])
    data['Gross'] = data['Gross'].map(lambda value: value[0])
    data['Theaters'] = data['Theaters'].map(lambda value: value[0])
    data['Release Date'] = data['Release Date'].map(lambda value: value[0])

    return data

def get_movie_info_boxoffice_ThreadPool(data):
    # Use thread pool to accelerate the process of getting data using request and bs4.
    # Cost 5.9 seconds for 200 records

    urls = data['Info_url'].values
    site = 'https://www.boxofficemojo.com'
    urls = [(site+url, url) for url in urls]
    uids = []
    openingGross = []
    openingTheaters = []
    urls_ = []

    def get_request(url):
        response = requests.get(url[0])

        # get uid
        soup = BeautifulSoup(response.content, "html.parser")
        uid_href = soup.find("div", {"id": "title-summary-refiner"}).find("a")['href']
        uid = uid_href.split('/')[2]

        # get opening gross and theaters
        opening_span = soup.find('span', string='Opening')
        if opening_span:
            opening_div = opening_span.find_parent('div')
            texts = [text for text in opening_div.stripped_strings]
            
            openingGross = texts[1]
            if len(texts) > 2:
                openingTheater = texts[2].split('\n')[0]
            else:
                openingTheater = 'unknown'

        else:
            openingGross = 'unknown'
            openingTheater = 'unknown'

        return uid, openingGross, openingTheater, url[1]
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        future_to_url = (executor.submit(get_request, url) for url in urls)
        for future in as_completed(future_to_url):
            
            try:
                uid, openingGross_, openingTheater, url = future.result()
            except Exception as exc:
                uid = 'request error'
                openingGross_ = 'request error'
                openingTheater = 'request error'
                url = 'request error'
            finally:
                uids.append(uid)
                openingGross.append(openingGross_)
                openingTheaters.append(openingTheater)
                urls_.append(url)

    data = pd.DataFrame({
        'Info_url': urls_,
        'uid': uids,
        'openingGross': openingGross,
        'openingTheaters': openingTheaters
    })


    return data


def get_movie_info_boxoffice(data):
    # Get data using request and bs4. Cost 150 seconds for 200 records

    urls = data['Info_url'].values
    site = 'https://www.boxofficemojo.com'
    uids = []
    openingGross = []
    openingTheaters = []
    for url in urls:
        url = site + url
        response = requests.get(url)

        # get uid
        soup = BeautifulSoup(response.content, "html.parser")
        uid_href = soup.find("div", {"id": "title-summary-refiner"}).find("a")['href']
        uid = uid_href.split('/')[2]
        uids.append(uid)

        # get opening gross and theaters
        opening_span = soup.find('span', string='Opening')
        if opening_span:
            opening_div = opening_span.find_parent('div')
            texts = [text for text in opening_div.stripped_strings]
            openingGross.append(texts[1])
            if len(texts) > 2:
                openingTheaters.append(texts[2].split('\n')[0])
            else:
                openingTheaters.append('unknown')

        else:
            openingGross.append('unknown')
            openingTheaters.append('unknown')

    return uids, openingGross, openingTheaters



def get_movies_2023_boxoffice(n=None):
    # Get movies in 2023

    columns = ['Release', 'Gross', 'Theaters', 'Release Date']
    if n:
        data = pd.read_html('https://www.boxofficemojo.com/year/2023/', extract_links='body')[0].head(n)
    else:
        data = pd.read_html('https://www.boxofficemojo.com/year/2023/', extract_links='body')[0]

    data = data[columns]

    data = format_movies_2023_boxoffice(data)

    info_data = get_movie_info_boxoffice_ThreadPool(data)
    result = pd.merge(data, info_data, on='Info_url', how='inner')

    return result


def main(scrape=None, save=None):
    data = get_movies_2023_boxoffice(scrape)
    if save:
        data.to_csv(save, index=False)
        print(f'Data saved in {save}')
    else:
        print(data)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Scraper")

    parser.add_argument("--save", type=str, required=False, help="Path to save the dataset")
    parser.add_argument("--scrape", type=int, required=False, help="Numbers of data to scrape")

    args = parser.parse_args()
    main(args.scrape, args.save)

    



