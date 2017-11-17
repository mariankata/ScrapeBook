#import urlopen from urllib2 to call an URL address and get HTML from it
from urllib2 import urlopen

#import BeautifulSoup to parse data out of HTML
from BeautifulSoup import BeautifulSoup

#open CSV file
csv_file = open("mail_list.csv", "w+")

url = "https://scrapebook22.appspot.com/"

#we use urlopen from urllib2 to open (URL) and .read() the HTML from it
response = urlopen(url).read()

#we use BeautifulSoup to parse data out of our (HTML)
soup = BeautifulSoup(response)

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = url + link["href"]
        person_html = urlopen(person_url).read()
        person_html_soup = BeautifulSoup(person_html)
        person_name = person_html_soup.find("div", attrs={"class": "col-md-8"}).h1.string
        person_email = person_html_soup.find("span", attrs={"class": "email"}).string
        #When for attributes nothing comes after the :, put True ?? for things to work :)
        person_city = person_html_soup.find("span", attrs={"data-city": True}).string
        print person_name + ", " + person_email + ", " + person_city

        #write data in CSV file
        csv_file.write(person_name + ", " + person_email + ", " + person_city + "\n")

#close CSV file
csv_file.close()