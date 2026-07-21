from pridobi_tickerje import pridobi_tickerje
from izlusci_cene_ob_zaprtju import izlusci_cene_zaprtje
from izlusci_podatke_SP_500 import izlusci_sp_500
from izlusci_market_cap_Beta_in_P_E import izlusci_mcap_beta_pe


def vsi_podatki_delnice():
    pridobi_tickerje()
    izlusci_cene_zaprtje()
    izlusci_sp_500()
    izlusci_mcap_beta_pe()


if __name__ == "__main__":
    vsi_podatki_delnice()
