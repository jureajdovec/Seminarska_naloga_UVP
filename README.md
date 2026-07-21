# Analiza delnic

V tej nalogi sem analiziral 500 največjih delnic na borzi in indeks S&P 500. <br>
<br>

### Podatke sem pridobil iz strani Yahoo finance:

1. Najprej sem pridobil tickerje 500 največjih delnic na trgu.

2. Iz strani za vsako delnico sem izluščil adjusted close price delnice za vsak dan v obdobju od 1. julija 2025 do 1. julija 2026.

3. Za vsako delnico sem izluščil tudi market cap, P/E razmerje in beta marker.

4. Izluščil sem tudi adjusted close price za indeks S&P 500 za vsak dan v obdobju od 1. julija 2025 do 1. julija 2026.
   <br>

### Podatke sem analiziral in naredil naslednje:

- Izvedel sem Fourierove transformacije in poiskal najmočnejše signale gibanja cen indeksa S&P 500.

- Na indeksu S&P 500 sem izvedel tudi Fourierovo ekstrapolacijo in ustvaril napoved za ceno tega indeksa v naslednjih 100 dnevih na podlagi preteklih podatkov.

- S pomočjo podatkov o 500 največjih delnicah sem ustvail sintetični indeks, ki posnema indeks S&P 500 ter ju primerjal med seboj.

- Poiskal sem delnice, ki najbolje aproksimirajo gibanje celotnega trga z beta markerji.

- Analiziral sem kumulativni delež največjih n podjetij, ko spreminjamo n.

- Poiskal in analiziral sem delnice z najvišjimi in najnižjimi P/E razmerji.

- Na podlagi razmerja med tveganjem in donosom sem ugotovil, katere od izbranih 500 delnic so najboljše za vlagatelje.
