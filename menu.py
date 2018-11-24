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
            itemsAndPrices.update({item : price})



    restaurantName = re.compile(r"<title>(.*?) Menu and Prices Today - Dandy Kat</title>")
    name = restaurantName.search(str(soup.find_all('title')))
    if name != None:
        name = name.group(1)
    else:
        name = '#NNF#'

    return [name, itemsAndPrices]





urls = ['https://www.dandykat.com/menu/blaze-pizza/index.html',
        'https://www.dandykat.com/menu/dominos-pizza/index.html',
        'https://www.dandykat.com/menu/foxs-pizza-den/index.html',
        'https://www.dandykat.com/menu/godfathers-pizza/index.html',
        'https://www.dandykat.com/menu/imos/index.html',
        'https://www.dandykat.com/menu/hungry-howies-pizza/index.html',
        'https://www.dandykat.com/menu/jets-pizza/index.html',
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

while (1):
    s = int(input('''Type the number in front of the restaurant:
    1. Blaze Pizza
    2. Domino's Pizza
    3. Fox's Pizza Den
    4. Godfather's Pizza
    5. Imo's Pizza
    6. Hungry Howie's Pizza
    7. Jet's Pizza
    8. Marco's Pizza
    9. Mountain Mike's Pizza
    10.Papa John's Pizza
    11.Pdq Pizza
    12.Peter Piper Pizza
    13.Pie Five Pizza
    14.Pizza Hut
    15.Pizza Inn
    16.Pizza Ranch
    17.Pizza Patron
    18.PizzaRev
    19.Round Table Pizza
    20.Toppers Pizza

    '''))
    pprint.pprint(pageRead(urls[s-1]))
    input()
    print('\n
