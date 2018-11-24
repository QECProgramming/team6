def pageRead(url):
    import requests
    from bs4 import BeautifulSoup as bs
    import pprint
    import re
    page = requests.get(url)

    if str(page.status_code) == '400' or str(page.status_code) == '500':
        exit("probable error")

    soup = bs(page.content, 'html.parser')
    listOfPrices = list(soup.find_all('td'))

    stringSearch = re.compile(r"\>(.*?)\<")
    itemsAndPrices = {}

    for i in range(int(len(listOfPrices))):
        listOfPrices[i] = str(listOfPrices[i])
        if listOfPrices[i][0:21] == '<td class="prcl-fir">':
            item = stringSearch.search(str(listOfPrices[i])).group(1)
            price = stringSearch.search(str(listOfPrices[i+2])).group(1)
            itemsAndPrices.update( {item : price} )

    restaurantAndItems =
    return itemsAndPrices




urls = ['https://www.dandykat.com/menu/blaze-pizza/index.html',
        'https://www.dandykat.com/menu/dominos-pizza/index.html',
        'https://www.dandykat.com/menu/foxs-pizza-den/index.html',
        'https://www.dandykat.com/menu/godfathers-pizza/index.html',
        'https://www.dandykat.com/menu/imos/index.html',
        'https://www.dandykat.com/menu/hungry-howies-pizza/index.html',
        'https://www.dandykat.com/menu/jets-pizza/index.html',
        'https://www.dandykat.com/menu/little-caesars-pizza/index.html',
        'https://www.dandykat.com/menu/marcos-pizza/index.html',
        'https://www.dandykat.com/menu/mountain-mikes-pizza/index.html',
        'https://www.dandykat.com/menu/papa-johns-pizza/index.html',
        'https://www.dandykat.com/menu/pdq-pizza/index.html',
        'https://www.dandykat.com/menu/peter-piper-pizza/index.html',
        'https://www.dandykat.com/menu/pie-five-pizza/index.html',
        'https://www.dandykat.com/menu/pizza-hut/index.html',
        'https://www.dandykat.com/menu/pizza-inn/index.html',
        'https://www.dandykat.com/menu/pizza-ranch/index.html',
        'https://www.dandykat.com/menu/pizza-patron/index.html',
        'https://www.dandykat.com/menu/pizzarev/index.html',
        'https://www.dandykat.com/menu/round-table-pizza/index.html',
        'https://www.dandykat.com/menu/toppers-pizza/index.html']

import pprint

for url in urls:
    pprint.pprint(pageRead(url))
