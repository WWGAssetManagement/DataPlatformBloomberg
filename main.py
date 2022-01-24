import bloomberg
from tqdm import tqdm

if __name__ == "__main__":
    indx = bloomberg.get_indx_members(security="KOSPI Index")
    data = indx.to_dict()
    tickers = list(map(lambda x: x['member_ticker_and_exchange_code'] + ' EQUITY', data))
    for ticker in tqdm(tickers):
        price = bloomberg.get_px_close_1d(security=ticker, start="19800101", end="20220123")
        price.to_mysql()