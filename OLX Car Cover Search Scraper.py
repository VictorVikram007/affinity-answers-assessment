import requests
from bs4 import BeautifulSoup
import csv

def scrape_olx_car_cover():
    url = "https://www.olx.in/items/q-car-cover"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to load page")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('li')

    with open("olx_car_covers.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link"])

        for item in items:
            anchor = item.find("a")
            if anchor and anchor.text.strip():
                title = anchor.text.strip()
                link = "https://www.olx.in" + anchor["href"]
                writer.writerow([title, link])

    print("Scraped results saved to olx_car_covers.csv")

if __name__ == "__main__":
    scrape_olx_car_cover()
