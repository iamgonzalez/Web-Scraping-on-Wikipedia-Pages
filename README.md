# 📖 Overview

This Jupyter Notebook uses the python programming language to perform web scraping on Wikipedia pages, by collecting information present in the infobox of a given page. In the present code, the main table of Disney films on Wikipedia was used: “https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films”, in which the link to the page of each film on Wikipedia was extracted, and later each one these links are accessed by extracting the infobox and adding their information to the DataFrame. In another step, the critical notes are extracted for each movie in the DataFrame through the use of the OMDB (open movie database) api.

# 📦 Dependencies

- bs4
- datetime
- json
- pandas 
- pickle
- requests

# 💻 Usage

1.	Install the dependencies;
2.	Run Jupyter Notebook in terminal to see the code in your browser.
