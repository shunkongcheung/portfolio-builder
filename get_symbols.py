import json
import requests

def get_symbols():
    # # get total
    # data = json.dumps({
    #     "instrumentType":"EQUITY",
    #     "pageNumber":1,
    #     "sortColumn":"NORMALIZED_TICKER",
    #     "sortOrder":"ASC",
    #     "maxResultsPerPage":1,
    #     "filterToken":""
    # })
    # headers = {
    #     'Content-Type': 'application/json',
    # }
    # response = requests.post('https://www.nyse.com/api/quotes/filter', headers=headers, data=data)
    # res_data = response.json()
    # total = res_data[0]['total']

    # # get all data
    # data = json.dumps({
    #     "instrumentType":"EQUITY",
    #     "pageNumber":1,
    #     "sortColumn":"NORMALIZED_TICKER",
    #     "sortOrder":"ASC",
    #     "maxResultsPerPage":total,
    #     "filterToken":""
    # })
    # headers = {
    #     'Content-Type': 'application/json',
    # }
    # response = requests.post('https://www.nyse.com/api/quotes/filter', headers=headers, data=data)
    # res_data = response.json()

    # return [ itm ['symbolTicker'] for itm in res_data]

    # getting it from https://www.advfn.com/nasdaq/nasdaq.asp

    return ['AAL', 'AAPL', 'ACIU', 'ACST', 'ADTX', 'ADXS', 'AEZS', 'AGTC', 'AIKI', 'AMD', 'APHA', 'ASRT', 'ATOS', 'AYRO', 'AZN', 'BIOL', 'BMBL', 'BNGO', 'BOXL', 'BRQS', 'CAN', 'CGC', 'CIDM', 'CKPT', 'CLBS', 'CLOV', 'CLSN', 'COMS', 'CRBP', 'CRNT', 'CRON', 'CSCO', 'CSCW', 'CTRM', 'DKNG', 'DOYU', 'EBON', 'FCEL', 'FUTU', 'GEVO', 'GHSI', 'GLUU', 'GNUS', 'HUGE', 'IDEX', 'IFMK', 'INFI', 'INPX', 'INTC', 'IRDM', 'ITRM', 'JAGX', 'KHC', 'KXIN', 'LAZR', 'LI', 'LKCO', 'MARA', 'MSFT', 'MU', 'MVIS', 'NAKD', 'NNDM', 'NOVN', 'NVCN', 'NXTD', 'OCGN', 'OGI', 'ONTX', 'OPEN', 'PHUN', 'PLUG', 'PTE', 'PULM', 'PYPL', 'QTT', 'RCMT', 'RIOT', 'RKDA', 'SHIP', 'SIRI', 'SNDL', 'SOLO', 'SRNE', 'STAF', 'TELL', 'TLRY', 'TNXP', 'TRCH', 'TSLA', 'TXMD', 'TYME', 'VISL', 'VXRT', 'VYNE', 'XSPA', 'Z', 'ZNGA', 'ZSAN', 'ZYNE', 'CTAS', 'MAR', 'MRNA', 'PDD', 'ROST', 'ZM']
    # return ['AAL', 'AAPL', 'ACIU', ]

