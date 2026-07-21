# Analiza delnic

V tej nalogi sem analiziral 500 največjih delnic na borzi in indeks S&P 500.

### Pridobivanje podatkov (Yahoo Finance)
1. **Tickerji:** Pridobil sem seznam 500 največjih delnic na trgu.
2. **Cene delnic:** Za vsako delnico sem izluščil prilagojeno ceno ob zaprtju (*Adjusted Close Price*) za vsak dan v obdobju od **1. julija 2025 do 1. julija 2026**.
3. **Finančni kazalniki:** Za vsako podjetje sem pridobil tržno kapitalizacijo (*Market Cap*), **P/E razmerje** in **beta marker**.
4. **Indeks S&P 500:** Pridobil sem dnevne prilagojene cene ob zaprtju tudi za indeks S&P 500 za enako časovno obdobje.

### Analiza podatkov
- **Fourierova transformacija (FFT):** Izvedel sem analizo frekvenc in poiskal najmočnejše signale v gibanju cen indeksa S&P 500.
- **Fourierova ekstrapolacija:** Na podlagi preteklih ciklov sem ustvaril model za napoved cene indeksa S&P 500 za naslednjih 100 dni.
- **Sintetični indeks:** S pomočjo podatkov o 500 delnicah sem ustvaril sintetični indeks, ki posnema S&P 500, ter ju med seboj primerjal.
- **Aproksimacija trga:** S pomočjo beta markerjev sem poiskal delnice, ki najbolje posnemajo gibanje celotnega trga.
- **Tržna koncentracija:** Analiziral sem kumulativni delež največjih $N$ podjetij ob spreminjanju parametra $N$.
- **Vrednotenje (P/E):** Analiziral sem delnice z najvišjimi in najnižjimi P/E razmerji ter razložil razloge za odstopanja.
- **Tveganje vs. Donos:** Na podlagi razmerja med tveganjem in donosom sem identificiral najbolj optimalne delnice za vlagatelje.


### Kako zagnati projekt?

- potreboval boš naložen python verzije 3.0 ali več.

- naložene moraš imeti knjižnice pandas, matplotlib, numpy in scipy.

- celoten projekt lahko zaženeš z enim samim ukazom: python main.py

- v datoteki analiza_delnic.ipynb lahko pogledaš kakšne grafe izpiše napisana koda in poskusiš spremeniti določene vrednosti, da dobiš različne rezultate.