from pycoingecko import CoinGeckoAPI
import datetime
from statistics import median, mean
cg = CoinGeckoAPI()

def main():
    numdays = 7
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]
    fn_format = lambda x: x.strftime("%d-%m-%Y")
    fn_gecko = lambda date: cg.get_coin_history_by_id(id='edgeware', vs_currencies='usd', date=date)
    fn_usd_price = lambda x: x['market_data']['current_price']['usd']
    fn_eur_price = lambda x: x['market_data']['current_price']['eur']

    usd_prices =  sorted(map(fn_usd_price, map(fn_gecko, map(fn_format, date_list))))
    eur_prices =  sorted(map(fn_eur_price, map(fn_gecko, map(fn_format, date_list))))
    usd_mean_price =  mean(usd_prices)
    eur_mean_price =  mean(eur_prices)
    prices = (usd_mean_price,eur_mean_price)

    print('The following is the average price in USD of Edgeware over the past seven days calculated by mathematical mean, rounded to the 4th decimal:')
    print('')
    print('$', round(usd_mean_price, 4), 'per EDG')
    print('€',round(eur_mean_price, 4), 'per EDG')
    print('')
    print('This function also returns the set of both prices respectively:')
    print(prices)
    print('')
    print('Authorship: The data is provided by Coingecko, and this script is originally by developer Matej Nemçek, updated by Thom Ivy, and is open-source.')
    print('Original 30-day version: https://repl.it/talk/share/calculate-edgeware-price-for-30d/118764')
    
    
    return prices


if __name__ == "__main__":
    main()
