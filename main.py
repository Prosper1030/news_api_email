import requests
from send_email import send_email
api_key ="2abfd9f0bfdc4a428029254b35b19434"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07-21&sortBy=publishedAt&apiKey=2abfd9f0bfdc4a428029254b35b19434"

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"]:
    title = article["title"] if article["title"] is not None else ""
    description = article["description"] if article["description"] is not None else ""
    body = body + title + "\n" + description + 2 * "\n"

send_email(body)