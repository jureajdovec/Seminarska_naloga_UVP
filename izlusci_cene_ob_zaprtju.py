import requests
import re
import json
import time
import csv

def izlusci_cene_zaprtje():

    # Ti headersi so bili skopirani iz interneta - yfinance je zelo strog, zato kratki headersi niso zadostovali

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "sl-SI,sl;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "sec-ch-ua": '"Google Chrome";v="144", "Not=A?Brand";v="8", "Chromium";v="144"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
    }

    # Na internetu nekateri za daljše requeste priporočajo ustvarjanje seesiona
    session = requests.Session()
    session.headers.update(HEADERS)

    with open("json_tickerjev", "r", encoding="utf-8") as dat:
        seznam_tickerjev = json.load(dat)

    slovar_ticker_plus_cena_ob_zaprtju = {}

    vzorec = r"<tr[^>]*>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>\s*</tr>"

    validni_datumi = []

    # Python tukaj pošiljam na kanadsko stran yahoo finance, saj ta nima piškotkov in ne zablokira
    # Datume, ko je bila borza odprta poberem iz strani za delnico Nvidia
    odgovor = session.get(
        f"https://ca.finance.yahoo.com/quote/NVDA/history", timeout=10, headers=HEADERS
    )
    if odgovor.status_code == 200:
        vsebina = odgovor.text
        for najdba in re.findall(
            vzorec,
            vsebina,
            flags=re.DOTALL,
        ):
            validni_datumi.append(f"{najdba[0]}")
    else:
        print("nekaj je šlo narobe")

    for ticker in seznam_tickerjev:
        seznam_cen = []

        # Zaradi pogostih sesutev (timeoutov) sem tukaj vključil try/except
        try:
            odgovor = session.get(
                f"https://ca.finance.yahoo.com/quote/{ticker}/history",
                timeout=10,
                headers=HEADERS,
            )

            if odgovor.status_code == 200:
                vsebina = odgovor.text
                for najdba in re.findall(vzorec, vsebina, flags=re.DOTALL):
                    seznam_cen.append(najdba[5])
                slovar_ticker_plus_cena_ob_zaprtju[ticker] = seznam_cen
            else:
                slovar_ticker_plus_cena_ob_zaprtju[ticker] = []

        except requests.exceptions.Timeout:
            slovar_ticker_plus_cena_ob_zaprtju[ticker] = []

        time.sleep(2)

    with open("tickerji_plus_cene.csv", "w", newline="", encoding="utf-8") as dat:
        pisatelj = csv.writer(dat)
        glava = ["ticker"] + validni_datumi
        pisatelj.writerow(glava)

        for ticker in seznam_tickerjev:
            cene = slovar_ticker_plus_cena_ob_zaprtju[ticker]
            vrstica = [ticker] + cene
            pisatelj.writerow(vrstica)
