import requests
import re
import json
import time
import csv

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

session = requests.Session()
session.headers.update(HEADERS)

with open("json_tickerjev", "r", encoding="utf-8") as dat:
    seznam_tickerjev = json.load(dat)

# regex za P/E je malo bolj zakompliciran, saj ne vsebuje značke </fin-streamer>
# del [^<]*<\/[^>]+> "poje" vse do < in potem ignorira čim več besedila, kolikor je možno do >

vzorec_market_cap = r"Market Cap.*?([^<>]+)</fin-streamer>"
vzorec_beta = r"PE Ratio \(TTM\).*?([^<>]+)</fin-streamer>"
vzorec_pe = r"PE Ratio \(TTM\)[^<]*<\/[^>]+>(?:\s*<[^>]+>)*\s*([^<>]+?)\s*<"

with open("tickerji_s_podatki.csv", "w", newline="", encoding="utf-8") as dat:
    pisatelj = csv.writer(dat)
    pisatelj.writerow(["ticker", "market_cap", "beta", "P/E"])

    for ticker in seznam_tickerjev:
        odgovor = session.get(
            f"https://ca.finance.yahoo.com/quote/{ticker}", timeout=10, headers=HEADERS
        )

        if odgovor.status_code == 200:
            vsebina = odgovor.text

            market_cap_najden = re.search(vzorec_market_cap, vsebina, re.DOTALL)
            beta_najden = re.search(vzorec_beta, vsebina, re.DOTALL)
            pe_najden = re.search(vzorec_pe, vsebina, re.DOTALL)

            if market_cap_najden == None or market_cap_najden.group(1).strip() == "--":
                market_cap = "N/A"
            else:
                market_cap = market_cap_najden.group(1).strip()

            if beta_najden == None or beta_najden.group(1).strip() == "--":
                beta = "N/A"
            else:
                beta = beta_najden.group(1).strip()

            if pe_najden == None or pe_najden.group(1).strip() == "--":
                pe = "N/A"
            else:
                pe = pe_najden.group(1).strip()

            pisatelj.writerow([ticker, market_cap, beta, pe])

        else:
            pisatelj.writerow([ticker, "N/A", "N/A", "N/A"])

        time.sleep(1)
