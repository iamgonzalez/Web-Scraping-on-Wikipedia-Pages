# 📖 Overview

This Jupyter Notebook uses the python programming language to perform web scraping on Wikipedia pages, by collecting information present in the infobox of a given page. In the present code, the main table of Disney films on Wikipedia was used: “https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films”, in which the link to the page of each film on Wikipedia was extracted, and later each one these links are accessed by extracting the infobox and adding their information to the DataFrame. In another step, the critical notes are extracted for each movie in the DataFrame through the use of the OMDB (open movie database) API.

# 📄 Files

- **main.ipynb**: Main Jupyter Notebook used to perform web scraping;
- **get_imdb_note.ipynb**: Jupyter Notebook used to get imdb note;
- **help_functions.py**: Python Script that contains help functions used by main.ipynb and get_imdb_note.ipynb.

# 📦 Dependencies

- bs4
- datetime
- json
- pandas 
- pickle
- requests

# 💻 Usage

1. To use this project it is necessary to have a OMDb API account, the registration can be done for free [here](http://www.omdbapi.com/apikey.aspx "here");
2. Obtain the authentication keys for connecting to the OMDb API account;
3. Store the authentication keys in the Python Script help_functions.py;
4.	Install the dependencies;
5.	Run Jupyter Notebook in terminal to see the code in your browser.
