import pandas as pd
url = "https://www.dias-uteis.pt/data_excel?from=2013-01-01&to=2043-12-01&step=2&cols=31,0,0;31,0,1;31,0,3;31,0,2;&country_code_adding=portugal"
tables_on_page = pd.read_html(url)
# tables_on_page = pd.read_html("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
table = tables_on_page[0]
tables_on_page[3].columns = ["x1", "x1", "x1", "x1", "x1"]
table.to_json("table.json", index=False, orient='table')

tables_on_page[3].iloc[110:120, :]