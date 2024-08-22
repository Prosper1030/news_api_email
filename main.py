import requests
from send_email import send_email

topic = "tesla"

api_key ="2abfd9f0bfdc4a428029254b35b19434"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=2abfd9f0bfdc4a428029254b35b19434&"\
      "language=en"

request = requests.get(url)
content = request.json()

# print(content)
subject = "Today's news"
body = ""

for article in content["articles"][:20]:
    title = article.get("title", "No Title")
    description = article.get("description", "No Description")
    url = article.get("url", "No URL")
    if title and description:  # 確保都不是 None 或空字符串
        body += f"{title}\n{description}\n{url}\n\n"

send_email(subject=subject, message=body)
