from bs4 import BeautifulSoup

with open ("100_days_of_python\Day 45\website.html", encoding="utf8") as file:
    contents =  file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title.string)
# print(soup.prettify())
# print(soup.h1)
# print(soup.h1.string)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)