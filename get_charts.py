from __future__ import annotations

import os
from os import path
from time import sleep

import requests
from bs4 import BeautifulSoup

import csv
from charts import chart


class WebScraping:
    def __init__(self, url):
        self.url = url

    def get_imdb(self) -> dict[str, int, float]:
        soup = BeautifulSoup(requests.get(self.url).text, "html.parser")
        titles = soup.find_all("td", class_="titleColumn")
        ratings = soup.find_all("td", class_="ratingColumn imdbRating")

        return {
            title.contents[1].text: {
                int(title.contents[3].text[1:5]): float(rating.contents[1].text)
            }
            for title, rating in zip(titles, ratings)
            if len(rating.contents) > 1
        }


def save_data(filename: str, movies: dict):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Movie title", "Year", "IMDb rating"])
        for title, year_rating in movies.items():
            for year, rating in year_rating.items():
                writer.writerow([title, year, rating])


def run():
    if not path.isdir('csv'):
        os.mkdir('csv')
    os.chdir('csv')

    scraping = True

    while scraping:
        print('Choose which chart do you want to web scrap?')
        print(
            '[1] - Top 250 Movies\n'
            '[2] - Most Popular Movies\n'
            '[3] - Top 250 TV Shows\n'
            '[4] - Most Popular TV Shows\n'
            '[5] - Lowest Rated Movies\n'
            '[6] - Top Rated English Movies\n')
        number = int(input("===> "))

        print(
            f'You have chosen {chart[number]} and data will be saved in .csv file')

        match number:
            case 1:
                save_data(
                    "IMDb_Top_250_Movies.csv",
                    WebScraping(
                        "https://www.imdb.com/chart/top/?ref_=nv_mv_250").get_imdb()
                )
            case 2:
                save_data(
                    "IMDb_Most_Popular_Movies.csv",
                    WebScraping(
                        "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm").get_imdb()
                )
            case 3:
                save_data(
                    "IMDb_Top_250_TV_Shows.csv",
                    WebScraping(
                        "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250").get_imdb()
                )
            case 4:
                save_data(
                    "IMDb_Most_Popular_TV_Shows.csv",
                    WebScraping(
                        "https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv").get_imdb()
                )
            case 5:
                save_data(
                    "IMDb_Lowest_Rated_Movies.csv",
                    WebScraping(
                        "https://www.imdb.com/chart/bottom?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35"
                        "-bb05-8646a1195842&pf_rd_r=Y1CT9PTRXSYCWQ0JWKWS&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i"
                        "=top&ref_=chttp_ql_8").get_imdb()
                )
            case 6:
                save_data(
                    "IMDb_Top_Rated_English_Movies.csv",
                    WebScraping("https://www.imdb.com/chart/top-english-movies?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p"
                                "=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=0APT2MECQACXEH9AG2TB&pf_rd_s"
                                "=right-4&pf_rd_t=15506&pf_rd_i=bottom&ref_=chtbtm_ql_4").get_imdb()
                )
        sleep(1)
        more_scraping = input(
            'All done. Do you want to scrap another one? [y/n] ')
        scraping = False if more_scraping.lower() == 'n' else True
