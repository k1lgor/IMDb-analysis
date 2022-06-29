from __future__ import annotations

import csv
from time import sleep

import requests
from bs4 import BeautifulSoup


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


def write_movies(filename: str, movies: dict):
    with open(filename, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Movie title", "Year", "IMDb rating"])
        for title, year_rating in movies.items():
            for year, rating in year_rating.items():
                writer.writerow([title, year, rating])


if __name__ == "__main__":
    chart = {
        1: 'Top 250 Movies',
        2: 'Most Popular Movies',
        3: 'Top 250 TV Shows',
        4: 'Most Popular TV Shows'
    }
    scraping = True

    while scraping:
        print('Choose which chart do you want to web scrap?')
        print('[1] - Top 250 Movies\n[2] - Most Popular Movies\n[3] - Top 250 TV Shows\n[4] - Most Popular TV Shows')
        number = int(input("===> "))

        print(
            f'You have chosen {chart[number]} and data will be saved in .csv file')

        match number:
            case 1:
                write_movies("IMDb_Top_250_Movies.csv",
                             WebScraping("https://www.imdb.com/chart/top/?ref_=nv_mv_250").get_imdb())
            case 2:
                write_movies("IMDb_Most_Popular_Movies.csv",
                             WebScraping("https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm").get_imdb())
            case 3:
                write_movies("IMDb_Top_250_TV_Shows.csv",
                             WebScraping("https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250").get_imdb())
            case 4:
                write_movies("IMDb_Most_Popular_TV_Shows.csv",
                             WebScraping("https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv").get_imdb())

        sleep(1)
        more_scraping = input(
            'All done. Do you want to scrap another one? [y/n] ')
        scraping = False if more_scraping.lower() == 'n' else True
