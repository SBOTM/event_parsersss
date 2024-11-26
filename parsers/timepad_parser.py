import requests
from typing import List, Dict
from .base_parser import BaseParser

class TimepadParser(BaseParser):
    API_URL = "https://api.timepad.ru/v1/events"

    def fetch_events(self) -> List[Dict]:
        events = []
        try:
            response = requests.get(self.API_URL, params={"limit": 10})
            response.raise_for_status()
            data = response.json()

            for event in data.get('values', []):
                events.append({
                    "title": event.get('name', ''),
                    "date": event.get('starts_at', ''),
                    "location": event.get('location', {}).get('name', 'Unknown'),
                    "description": event.get('description_short', ''),
                    "category": event.get('category', {}).get('name', 'Unknown'),
                    "price": event.get('tickets', {}).get('min_price', 'Unknown'),
                    "url": event.get('url', '')
                })

        except requests.RequestException as e:
            print(f"Error fetching data from Timepad: {e}")

        return events