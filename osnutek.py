import re
import requests

url = "https://finance.yahoo.com/research-hub/screener/equity/"
HEADERS = {"User-Agent": "Mozilla/5.0"}


odgovor = requests.get(url, timeout=2, headers=HEADERS)

print(odgovor.status_code)

vsebina = odgovor.text

dat = open("glavna_stran_yahoo_finance", "w", encoding="utf-8")
dat.write(vsebina)
dat.close()
with open("glavna_stran_yahoo_finance", "r", encoding="utf-8") as dat1:
    vsebina = dat1.read()

primer_vzorca = '<span class="symbol yf-hzimq4">GOOGL </span>'

imena_tickerjev = []


def poisci_tickerje(vsebina):
    for najdba in re.finditer(
        r'<span class="symbol yf-hzimq4">(<ticker>GOOGL) </span>',
        vsebina,
        flags=re.DOTALL,
    ):
        imena_tickerjev.append("ticker")

    return imena_tickerjev
