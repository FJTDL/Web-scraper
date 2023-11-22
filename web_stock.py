from bs4 import BeautifulSoup

from selenium import webdriver

buys = []
sells = []
holds = []

def get_data(url):
    dr = webdriver.Firefox()
    dr.get(url)
    bs = BeautifulSoup(dr.page_source,"html.parser")

    category = bs.find(id="ta-list-top-buy-link")
    result = bs.find("span", class_="pl-5 pr-5 pt-3 pb-3 font-weight-600 border-radius-default font-size-16")
    # date = bs.find(lambda tag: tag.name=="small" and "Updated on" in tag.text)

    if result != None:
        result = result.text
    else:
        result = 0.0

    category = category.text
    
    if "Hold" in category:
        holds.append((float(result), url[url.rfind("/")+1:]))

    elif "Buy" in category:
        buys.append((float(result), url[url.rfind("/")+1:]))
    
    else:
        sells.append((float(result), url[url.rfind("/")+1:]))

    dr.quit()




buys.sort(reverse=True)
sells.sort()
holds.sort()

print(f"Buys: {buys}")
print()
print(f"Sells: {sells}")
print()
print(f"Holds: {holds}")     