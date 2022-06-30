# Web Scraping file for IMDb charts as follows:

### - Top 250 Movies

### - Most Popular Movies

### - Top 250 TV Shows

### - Most Popular TV Shows

### - Lowest Rated Movies

### - Top Rated English Movies

### Info

```
The file takes the title, year and IMDb rating from the particular chart
and writes the information in '.csv' file in the current dir.

The script skips the Movies/TV shows which has NO rating in the charts.
```

### Setup

```
1. Initialize python virtual environment
    $ python -m venv venv
2. Activate virtual environment
    For Windows:
        $ .\venv\Scripts\activate
    For Linux:
        $ venv/bin/activate
3. Update pip manager
    For Windows:
        $ python -m pip install -- upgrade pip
    For Linux:
        $ pip install pip -U
4. Install pip requirements
    $ pip install -r requirements.txt
5. Usage
    $ python3 main.py
    or
    $ py main.py
```

### To do

```
- visualization of the charts with Jupyter Notebook
```