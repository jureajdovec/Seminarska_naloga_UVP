import json
import requests
import re

HEADERS = {"User-Agent": "Mozilla/5.0"}

with open('json_tickerjev', 'r', encoding='utf-8') as dat:
    seznam_tickerjev = json.load(dat)

slovar_ticker_plus_cena_ob_zaprtju = {}

vzorec = r'<tr class="svelte-1swpzu1">.*?<td class="sym svelte-1swpzu1">.*?</td>.*?<td class="tr svelte-1swpzu1">([\d.]+)</td>.*?<td class="tr svelte-1swpzu1">([\d.]+)</td>.*?<td class="svelte-1swpzu1">([\d.]+)</td>.*?<td class="svelte-1swpzu1">([\d.]+)</td>.*?<td class="svelte-1swpzu1">([\d.]+)</td>.*?</tr>'

#primer_vrstice: <tr class="svelte-1swpzu1"><!----><!----><!----><!----><!----><!----><td class="sym svelte-1swpzu1">Jun 23, 2026</td><!----><!----><!----><!----><!----><!----><td class="tr svelte-1swpzu1">202.17</td><!----><!----><!----><!----><!----><!----><td class="tr svelte-1swpzu1">203.77</td><!----><!----><!----><!----><!----><!----><td class="svelte-1swpzu1">200.00</td><!----><!----><!----><!----><!----><!----><td class="svelte-1swpzu1">200.04</td><!----><!----><!----><!----><!----><!----><td class="svelte-1swpzu1">200.04</td><!----><!----><!----><!----><!----><!----><td class="svelte-1swpzu1"><span class="rr">-4.13%</span><!----></td><!----><!----><!----><!----><!----><!----><td class="svelte-1swpzu1">153,496,196</td></tr>

for t in seznam_tickerjev:
    ticker = t.strip().lower()
    seznam_cen = []
    #tickerji iz json datoteke so shranjeni z velikimi tiskanimi črkami, v url-jih pa so uporabljeni z malimi
    odgovor = requests.get(f"https://stockanalysis.com/stocks/{ticker}/history",timeout = 2,headers=HEADERS)
    vsebina = odgovor.text

    for najdba in re.findall(vzorec, 
    vsebina,
    flags=re.DOTALL,
    ): 
        seznam_cen.append(f'{najdba[4]}')
    slovar_ticker_plus_cena_ob_zaprtju[t] = seznam_cen


#import json
#import requests
#import re
#
#HEADERS = {"User-Agent": "Mozilla/5.0"}
#
#vzorec = r'<tr class="svelte-1swpzu1">.*?<td class="sym svelte-1swpzu1">.*?</td>.*?<td class="tr svelte-1swpzu1">([\d.]+)</td>.*?<td class="tr svelte-1swpzu1">([\d.]+)</td>.*?<td class="svelte-1swpzu1">([\d.]+)</td>.*?<td class="svelte-1swpzu1">([\d.]+)</td>.*?<td class="svelte-1swpzu1">([\d.]+)</td>.*?</tr>'
#
#odgovor = requests.get(f"https://stockanalysis.com/stocks/nvda/history",timeout = 2,headers=HEADERS)
#vsebina = odgovor.text
#for najdba in re.findall(vzorec, 
#vsebina,
#flags=re.DOTALL,
#): 
#    print(f'{najdba[4]}')