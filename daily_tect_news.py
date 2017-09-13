import urllib.request, os
from bs4 import BeautifulSoup
from datetime import date

url = "https://www.phonearena.com"
# loading our webpage
page = urllib.request.urlopen(url)
# parsing html
soup = BeautifulSoup(page, 'html.parser')
# collecting headlines from html
headline = soup.find_all('h3', {'class': 'title'})
# assigning today to today's date
today = date.today()

# if file already exists, remove it
# change path of your file before using it
path = '%s_news.txt' %(str(today))
if os.path.isfile(path):
    os.remove(path)

# reading every headline into a newline with numbering
# Note: we're opening our file in append mode
# to use date as file name, convert it into a string
with open(path, 'a') as file:
    i=1
    file.write(str(today)+"\nTech News:\n\n")
    for h in headline:
        file.write("%d. %s.\n" %(i,h.text))
        i += 1  # counter

# opens file after reading data to it
print("Done! Opening the file...\n")
os.startfile(path)







