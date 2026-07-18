import requests
import re
import csv

def izlusci_sp_500():
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

    vzorec = r"<tr[^>]*>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>\s*<td[^>]*>([^<]*)</td>\s*</tr>"

    validni_datumi = []
    seznam_cen = []

    odgovor = session.get(
        f"https://ca.finance.yahoo.com/quote/%5EGSPC/history/", timeout=10, headers=HEADERS
    )
    if odgovor.status_code == 200:
        vsebina = odgovor.text
        for najdba in re.findall(
            vzorec,
            vsebina,
            flags=re.DOTALL,
        ):
            validni_datumi.append(f"{najdba[0]}")

        for najdba in re.findall(vzorec, vsebina, flags=re.DOTALL):
            seznam_cen.append(najdba[5])

        with open("SP_500_cene", "w", newline="", encoding="utf-8") as dat:
            pisatelj = csv.writer(dat)

            glava = ["ticker"] + validni_datumi
            pisatelj.writerow(glava)
            vrstica = ["^GSPC"] + seznam_cen
            pisatelj.writerow(vrstica)
