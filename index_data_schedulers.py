from doctest import BLANKLINE_MARKER
import bloomberg
from tqdm import tqdm
from config.settings import LOG
from datetime import datetime, timedelta

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


now = datetime.now()

start_date = (now - timedelta(days=5)).strftime('%Y%m%d')
end_date = now.strftime("%Y%m%d")
LOG.logger.debug(f"인덱스 데이터 수집 시작: {start_date}~{end_date}")

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


