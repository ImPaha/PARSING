# Парсинг авито
from parsing import Url


def reutnUrl():
    return 'https://www.avito.ru/barnaul?avito_campaign_id=9782518030&utm_campaign=web_google_buyers_c2c_general_all_search_01042020_regother_generic_perf&utm_medium=cpc&utm_source=google&utm_term=%2Bavito&advGeoRedirect=&gclid=CjwKCAjwiOv7BRBREiwAXHbv3FqmJeXwmHH2HzXi4k9OvjQP5laRaUj_kj3jkNZCmYDgMrZ2oEGS6BoCVo8QAvD_BwE'


def returnData():
    return 'title-root-395AQ styles-title-2VgwA title-root_maxHeight-3obWc text-text-1PdBw text-size-s-1PUdo text-bold-3R9dt'


def return_ua():
    return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

urlObj = Url(reutnUrl(), user_agent=return_ua())
result = urlObj.parse(returnData(), 'span')
print(result)
