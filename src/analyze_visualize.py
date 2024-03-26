import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_rating_distribution(data_):
    data = data_.copy()
    data['rt_audiencescore'] = data['rt_audiencescore'] / 10
    data['rt_tomatometerscores'] = data['rt_tomatometerscores'] / 10
    sns.histplot(x='IMDb_Rating', data=data, kde=True, element ='step', label='IMDb Rating')
    sns.histplot(x='rt_audiencescore', data=data, kde=True, element ='step', label='Rotten Tomatoes Audience Score')
    sns.histplot(x='rt_tomatometerscores', data=data, kde=True, element ='step', label='Rotten Tomatoes Tomatometer Score')

    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.legend()
    

def plot_gross_distribution(data_):
    data = data_.copy()
    sns.histplot(x='Gross', data=data, kde=True, element ='step', label='Gross')
    plt.xlabel('Gross')
    plt.ylabel('Count')
    plt.legend()
    

def plot_theaters_distribution(data_):
    data = data_.copy()
    sns.histplot(x='Theaters', data=data, kde=True, element ='step', label='Theaters')
    plt.xlabel('Theaters')
    plt.ylabel('Count')
    plt.legend()
    

def plot_avg_gross_distribution(data_):
    data = data_.copy()
    data['avg Gross'] = data['Gross'] / data['Theaters']
    sns.histplot(x='avg Gross', data=data, kde=True, element ='step', label='avg Gross')
    plt.xlabel('avg Gross')
    plt.ylabel('Count')
    plt.legend()


def plot_opening_gross_distribution(data_):
    data = data_.copy()
    sns.histplot(x='openingGross', data=data, kde=True, element ='step', label='Opening Gross')
    plt.xlabel('Opening Gross')
    plt.ylabel('Count')
    plt.legend()


def plot_avg_opening_gross_distribution(data_):
    data = data_.copy()
    data['avg openingGross'] = data['openingGross'] / data['openingTheaters']
    sns.histplot(x='avg openingGross', data=data, kde=True, element ='step', label='avg Opening Gross')
    plt.xlabel('avg Opening Gross')
    plt.ylabel('Count')
    plt.title('avg Opening Gross Distribution')
    plt.legend()


def plot_opening_theaters_distribution(data_):
    data = data_.copy()
    sns.histplot(x='openingTheaters', data=data, kde=True, element ='step', label='Opening Theaters')
    plt.xlabel('Opening Theaters')
    plt.ylabel('Count')
    plt.legend()


def plot_theaters_gross(data_):
    data = data_.copy()
    sns.regplot(x='Theaters', y='Gross', data=data)
    plt.title('Theaters & Gross')
    

def plot_rating_gross(data_):
    data = data_.copy()
    data['rt_audiencescore'] = data['rt_audiencescore'] / 10
    data['rt_tomatometerscores'] = data['rt_tomatometerscores'] / 10
    sns.regplot(x='IMDb_Rating', y='Gross', data=data, label='IMDb Rating')
    sns.regplot(x='rt_audiencescore', y='Gross', data=data, label='Rotten Tomatoes Audience Score')
    sns.regplot(x='rt_tomatometerscores', y='Gross', data=data, label='Rotten Tomatoes Tomatometer Score')

    plt.xlabel('Rating')
    plt.ylabel('Gross')
    plt.title('Rating & Gross')
    plt.legend()


def plot_rating_theaters(data_):
    data = data_.copy()
    data['rt_audiencescore'] = data['rt_audiencescore'] / 10
    data['rt_tomatometerscores'] = data['rt_tomatometerscores'] / 10
    sns.regplot(x='IMDb_Rating', y='Theaters', data=data, label='IMDb Rating')
    sns.regplot(x='rt_audiencescore', y='Theaters', data=data, label='Rotten Tomatoes Audience Score')
    sns.regplot(x='rt_tomatometerscores', y='Theaters', data=data, label='Rotten Tomatoes Tomatometer Score')

    plt.xlabel('Rating')
    plt.ylabel('Theaters')
    plt.title('Rating & Theaters')
    plt.legend()
    

def plot_rating_opening_gross(data_):
    data = data_.copy()
    data['rt_audiencescore'] = data['rt_audiencescore'] / 10
    data['rt_tomatometerscores'] = data['rt_tomatometerscores'] / 10
    sns.regplot(x='IMDb_Rating', y='openingGross', data=data, label='IMDb Rating')
    sns.regplot(x='rt_audiencescore', y='openingGross', data=data, label='Rotten Tomatoes Audience Score')
    sns.regplot(x='rt_tomatometerscores', y='openingGross', data=data, label='Rotten Tomatoes Tomatometer Score')

    plt.xlabel('Rating')
    plt.ylabel('Opening Gross')
    plt.title('Rating & Opening Gross')
    plt.legend()


def plot_rating_opening_theaters(data_):
    data = data_.copy()
    data['rt_audiencescore'] = data['rt_audiencescore'] / 10
    data['rt_tomatometerscores'] = data['rt_tomatometerscores'] / 10
    sns.regplot(x='IMDb_Rating', y='openingTheaters', data=data, label='IMDb Rating')
    sns.regplot(x='rt_audiencescore', y='openingTheaters', data=data, label='Rotten Tomatoes Audience Score')
    sns.regplot(x='rt_tomatometerscores', y='openingTheaters', data=data, label='Rotten Tomatoes Tomatometer Score')

    plt.xlabel('Rating')
    plt.ylabel('Opening Theaters')
    plt.title('Rating & Opening Theaters')
    plt.legend()
    

def plot_rating_avg_gross(data_):
    data = data_.copy()
    data['rt_audiencescore'] = data['rt_audiencescore'] / 10
    data['rt_tomatometerscores'] = data['rt_tomatometerscores'] / 10
    data['avg Gross'] = data['Gross'] / data['Theaters']
    sns.regplot(x='IMDb_Rating', y='avg Gross', data=data, label='IMDb Rating')
    sns.regplot(x='rt_audiencescore', y='avg Gross', data=data, label='Rotten Tomatoes Audience Score')
    sns.regplot(x='rt_tomatometerscores', y='avg Gross', data=data, label='Rotten Tomatoes Tomatometer Score')

    plt.xlabel('Rating')
    plt.ylabel('avg Gross')
    plt.title('Rating & avg Gross')
    plt.legend()
    

def plot_rating_avg_opening_gross(data_):
    data = data_.copy()
    data['rt_audiencescore'] = data['rt_audiencescore'] / 10
    data['rt_tomatometerscores'] = data['rt_tomatometerscores'] / 10
    data['avg Opening Gross'] = data['openingGross'] / data['openingTheaters']
    sns.regplot(x='IMDb_Rating', y='avg Opening Gross', data=data, label='IMDb Rating')
    sns.regplot(x='rt_audiencescore', y='avg Opening Gross', data=data, label='Rotten Tomatoes Audience Score')
    sns.regplot(x='rt_tomatometerscores', y='avg Opening Gross', data=data, label='Rotten Tomatoes Tomatometer Score')

    plt.xlabel('Rating')
    plt.ylabel('avg Opening Gross')
    plt.title('Rating & avg Opening Gross')
    plt.legend()
    

def corelation(data_):
    data = data_.copy()
    data['rt_audiencescore'] = data['rt_audiencescore'] / 10
    data['rt_tomatometerscores'] = data['rt_tomatometerscores'] / 10
    data['avg Opening Gross'] = data['openingGross'] / data['openingTheaters']
    data['avg Gross'] = data['Gross'] / data['Theaters']

    corr_matrix = data[data.columns[1:]].corr()
    # plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    
    plt.title('Correlation') 
    plt.tight_layout()
    
