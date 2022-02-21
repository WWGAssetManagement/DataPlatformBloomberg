from doctest import BLANKLINE_MARKER
from fileinput import close
import bloomberg
from tqdm import tqdm
from config.settings import LOG


index_tickers = [
    "KOSPI INDEX",
    "SPX INDEX",
    "NDX INDEX",
    "RTY INDEX",
    "SX5E INDEX",
    "HSI INDEX",
    "NKY INDEX",
    "VNINDEX INDEX",
    "SHSZ300 INDEX",
    "SENSEX INDEX"
    ]

start_date = '20000101'
end_date = '20220220'

for ticker in tqdm(index_tickers):
    try:
        name = bloomberg.get_security_name(ticker)
        name.to_mysql()
        close_price = bloomberg.get_px_close_1d(ticker, start=start_date, end=end_date)
        close_price.to_mysql()
        per = bloomberg.get_pe_ratio(ticker, start=start_date, end=end_date)
        per.to_mysql()
        pbr = bloomberg.get_px_to_book_ratio(ticker, start=start_date, end=end_date)
        pbr.to_mysql()
    except Exception as e:
        LOG.logger.debug(f"{ticker}: {e}")


