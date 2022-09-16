import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient(
    'mongodb://test:sparta@ac-qs2cnvy-shard-00-00.u33zjtg.mongodb.net:27017,ac-qs2cnvy-shard-00-01.u33zjtg.mongodb.net:27017,ac-qs2cnvy-shard-00-02.u33zjtg.mongodb.net:27017/Cluster0?ssl=true&replicaSet=atlas-4g7ly1-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.dbsparta

url = 'https://playboard.co/chart/video/most-viewed-all-videos-in-worldwide-weekly'
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    videos = soup.select('#app > div.root > main > div > div.container.container--mfit > table > tbody > tr')

    for video in videos:
        a = video.select_one('td.title > a > h3')
        if a is not None:
            rank = video.select_one('td.rank.rank.rank--ko > div.current').text
            title = a.text
            thumbnail = video.select_one('td.thumbnail > a > div > div')["data-background-image"]
            score = video.select_one('td.score > span').text
            channel = video.select_one('td.channel > a > span').text
        doc = {
            'rank': rank,
            'title' : title,
            'thumbnail' : thumbnail,
            'score' : score,
            'channel' : channel
        }
        db.worldviewsWEEKLY.insert_one(doc)

else :
    print(response.status_code)