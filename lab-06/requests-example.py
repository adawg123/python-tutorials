#!/usr/bin/python
import requests

    
def count_yelp(text):
    all_words = text.split()
    yelp_count = all_words.count('Yelp')
    return yelp_count

def replace_yelp(text):
    return text.replace('Yelp','google')

    r = requests.get('http://wwww.yelp.com')
    if r.status_code == 200:
    print count_yelp(r.text)



# Assignment 

# Load the yelp page and replace all occurance of yelp to google
# Load the file from http://censusdata.ire.org/36/all_050_in_36.P2.csv and find
# the max P002001

