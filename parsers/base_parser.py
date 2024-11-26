from abc import ABC, abstractmethod
from typing import List, Dict

class BaseParser(ABC):
    @abstractmethod
    def fetch_events(self) -> List[Dict]:
        """Метод для извлечения данных о мероприятиях."""
        pass