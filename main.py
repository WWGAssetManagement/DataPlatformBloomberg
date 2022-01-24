import bloomberg
from tqdm import tqdm
from bloomberg import blp
from config.settings import LOG
from multiprocessing import Pool

def start(ticker):
    try:
        close = bloomberg.get_px_close_1d(security=ticker, start="19800101", end="20220123")
        close.to_mysql()
        open = bloomberg.get_px_open(security=ticker, start="19800101", end="20220123")
        high = bloomberg.get_px_high(security=ticker, start="19800101", end="20220123")
        low = bloomberg.get_px_low(security=ticker, start="19800101", end="20220123")
        volume = bloomberg.get_px_volume(security=ticker, start="19800101", end="20220123")

        open.to_mysql()
        high.to_mysql()
        low.to_mysql()
        volume.to_mysql()

    except Exception as e:
        LOG.logger.debug(f"{ticker}: {e}")

if __name__ == "__main__":
    indx = bloomberg.get_indx_members(security="KOSPI Index")
    data = indx.to_dict()
    tickers = list(map(lambda x: x['member_ticker_and_exchange_code'] + ' EQUITY', data))
    pool = Pool(processes=4)
    pool.map(start, tqdm(tickers))
    pool.close()
    pool.join()