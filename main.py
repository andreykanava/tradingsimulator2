import requests
from colorama import Fore

balusd = 100
loanbal = 0
baleth = 0
balbtc = 0
baldot = 0
balbnb = 0
balxrp = 0
balluna = 0
balsol = 0
baltrx = 0
startbal = float(balusd)


while True:
    def get_price(symbol, prices):
        for price in prices:
            if symbol == price['symbol']:
                return price['price']






    prices = requests.get('https://api.binance.com/api/v3/ticker/price').json()
    curethprice = get_price('ETHUSDT', prices)
    curbtcprice = get_price('BTCUSDT', prices)
    curdotprice = get_price('DOTUSDT', prices)
    curbnbprice = get_price('BNBUSDT', prices)
    curxrpprice = get_price('XRPUSDT', prices)
    curlunaprice = get_price('LUNAUSDT', prices)
    cursolprice = get_price('SOLUSDT', prices)
    curtrxprice = get_price('TRXUSDT', prices)

    curethpriceview = get_price('ETHUSDT', prices)
    curbtcpriceview = get_price('BTCUSDT', prices)
    curdotpriceview = get_price('DOTUSDT', prices)
    curbnbpriceview = get_price('BNBUSDT', prices)
    curxrppriceview = get_price('XRPUSDT', prices)
    curlunapriceview = get_price('LUNAUSDT', prices)
    cursolpriceview = get_price('SOLUSDT', prices)
    curtrxpriceview = get_price('TRXUSDT', prices)

    balusd = float(balusd)
    balusd = round(balusd, 3)
    loanbal = float(loanbal)
    baleth = float(baleth)
    baleth = round(baleth, 3)
    balbnb = float(balbnb)
    balbnb = round(balbnb, 3)
    baldot = float(baldot)
    balbnb = round(balbnb, 3)
    balbtc = float(balbtc)
    balbtc = round(balbtc, 3)
    balxrp = float(balxrp)
    balxrp = round(balxrp, 3)
    balluna = float(balluna)
    balluna = round(balluna, 3)
    balsol = float(balsol)
    balsol = round(balsol, 3)
    baltrx = float(baltrx)
    baltrx = round(baltrx, 3)

    balusdview = format(float(balusd), 'f')
    balethview = format(float(baleth), 'f')
    balbnbview = format(float(balbnb), 'f')
    baldotview = format(float(baldot), 'f')
    balbtcview = format(float(balbtc), 'f')
    balxrpview = format(float(balxrp), 'f')
    ballunaview = format(float(balluna), 'f')
    balsolview = format(float(balsol), 'f')
    baltrxview = format(float(baltrx), 'f')

    curethprice = float(curethprice)
    curethbuyprice = 1 / curethprice
    ethusd = baleth * curethprice
    ethusd = round(ethusd, 3)

    curtrxprice = float(curtrxprice)
    curtrxbuyprice = 1 / curtrxprice
    trxusd = baltrx * curtrxprice
    trxusd = round(trxusd, 3)

    cursolprice =float(cursolprice)
    cursolbuyprice = 1 / cursolprice
    solusd = balsol * cursolprice
    solusd = round(solusd, 3)

    curlunaprice = float(curlunaprice)
    curlunabuyprice = 1 / curlunaprice
    lunausd = balluna * curlunaprice
    lunausd = round(lunausd, 3)

    curxrpprice = float(curxrpprice)
    curxrpbuyprice = 1 / curxrpprice
    xrpusd = balxrp * curxrpprice
    xrpusd = round(xrpusd, 3)

    curbtcprice = float(curbtcprice)
    curbtcbuyprice = 1 / curbtcprice
    btcusd = balbtc * curbtcprice
    btcusd = round(btcusd, 3)

    curdotprice = float(curdotprice)
    curdotbuyprice = 1 / curdotprice
    dotusd = baldot * curdotprice
    dotusd = round(dotusd, 3)

    curbnbprice = float(curbnbprice)
    curbnbbuyprice = 1 / curbnbprice
    bnbusd = balbnb * curbnbprice
    bnbusd = round(bnbusd, 3)

    allact = ethusd + btcusd + dotusd + bnbusd + solusd + xrpusd + trxusd + balusd + balluna

    if loanbal > allact:
        print('Warning! Your debt is more than your all actives!')

    mbalusd = allact - loanbal
    profit = mbalusd / startbal * 100 - 100
    profit = round(profit, 2)

    print(Fore.LIGHTWHITE_EX + '---------------------------')
    print('Your profit:', profit, '%')
    print(Fore.LIGHTYELLOW_EX + 'usd bal:', balusd)
    print(Fore.LIGHTRED_EX + 'loan bal:', loanbal)
    print(Fore.LIGHTWHITE_EX + '---------------------------')
    print(Fore.GREEN + 'bal eth: ', baleth, '≈', ethusd, '$')
    print(Fore.LIGHTWHITE_EX + '---------------------------')
    print(Fore.YELLOW + 'bal btc:', balbtc, '≈', btcusd, '$')
    print(Fore.LIGHTWHITE_EX + '---------------------------')
    print(Fore.BLUE + 'bal dot', baldot, '≈', dotusd, '$')
    print(Fore.LIGHTWHITE_EX + '---------------------------')
    print(Fore.CYAN + 'bal bnb', balbnb, '≈', bnbusd, '$')
    print(Fore.LIGHTWHITE_EX + '---------------------------')
    print(Fore.MAGENTA + 'bal xrp', balxrp, '≈', xrpusd, '$')
    print(Fore.LIGHTWHITE_EX + '---------------------------')
    print(Fore.LIGHTYELLOW_EX + 'bal luna', balluna, '≈', lunausd, '$')
    print(Fore.LIGHTWHITE_EX + '---------------------------')
    print(Fore.GREEN + 'bal sol', balsol, '≈', solusd, '$')
    print(Fore.LIGHTWHITE_EX + '---------------------------')
    print(Fore.RED + 'bal trx', baltrx, '≈', trxusd, '$')
    print(Fore.LIGHTWHITE_EX + '---------------------------')
    print(Fore.WHITE + 'all actives:', allact, '$')
    print(Fore.LIGHTWHITE_EX + '***********************************')
    print(Fore.GREEN + 'current eth price:', curethpriceview)
    print(Fore.YELLOW + 'current btc price:', curbtcpriceview)
    print(Fore.BLUE + 'current dot price:', curdotpriceview)
    print(Fore.CYAN + 'current bnb price:', curbnbpriceview)
    print(Fore.MAGENTA + 'current xrp price:', curxrppriceview)
    print(Fore.LIGHTYELLOW_EX + 'current luna price:', curlunapriceview)
    print(Fore.LIGHTCYAN_EX + 'current sol price:', cursolpriceview)
    print(Fore.RED + 'current trx price', curtrxpriceview)
    print(Fore.LIGHTWHITE_EX + '***********************************')


    print(Fore.GREEN +  '1-eth,', Fore.YELLOW +  '2-btc,', Fore.BLUE + '3-dot,', Fore.CYAN + '4-bnb,', Fore.MAGENTA + '5-xrp,')
    print(Fore.LIGHTYELLOW_EX + '6-luna,', Fore.LIGHTCYAN_EX + '7-sol,', Fore.RED + '8-trx,', Fore.LIGHTBLUE_EX + '9-credit', Fore.RESET)

    chcur = input(': ')

    if chcur == '9':
        print(Fore.LIGHTMAGENTA_EX + '1-take loan, 2-repay the loan')
        f = input(': ')
        if f == '1':
            print('amount (max. 10k)')
            r = input(': ')
            r = float(r)
            if r <= 10000:
                loanbal = loanbal + r
                balusd = balusd + r
                print('loanbal:', loanbal, 'usdbal:', balusd)
        if f == '2':
            print('amount (your debt:', loanbal, ')')
            if loanbal != 0:
                r = input(': ')
                r = float(r)
                if r <= balusd and r <= loanbal:
                    balusd = balusd - r
                    loanbal = loanbal - r
                    print('loanbal:', loanbal, 'usdbal:', balusd)

    if chcur == '8':
        print(Fore.RED + '1-sell,', Fore.GREEN +  '2-buy : ')
        ch = input(': ')
        if ch == '1':
            if baltrx != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                sellamount = input(': ')
                if sellamount == 'all':
                    sellamount = baltrx
                sellamount = float(sellamount)
                if balsol >= sellamount:
                    balusd = balusd + sellamount * curtrxprice
                    baltrx = baltrx - sellamount
                    print(balusd)
                else:
                    print(Fore.RED + 'not enough trx on bal')
            else:
                print(Fore.RED + 'no trx on bal')

        if ch == '2':
            if balusd != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                buyamount = input(': ')
                if buyamount == 'all':
                    buyamount = balusd
                buyamount = float(buyamount)
                if buyamount <= balusd:
                    baltrx = baltrx + buyamount * curtrxbuyprice
                    balusd = balusd - buyamount
                    print(baltrx)
                else:
                    print(Fore.RED + 'not enough usd on bal')
            else:
                print(Fore.RED + 'no usd on bal')

    if chcur == '7':
        print(Fore.RED + '1-sell,', Fore.GREEN +  '2-buy : ')
        ch = input(': ')
        if ch == '1':
            if balsol != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                sellamount = input(': ')
                if sellamount == 'all':
                    sellamount = balsol
                sellamount = float(sellamount)
                if balsol >= sellamount:
                    balusd = balusd + sellamount * cursolprice
                    balsol = balsol - sellamount
                    print(balusd)
                else:
                    print(Fore.Red + 'not enough sol on bal')
            else:
                print(Fore.RED + 'no sol on bal')

        if ch == '2':
            if balusd != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                buyamount = input(': ')
                if buyamount == 'all':
                    buyamount = balusd
                buyamount = float(buyamount)
                if buyamount <= balusd:
                    balsol = balsol + buyamount * cursolbuyprice
                    balusd = balusd - buyamount
                    print(balsol)
                else:
                    print(Fore.RED + 'not enough usd on bal')
            else:
                print(Fore.RED + 'no usd on bal')

    if chcur == '6':
        print(Fore.RED + '1-sell,', Fore.GREEN +  '2-buy : ')
        ch = input(': ')
        if ch == '1':
            if balluna != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                sellamount = input(': ')
                if sellamount == 'all':
                    sellamount = balluna
                sellamount = float(sellamount)
                if balluna >= sellamount:
                    balusd = balusd + sellamount * curlunaprice
                    balluna = balluna - sellamount
                    print(balusd)
                else:
                    print(Fore.Red + 'not enough luna on bal')
            else:
                print(Fore.RED + 'no luna on bal')

        if ch == '2':
            if balusd != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                buyamount = input(': ')
                if buyamount == 'all':
                    buyamount = balusd
                buyamount = float(buyamount)
                if buyamount <= balusd:
                    balluna = balluna + buyamount * curlunabuyprice
                    balusd = balusd - buyamount
                    print(balluna)
                else:
                    print(Fore.RED + 'not enough usd on bal')
            else:
                print(Fore.RED + 'no usd on bal')

    if chcur == '5':
        print(Fore.RED + '1-sell,', Fore.GREEN +  '2-buy : ')
        ch = input(': ')
        if ch == '1':
            if balxrp != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                sellamount = input(': ')
                if sellamount == 'all':
                    sellamount = balxrp
                sellamount = float(sellamount)
                if balxrp >= sellamount:
                    balusd = balusd + sellamount * curxrpprice
                    balxrp = balxrp - sellamount
                    print(balusd)
                else:
                    print(Fore.Red + 'not enough xrp on bal')
            else:
                print(Fore.RED + 'no xrp on bal')

        if ch == '2':
            if balusd != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                buyamount = input(': ')
                if buyamount == 'all':
                    buyamount = balusd
                buyamount = float(buyamount)
                if buyamount <= balusd:
                    balxrp = balxrp + buyamount * curxrpbuyprice
                    balusd = balusd - buyamount
                    print(balxrp)
                else:
                    print(Fore.RED + 'not enough usd on bal')
            else:
                print(Fore.RED + 'no usd on bal')

    if chcur == '4':
        print(Fore.RED + '1-sell,', Fore.GREEN +  '2-buy : ')
        ch = input(': ')
        if ch == '1':
            if balbnb != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                sellamount = input(': ')
                if sellamount == 'all':
                    sellamount = balbnb
                sellamount = float(sellamount)
                if balbnb >= sellamount:
                    balusd = balusd + sellamount * curbnbprice
                    balbnb = balbnb - sellamount
                    print(balusd)
                else:
                    print(Fore.Red + 'not enough bnb on bal')
            else:
                print(Fore.RED + 'no bnb on bal')

        if ch == '2':
            if balusd != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                buyamount = input(': ')
                if buyamount == 'all':
                    buyamount = balusd
                buyamount = float(buyamount)
                if buyamount <= balusd:
                    balbnb = balbnb + buyamount * curbnbbuyprice
                    balusd = balusd - buyamount
                    print(balbnb)
                else:
                    print(Fore.RED + 'not enough usd on bal')
            else:
                print(Fore.RED + 'no usd on bal')

    if chcur == '3':
        print(Fore.LIGHTRED_EX + '1-sell,', Fore.LIGHTGREEN_EX + '2-buy : ')
        ch = input(': ')
        if ch == '1':
            if baldot != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                sellamount = input(': ')
                if sellamount == 'all':
                    sellamount = baldot
                sellamount = float(sellamount)
                if sellamount <= baldot:
                    balusd = balusd + sellamount * curdotprice
                    baldot = baldot - sellamount
                    print(balusd)
                else:
                    print(Fore.RED + 'not enough dot on bal')
            else:
                print(Fore.Red + 'no dot on bal')

        if ch == '2':
            if balusd != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                buyamount = input(': ')
                if buyamount == 'all':
                    buyamount = balusd
                buyamount = float(buyamount)
                if buyamount <= balusd:
                    baldot = baldot + buyamount * curdotbuyprice
                    balusd = balusd - buyamount
                else:
                    print(Fore.Red + 'not enough usd on bal')
                print(baldot)
            else:
                print(Fore.Red + 'no usd on bal')

    if chcur == '2':
        print(Fore.LIGHTRED_EX + '1-sell,', Fore.LIGHTGREEN_EX + '2-buy : ')
        ch = input(': ')
        if ch == '1':
            if balbtc != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                sellamount = input(': ')
                if sellamount == 'all':
                    sellamount = balbtc
                sellamount = float(sellamount)
                if sellamount <= balbtc:
                    balusd = balusd + sellamount * curbtcprice
                    balbtc = balbtc - sellamount
                    print(balusd)
                else:
                    print(Fore.RED + 'not enough btc on bal')
            else:
                print(Fore.RED + 'no btc on bal')

        if ch == '2':
            if balusd != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                buyamount = input(': ')
                if buyamount == 'all':
                    buyamount = balusd
                buyamount = float(buyamount)
                if buyamount <= balusd:
                    balbtc = balbtc + buyamount * curbtcbuyprice
                    balusd = balusd - buyamount
                    print(balbtc)
                else:
                    print(Fore.RED + 'not enough usd on bal')
            else:
                print(Fore.RED + 'no usd on bal')

    if chcur == '1':
        print(Fore.LIGHTRED_EX + '1-sell,', Fore.LIGHTGREEN_EX + '2-buy : ')
        ch = input(': ')
        if ch == '1':
            if baleth != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                sellamount = input(': ')
                if sellamount == 'all':
                    sellamount = baleth
                sellamount = float(sellamount)
                if sellamount <= baleth:
                    balusd = balusd + sellamount * curethprice
                    baleth = baleth - sellamount
                    print(balusd)
                else:
                    print(Fore.RED + 'not enough eth on bal')
            else:
                print(Fore.RED + 'no eth on bal')

        if ch == '2':
            if balusd != 0:
                print(Fore.LIGHTWHITE_EX + 'amount or all:')
                buyamount = input(': ')
                if buyamount == 'all':
                    buyamount = balusd
                buyamount = float(buyamount)
                if buyamount <= balusd:
                    baleth = baleth + buyamount * curethbuyprice
                    balusd = balusd - buyamount
                    print(baleth)
                else:
                    print(Fore.RED + 'not enough usd on bal')
            else:
                print(Fore.RED + 'no usd on bal')
    print('''





















        ''')