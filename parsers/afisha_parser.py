import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from .base_parser import BaseParser

class AfishaParser(BaseParser):
    BASE_URL = "https://www.afisha.ru"

    def fetch_events(self) -> List[Dict]:
        events = []
        try:
            response = requests.get(f"{self.BASE_URL}/msk/")
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Пример извлечения данных
            for event_card in soup.select('.some-event-selector'):  # Указать реальный селектор
                title = event_card.select_one('.event-title').text.strip()
                date = event_card.select_one('.event-date').text.strip()
                location = event_card.select_one('.event-location').text.strip()
                url = self.BASE_URL + event_card.select_one('a')['href']

                events.append({
                    "title": title,
                    "date": date,
                    "location": location,
                    "description": "",
                    "category": "Unknown",  # Категорию можно уточнять
                    "price": "Unknown",    # Уточнить, если возможно
                    "url": url
                })

        except requests.RequestException as e:
            print(f"Error fetching data from Afisha.ru: {e}")

        return events