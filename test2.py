import requests
from bs4 import BeautifulSoup
import pandas as pd


start_url = "https://en.wikipedia.org/wiki/List_of_cities_by_GDP"
download_html = requests.get(start_url)

soup = BeautifulSoup(download_html.text)
with open('downloaded.html', 'w', encoding="utf-8") as file:
    file.write(soup.prettify())

print(soup)
full_table = soup.select("table.wikitable.sortable.jquery-tablesorter")
# print(full_table)

# table_head = full_table.select('tr td')
# # print(table_head)

# print("--------------")
# for element in table_head:
#     print(element.text)

# table_columns = []
# for element in table_head:
#     column_label = element.get_text(separator=" ", strip=True)
#     column_label = column_label.replace(' ', '_')
#     # column_label = regex.sub('', column_label)
#     table_columns.append(column_label)
#     # print(column_label)
    
# print('-------------')
# print(table_columns)

table_rows = full_table.select('tr')

table_data = []
for index, element in enumerate(table_rows):
    if index > 0:
        row_list = []
        values = element.select('td')
        for value in values:
            row_list.append(value.text.strip())
        table_data.append(row_list)

print(table_data)
