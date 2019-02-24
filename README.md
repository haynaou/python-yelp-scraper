# python-yelp-scraper
Yelp scraper that gets restaurants names by city/zipcode written in Python

### Example 
```python
url = build_url_from_location('San Fransisco, CA')
soup = read_soup_HTML(url)
names = build_restaurant_names(soup)
print(names)
```
The code above ☝️prints the following result:
```
[
  'The Soiled Dove',
  'Fog Harbor Fish House',
  'The House',
  'Marufuku Ramen SF',
  'Farmhouse Kitchen Thai Cuisine',
  'Tacorea',
  'Tropisueño',
  'Mersea',
  'Loló',
  'Scoma’s Restaurant',
  'The Codmother Fish and Chips',
  'Zero Zero',
  'Hog Island Oyster Co',
  'Izakaya KOU',
  'Hogwash',
  'Mensho Tokyo',
  'Brenda’s French Soul Food',
  'Hops & Hominy',
  'Anomaly',
  'Skool',
  'Marlowe',
  'Sotto Mare Oysteria & Seafood',
  'San Tung',
  'Myriad Gastropub',
  'Burma Superstar',
  'PPQ Dungeness Island',
  'Barbacco',
  'HRD',
  'Palm House',
  'Thanh Long',
  'Box Kitchen'
]
```

## Demo link
You can test it with your favourite city in the following link: https://repl.it/@HoudaAynaou/yelp-scraper
