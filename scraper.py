import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

# Builds yelp search url from given location:
# locValue can be either city, state e.g. San Fransisco, CA
# or zipcode 94016
def build_url_from_location(locValue=None):
    if locValue == None:
        locValue = input("Please enter the name of the place (city, State) or its zip code you want to search restaurants in (e.g. \"Bellevue, WA\" or 98004): ")

    locValue = urllib.parse.quote_plus(locValue)
    baseurl = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc='
    url = baseurl + locValue
    return url

# Sends GET request with given url and parses the html response using BeautifulSoup
# returns the BeautifulSoup instance
def read_soup_HTML(url):
    r = urllib.request.urlopen(url)
    html = r.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# Builds the restaurant names (only the first page) in a list from the given BeautifulSoup html
def build_restaurant_names(soup):
    restaurant_names = []
    for a in soup.select('h3 a'):
        name = a.get_text()
        restaurant_names.append(name)
    return restaurant_names


# Usage example:
#
# url = build_url_from_location('San Fransisco, CA')
# soup = read_soup_HTML(url)
# names = build_restaurant_names(soup)
# print(names, len(names))
