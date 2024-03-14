import requests

def get_wikipedia_table(api_url, article_title, table_name):
    params = {
        "action": "parse",
        "format": "json",
        "page": article_title,
        "prop": "wikitext"
    }
    response = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)")
    data = response.text
    print(data)

    if "parse" in data:
        wikitext = data["parse"]["wikitext"]["*"]
        # Pobierz zawartość tabeli z wikitext
        table_start = wikitext.find("{{" + table_name)
        if table_start != -1:
            table_end = wikitext.find("|}", table_start)
            table_content = wikitext[table_start:table_end + 2]
            return table_content
        else:
            return "Nie znaleziono tabeli o nazwie: " + table_name
    else:
        return "Nie udało się pobrać danych z API Wikipedia"


api_url = "https://pl.wikipedia.org/w/api.php"
article_title = "List_of_countries_by_GDP_(nominal)"
table_name = "table.wikitable.sortable.sticky-header-multi.static-row-numbers"

table_content = get_wikipedia_table(api_url, article_title, table_name)
print(table_content)
