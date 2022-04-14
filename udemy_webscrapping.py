from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


PATH = "/home/philica/Documents/personal/projects/Python/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://ethio-bookstore.com/product-category/amharic-books-%e1%8b%a8%e1%8a%a0%e1%88%9b%e1%88%ad%e1%8a%9b-%e1%88%98%e1%8c%bd%e1%88%90%e1%8d%8d%e1%89%b5/")
main = driver.find_element(By.ID, value='main')
lists =main.find_elements(By.TAG_NAME, value='li')
print("===========================")
books_Info = []
for list in lists:
    try:
        title = list.find_element(By.TAG_NAME, value='h2').text
        price = list.find_element(By.CLASS_NAME, value='price').text
        category = list.find_element(By.CLASS_NAME, value='ast-woo-product-category').text
        book_item = {
            'title':title,
            'price':str(price),
            'category':category
        }
        books_Info.append(book_item)
    except:
        break

df = pd.DataFrame(books_Info)
print(df)



time.sleep(5)
driver.quit()