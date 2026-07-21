import re
import requests
import json


def pridobi_tickerje():
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    imena_tickerjev = []

    for i in range(5):
        odgovor = requests.get(
            f"https://finance.yahoo.com/research-hub/screener/equity/?start={i * 100}&count=100",
            timeout=2,
            headers=HEADERS,
        )
        vsebina = odgovor.text

        # V seznam imena_tickerjev doda vse tickerje, ki ustrezajo regularnem izrazu (validni simboli za delnice so le velike tiskane črke in pa znaki +-. =/)

        for najdba in re.findall(
            r'<span class="symbol yf-hzimq4">(?P<ticker>[A-Z+-. =/]*?) </span>',
            vsebina,
            flags=re.DOTALL,
        ):
            if najdba not in imena_tickerjev:
                imena_tickerjev.append(f"{najdba}")

    with open("json_tickerjev", "w", encoding="utf-8") as dat:
        json.dump(imena_tickerjev, dat)
