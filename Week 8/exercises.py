from urllib import request
import json
import csv
# Otvoriti url https://api.myjson.com/bins/1cqtp5 (ne zaboraviti read pa decode)
content = json.loads((request.urlopen("http://jsonblob.com/api/1226162686332362752).read()).decode())

# Napisati funkciju koja vraća article na osnovu vrijednosti atributa title
def get_article(title):
    article = list(filter(lambda elem: elem["title"] == title, content["data"]["articles"]))
    return article[0]

artikal = get_article("Apple is Listening")
print(artikal)

'''
# Napisati funkciju koja: 
# Omogućava dodavanje komentara. Prije dodavanja komentara odraditi adekvatnu validaciju (title unique). 
# Ako je unos ispravan u listu se dodaje novi dict oblika {title, author, description}.               
# Napomena: author nije obavezan, tako da ako ga korisnik ne unese, default vrijednost je “anonim”
'''
def insert_new_comment(title, description, author = "anonim"):
    for comment in artikal["comments"]:
        if comment["title"] == title:
            print("Article already exists")
            return

    artikal["comments"].append({"title": title, "author": author, "description":description})

# Brise comment u odnosu na naslov komentara
def delete_comment_by_title(title):
    for comment in artikal["comments"]:
        if comment["title"] == title:
            artikal["comments"].remove(comment)
            break

# Brise komentare u odnosu na autora komentara
def delete_comments_by_author(author):
    for comment in artikal["comments"]:
        if comment["author"] == author:
            artikal["comments"].remove(comment)

# Vraća komentar koji ima vrijednost parametra title
def get_comment_by_title(title):
    for comment in artikal["comments"]:
        if comment["title"] == title:
            return comment

# Vraća komentare koji imaju vrijednosti za autora vrijednost parametra author
def get_comments_by_author(author):
    result = []
    for comment in artikal["comments"]:
        if comment["author"] == author:
            result.append(comment)
    return result

# Funkcija koja vraća sve articles na osnovu imena autora
def get_articles_by_author(author):
    articles = list(filter(lambda elem: elem["author"] == author, content["data"]["articles"]))
    return articles

articles = get_articles_by_author("Marco Arment")

# Odabrane articles (po autoru) treba upisati u CSV fajl sortirane po broju komentara 
def sort_by_views(article):
    return article["views"]

sorted_by_views = sorted(articles, key=sort_by_views)

with open('sort_by_views.csv',"w", newline='') as csvfile:
    fieldnames = ["title", "author", "description", "category", "views", "comments"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for elem in sorted_by_views:
        writer.writerow(elem)

def sort_by_comments(article):
    return len(article["comments"])

# # Odabrane articles (po autoru) treba upisati u JSON fajl sortirane po broju pregleda
sort_by_comments = sorted(articles, key=sort_by_comments)

with open("sort_by_comments.json", "w", encoding="utf-8") as json_file:
    json.dump(sort_by_comments, json_file, ensure_ascii=False) 
