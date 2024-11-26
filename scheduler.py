import schedule
import time
from parsers.afisha_parser import AfishaParser
from parsers.timepad_parser import TimepadParser

def run_parsers():
    afisha_parser = AfishaParser()
    timepad_parser = TimepadParser()

    events = []
    events.extend(afisha_parser.fetch_events())
    events.extend(timepad_parser.fetch_events())

    # Сохраняем результаты в JSON
    with open("events.json", "w", encoding="utf-8") as f:
        import json
        json.dump({"events": events}, f, ensure_ascii=False, indent=4)

    print("Events fetched and saved successfully!")

# Планирование задачи
schedule.every().day.at("03:00").do(run_parsers)

#if __name__ == "__main__":
#    while True:
#        schedule.run_pending()
#        time.sleep(1)