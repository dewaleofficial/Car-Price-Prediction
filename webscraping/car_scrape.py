import time
import requests
from bs4 import BeautifulSoup as bs


def get_soup(url):
    r = requests.get(url)
    # create a beautiful soup object
    soup = bs(r.content, "lxml")
    return soup


def get_data(min: int = 1, max: int = 84):
    import csv

    pages = []
    for n in range(min, max + 1):
        time.sleep(0.2)
        url = (
            f"https://buy.cars45.com/cars?page={n}"
        )
        pages.append(url)

    # create csv file
    with open("cars_data.csv", "w", encoding="utf-8") as f:
        col_names = ["make", "mileage", "year", "condition", "price"]
        # instantiate
        my_csv = csv.writer(f, delimiter=",")

        # add the column names
        my_csv.writerow(col_names)

        for i, url in enumerate(pages):
            try:
                soup = get_soup(url)
                body = soup.find_all('figcaption')
            except:
                soup = None
                body = None
            for idx, row in enumerate(body):
                if idx < len(body) - 3:
                    try:
                        make = row.find('h4').get_text(strip=True).split('C45')[0]
                    except:
                        make = None
                    try:
                        mileage = row.find_all(class_ = 'text-small mb-1')[0].get_text().split(':')[1]
                    except:
                        mileage = None
                    try:
                        year = row.find_all(class_ = 'text-small mb-1')[1].get_text().split(':')[1]
                    except:
                        year = None
                    try:
                        condition = row.find(class_ = 'd-none d-sm-block').text
                    except:
                        condition = None
                    try:
                        price = row.find(class_ = 'price').text.split('₦')[1]
                    except:
                        price = None
                    

                    # write the files into my_csv object
                    my_csv.writerow([make, mileage, year, condition, price])


if __name__ == "__main__":
    get_data(1, 80)
    # 1 80