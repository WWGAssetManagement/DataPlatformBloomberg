import bloomberg
from tqdm import tqdm
from bloomberg import blp
from bloomberg.blp.GICS_INDUSTRY import GICS_INDUSTRY
from config.settings import ENGINE, LOG
from multiprocessing import Pool
from config.settings import SESSION
from bloomberg.model.models import DelistModel
import pandas as pd 

def start(ticker):
    try:
        close = bloomberg.get_px_close_1d(security=ticker, start="20000101", end="20220313")
        open = bloomberg.get_px_open(security=ticker, start="20000101", end="20220313")
        high = bloomberg.get_px_high(security=ticker, start="20000101", end="20220313")
        low = bloomberg.get_px_low(security=ticker, start="20000101", end="20220313")
        volume = bloomberg.get_px_volume(security=ticker, start="20000101", end="20220313")
        last = bloomberg.get_px_last(sercurity=ticker, start="20000101", end="20220313")
        
        close.to_mysql()
        open.to_mysql()
        high.to_mysql()
        low.to_mysql()
        volume.to_mysql()
        last.to_mysql()
    except Exception as e:
        LOG.logger.debug(f"{ticker}: {e}")

def start_px_last(ticker):
    try:
        last = bloomberg.get_px_last(sercurity=ticker,  start="20000101", end="20220411")
        last.to_mysql()
    except Exception as e:
        LOG.logger.debug(f"{ticker}: {e}")


def start_ern(ticker):
    try:
        ern = bloomberg.get_ern_ann_dt_and_per(ticker)
        ern.to_mysql()
    except Exception as e:
        LOG.logger.debug(f"{ticker}: {e}")

def start_gics_name(ticker):
    try:
        gics_name = bloomberg.get_gics_sector_name(ticker)
        gics_name.to_mysql()
    except Exception as e:
        LOG.logger.debug(f"{ticker}: {e}")

def start_gics_industry(ticker):
    try:
        gics_indst = bloomberg.get_gics_industry_name(ticker)
        gics_indst.to_mysql()
    except Exception as e:
        LOG.logger.debug(f"{ticker}: {e}")

def start_gics_sector(ticker):
    try:
        gics_sector = bloomberg.get_gics_sector(ticker)
        gics_sector.to_mysql()
    except Exception as e:
        LOG.logger.debug(f"{ticker}: {e}")

def start_gics_industry(ticker):
    try:
        gics_industry = bloomberg.get_gics_industry(ticker)
        gics_industry.to_mysql()
    except Exception as e:
        LOG.logger.debug(f"{ticker}: {e}")

def start_id_cusip(ticker):
    try:
        cusip = bloomberg.get_id_cusip(ticker)
        cusip.to_mysql()
    except Exception as e:
        LOG.logger.debug(f"{ticker}: {e}")

def start_net_oper_profit_after_tax(ticker):
    try:
        operatin_profit = bloomberg.get_net_oper_profit_after_tax(ticker, start="20220126", end="2022-02-10")
        operatin_profit.to_mysql()
    except Exception as e:
        LOG.logger.debug(f"{ticker}: {e}")

def start_pe_ratio(ticker):
    try:
        per = bloomberg.get_pe_ratio(ticker, start="19000101", end="20220313")
        per.to_mysql()
    except Exception as e:
        LOG.logger.debug(f"{ticker}: {e}")

def start_px_to_book_ratio(ticker):
    try:
        pbr = bloomberg.get_px_to_book_ratio(ticker, start="19000101", end="20220313")
        pbr.to_mysql()
    except Exception as e:
        LOG.logger.debug(f"{ticker}: {e}")

if __name__ == "__main__":
    # session = SESSION()
    # results = session.query(DelistModel.Security_ID).all()
    # indx = bloomberg.get_indx_members(security="SPX Index")
    # indx.to_mysql()
    # indx = bloomberg.get_indx_members(security="KOSDAQ Index")
    # indx.to_mysql()
    # data = indx.to_dict()
    # index_tickers = list(map(lambda x: x['member_ticker_and_exchange_code'] + ' EQUITY', data))
    # tickers = list(map(lambda x: x[0], results))
    # tickers = tickers + index_tickers
    # print(index_tickers)
    # sql = """SELECT ticker FROM tb_etf"""
    # conn = ENGINE.connect()
    # ticker_df = pd.read_sql(sql, conn)['ticker']
    # tickers = list(map(lambda x: x+' EQUITY', ticker_df))
    index_tickers = ['KBPMABIN Index']

    pool = Pool(processes=2)
    # pool.map(start_net_oper_profit_after_tax, tqdm(index_tickers))
    pool.map(start_px_last, tqdm(index_tickers))
    # pool.map(start, tqdm(index_tickers))    
    # pool.map(start_ern, tqdm(index_tickers))
    # pool.map(start_pe_ratio, tqdm(index_tickers))
    # pool.map(start_px_to_book_ratio, tqdm(index_tickers))
    # pool.map(start_gics_name, tqdm(tickers))
    # pool.map(start_gics_industry, tqdm(tickers))
    # pool.map(start_gics_sector, tqdm(tickers ))
    # pool.map(start_gics_industry, tqdm(tickers))
    # pool.map(start_id_cusip, tqdm(tickers))
    pool.close()
    pool.join() 

