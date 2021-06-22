import tornado.web
import tornado.escape
import uuid
import yfinance as yf
import tornado.web
import json
from utils import *


class RequestHandler(tornado.web.RequestHandler):

    def response(self,message):
        self.write(json.dumps(message))
    
    def error(self,message,status_code: int):
        self.set_status(status_code)
        self.write(json.dumps(message))
        self.finish()
        
    def finish(self,*args, **kwargs):
        self.set_header('Content-Type', 'application/json')
        return super(RequestHandler, self).finish(*args, **kwargs)

class CPRHandler(RequestHandler):

    async def get(self):
        try:
            stock=self.get_argument("stock", None, True)
        except tornado.web.MissingArgumentError as e:
            self.error("Stock name param doesnt exist",409)

        method=self.get_argument("method", "TRADITIONAL", True)

        data = yf.download(tickers=stock+'.NS', period='1d', interval='1d')
        try:
            PREVDAY = data.iloc[-1]
            HIGH = PREVDAY["High"]
            LOW = PREVDAY["Low"]
            OPEN = PREVDAY["Open"]
            CLOSE = PREVDAY["Close"]
            self.response({"Name":stock.upper(),
                            "Segment":"NSE",
                            "LastTradingDay":{"Date":PREVDAY._name.__str__().split(" ")[0],
                                                "Open":OPEN,
                                                "High":HIGH,
                                                "Low":LOW,
                                                "Close":CLOSE,},

                            "CPR":CPR(HIGH,LOW,OPEN,CLOSE,method.upper())})
        except IndexError as e:
            
            self.error("Stock with name {} doesnt exist in NSE segment".format(stock),409)