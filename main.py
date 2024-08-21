import requests

api_key ="2abfd9f0bfdc4a428029254b35b19434"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07-21&sortBy=publishedAt&apiKey=2abfd9f0bfdc4a428029254b35b19434"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])