import requests
from bs4 import BeautifulSoup

def fetch_nanjo_topics():
    url = "https://www.city.nanjo.okinawa.jp/topics/"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
    response = requests.get(url, headers=headers, timeout=10)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "lxml")
    articles = []
    links = soup.find_all("a", href=lambda h: h and "/topics/" in h and h != "/topics/")
    for link in links:
        title = link.get_text(strip=True)
        href = link.get("href", "")
        url_full = href if href.startswith("http") else "https://www.city.nanjo.okinawa.jp" + href
        if title:
            articles.append({"title": title, "url": url_full})
    return articles
