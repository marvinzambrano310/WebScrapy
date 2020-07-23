import requests
from bs4 import BeautifulSoup
# Import MongoClient from pymongo so we can connect to the database
from pymongo import MongoClient


if __name__ == '__main__':
    # Instantiate a client to our MongoDB instance
    db_client = MongoClient('mongodb+srv://Marzam23:marzam23@dataanalysis.m9jnd.mongodb.net/test')
    prueba = db_client.prueba
    my_posts = prueba.posts


    response = requests.get("https://www.elsevier.com/es-es/connect")
    soup = BeautifulSoup(response.content, "lxml")

    post_titles = soup.find_all("a", class_="tile-image-anchor")

    extracted = []
    for post_title in post_titles:
        extracted.append({
            'title' : post_title['title'],
            'link'  : post_title['href']
        })

    # Iterate over each post. If the link does not exist in the database, it's new! Add it.
    for post in extracted:
        if db_client.prueba.my_posts.find_one({'link': post['link']}) is None:
            # Let's print it out to verify that we added the new post
            print("Found a new listing at the following url: ", post['link'])
            db_client.prueba.my_posts.insert(post)