from bs4 import BeautifulSoup as bs
import requests
import json
import datetime
import pickle


def get_content_value(row_data):
    """ Selecting table text

    Args:
        row_data (str): html element parsing in BeautifulSoup with .find("td"))

    Returns:
        str: Text of each table row 
    """
    if row_data.find('li'):
        # Selecting html
        return[li.get_text(' ', strip=True).replace('\xa0', ' ') for li in row_data.find_all('li')]
    else:
        # Selecting text
        return row_data.get_text(' ', strip=True).replace('\xa0', ' ')

def clean_tags(soup):
    """ Deleting tags in html

    Args:
        soup (bs): html parsing in BeautifulSoup
    """
    for tag in soup.find_all(["sup", "span"]):
        tag.decompose()
        
def get_info_box(url):
    """ Selecting info box

    Args:
        url (str): url in str format

    Returns:
        dict: Dictionary containing a movie with their info box
    """
    # Using the requests library to access the website
    r = requests.get(url)
    # Using BeautifulSoup for parsing html from website
    soup = bs(r.content)
    # Selecting table
    info_box = soup.find(class_="infobox vevent")
    # Pick up the all lines of the box
    info_rows = info_box.find_all("tr")
    # Deleting tags
    clean_tags(soup)
    movie_info = {}
    for index, row in enumerate(info_rows):
        if index == 0:
            # Selecting the title of each line 
            movie_info['title'] = row.find("th").get_text(" ", strip=True)
        else:
            # Selecting data of each line 
            header = row.find('th')
            if header:
                content_key = row.find("th").get_text(" ", strip=True)
                content_value = get_content_value(row.find("td"))
                movie_info[content_key] = content_value
            
    return movie_info    

def save_data_json(title, data):
    """ Saved the DataFrame in json format

    Args:
        title (str): File name
        data (list): Movie data
    """
    with open(title,'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii = False, indent=2)

def load_data_json(path):
    """ Load the DataFrame in json format

    Args:
        path (str): File path

    Returns:
        json: File
    """
    with open(path,'r', encoding='utf-8') as file:
        return json.load(file)

def get_date(data):
    """ Create a get_date function, which uses a split on the list element, selecting month, day and year

    Args:
        data (list): List with date ex: [May 19, 1937]

    Returns:
        str: str with the date
    """
    
    try:
        for e in data:
            try:
                mes = e.split()[0].strip()
                dia = e.split()[1].replace(',', '').strip()
                ano = e.split()[2].strip()
                # Select month name and convert to number
                datetime_object = datetime.datetime.strptime(mes, "%B")
                month_number = datetime_object.month
                
                datetime_object = datetime.datetime.strptime(ano, "%Y")
                year_number = datetime_object.year
                
                datetime_object = datetime.datetime.strptime(dia, "%d")
                day_number = datetime_object.day
                # Returns a string in y-m-d format
                tudo = f'{year_number}/{month_number}/{day_number}'
                return tudo
            except:
                pass
    except:
        pass

def converter(data):
    """ Function to convert date to datetime

    Args:
        data (str): String with date 

    Returns:
        str: Date converted to datetime
    """
    try:
        date = datetime.strptime(data,'%Y/%m/%d')
        return date
    except:
        pass

def split_budget(value):
    """ Removing text and characters in budget column and select numerical value

    Args:
        value (str): String with numeric value

    Returns:
        str: Retuns the value
    """
    try:
        valor = value.split('$')[1]
        valor = valor.split(' ')[0]
        valor = valor.split('–')[0]
        valor = valor.replace(',','.')
        return valor
    except:
        pass

def split_value(value):
    """ Removing text and characters in Box office column and select numerical value

    Args:
        value (str): String with numeric value

    Returns:
        str: Returns the value
    """
    try:
        valor = value.split('$')[1]
        valor = valor.split(' ')[0]
        valor = valor.split('–')[0]
        valor = valor.replace(',','.')
        valor = valor.split('.')[0]
        
        return valor
    except:
        pass

def save_data_pickle(name, data):
    """ Saving the DataFrame in pickle format

    Args:
        name (str): File name
        data (DataFrame): Data frame you want to save
    """
    with open(name,'wb') as f:
        pickle.dump(data,f)

def load_data_pickle(name):
    """ Load the DataFrame in pickle format

    Args:
        name (str): File path

    Returns:
        DataFrame:  Returns the DataFrame
    """
    with open(name,'rb') as f:
        return pickle.load(f)

def catch_rating(filme, ano, avaliation):
    """ Captures the critic's rating for each movie

    Args:
        filme (str): Movie name
        ano (str): Film release year
        avaliation (str): Choose rating between Internet Movie Database', 'Rotten Tomatoes' or 'Metacritic'

    Returns:
        str: Review note
    """
    try:
        movie = filme.replace(' ', '+')
        key = 'YOUR_KEY'
        userid = 'YOUR_USERID'
        info =  requests.get(f'http://www.omdbapi.com/?i=tt{userid}&apikey={key}&t={movie}&y={ano}&plot=full').json()
        ratings = info.get('Ratings')
        for rating in ratings:
            if rating['Source'] == avaliation:
                nota = (rating['Value']).replace('%','')
                nota = nota.split('/')[0]
        return nota
    except:
        return 0