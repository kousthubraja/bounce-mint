import numpy as np
import trendln
import yfinance as yf
from nsetools import Nse
from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

if __name__ == '__main__':
    nse = Nse()
    codes = nse.get_stock_codes().keys()
    # codes = ['ACC', 'AUBANK', 'AARTIIND', 'ABBOTINDIA', 'ADANIENT', 'ADANIGAS', 'ADANIGREEN', 'ADANIPORTS', 'ADANITRANS',            'ABCAPITAL', 'ABFRL', 'AJANTPHARM', 'APLLTD', 'ALKEM', 'AMARAJABAT', 'AMBUJACEM', 'APOLLOHOSP',  'APOLLOTYRE', 'ASHOKLEY', 'ASIANPAINT', 'AUROPHARMA', 'DMART', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE',            'BAJAJFINSV', 'BAJAJHLDNG', 'BALKRISIND', 'BANDHANBNK', 'BANKBARODA', 'BANKINDIA', 'BATAINDIA',            'BERGEPAINT', 'BEL', 'BHARATFORG', 'BHEL', 'BPCL', 'BHARTIARTL', 'BIOCON', 'BBTC', 'BOSCHLTD', 'BRITANNIA',            'CESC', 'CADILAHC', 'CANBK', 'CASTROLIND', 'CHOLAFIN', 'CIPLA', 'CUB', 'COALINDIA', 'COFORGE', 'COLPAL',            'CONCOR', 'COROMANDEL', 'CROMPTON', 'CUMMINSIND', 'DLF', 'DABUR', 'DALBHARAT', 'DHANI', 'DIVISLAB',            'LALPATHLAB', 'DRREDDY', 'EDELWEISS', 'EICHERMOT', 'EMAMILTD', 'ENDURANCE', 'ESCORTS', 'EXIDEIND',            'FEDERALBNK', 'FORTIS', 'FRETAIL', 'GAIL', 'GMRINFRA', 'GICRE', 'GLENMARK', 'GODREJAGRO', 'GODREJCP',            'GODREJIND', 'GODREJPROP', 'GRASIM', 'GUJGASLTD', 'GSPL', 'HCLTECH', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE',            'HAVELLS', 'HEROMOTOCO', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR', 'HINDZINC', 'HUDCO', 'HDFC', 'ICICIBANK',            'ICICIGI', 'ICICIPRULI', 'ISEC', 'IDFCFIRSTB', 'ITC', 'IBULHSGFIN', 'INDHOTEL', 'IOC', 'IRCTC', 'IGL',            'INDUSTOWER', 'INDUSINDBK', 'NAUKRI', 'INFY', 'INDIGO', 'IPCALAB', 'JSWENERGY', 'JSWSTEEL', 'JINDALSTEL',            'JUBLFOOD', 'KOTAKBANK', 'L&TFH', 'LTTS', 'LICHSGFIN', 'LTI', 'LT', 'LUPIN', 'MRF', 'MGL', 'M&MFIN', 'M&M',            'MANAPPURAM', 'MARICO', 'MARUTI', 'MFSL', 'MINDTREE', 'MOTHERSUMI', 'MPHASIS', 'MUTHOOTFIN', 'NATCOPHARM',            'NMDC', 'NTPC', 'NATIONALUM', 'NAVINFLUOR', 'NESTLEIND', 'OBEROIRLTY', 'ONGC', 'OIL', 'OFSS', 'PIIND',            'PAGEIND', 'PETRONET', 'PFIZER', 'PIDILITIND', 'PEL', 'POLYCAB', 'PFC', 'POWERGRID', 'PRESTIGE', 'PGHH',            'PNB', 'RBLBANK', 'RECLTD', 'RAJESHEXPO', 'RELIANCE', 'SBICARD', 'SBILIFE', 'SRF', 'SANOFI', 'SHREECEM',            'SRTRANSFIN', 'SIEMENS', 'SBIN', 'SAIL', 'SUNPHARMA', 'SUNTV', 'SYNGENE', 'TVSMOTOR', 'TATACHEM', 'TCS',            'TATACONSUM', 'TATAMOTORS', 'TATAPOWER', 'TATASTEEL', 'TECHM', 'RAMCOCEM', 'TITAN', 'TORNTPHARM',            'TORNTPOWER', 'TRENT', 'UPL', 'ULTRACEMCO', 'UNIONBANK', 'UBL', 'VGUARD', 'VBL', 'IDEA', 'VOLTAS',            'WHIRLPOOL', 'WIPRO', 'YESBANK', 'ZEEL']
    found = []
    for i in codes:
        try:
            scrip = nse.get_quote(i)
            tick = yf.Ticker(i + '.NS')
            hist = tick.history(period='1y', rounding=False)
            fig = trendln.plot_support_resistance(hist[-1000:].Low, None)
            ax = fig.gca()
            labels = list(map(lambda l: l._label, ax.lines))
            index = labels.index('Resistance')
            index0 = labels.index('Support')
            for j in range(index0, index):
                line = ax.lines[j]
                x = line.get_xdata().tolist()
                y = line.get_ydata().tolist()

                model = LinearRegression()
                model.fit(np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1))
                # print(tick.info['regularMarketPrice'])
                X_predict = np.array([251])  # put the dates of which you want to predict kwh here
                y_predict = model.predict(X_predict.reshape(-1, 1))
                print(i, ":", y_predict[0][0], scrip['lastPrice'])
                if abs(scrip['lastPrice'] - y_predict[0][0]) <= 0.02 * scrip['lastPrice']:
                    found.append(i)
                    # c = plt.plot(x, y)
                    # plt.show()
                    break
        except:
            print("error")
            pass
    print(found)

