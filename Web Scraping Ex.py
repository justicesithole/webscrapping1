#Web Scraping

import bs4, webbrowser, requests

try:
    data = requests.get("http://en.wikipedia.org/wiki/Python")
    data.raise_for_status()
    
    my_data = bs4.BeautifulSoup(data.text, "lxml")
    
    print("List of all the header tags: \n\n")
    for the_data in my_data.find_all("a"):
        try:
            print(the_data.attrs["href"])
        except Exception as err:
            print(err)
        
except Exception as err:
    print(err)
    print("\nNo website matches your search.")


