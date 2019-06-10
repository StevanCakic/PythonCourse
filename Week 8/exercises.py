from urllib import request
import json

# 1. Otvoriti url https://api.myjson.com/bins/1cqtp5 (ne zaboraviti read pa decode)
# TODO

# 2. Napisati sledece funkcije:
    # a) insert_new_comment (title, author, description)
        # Omogućava dodavanje komentara. Prije dodavanja komentara odraditi adekvatnu validaciju (title unique). 
        # Ako je unos ispravan u listu se dodaje novi dict oblika {title, author, description}.               
        # Napomena: author nije obavezan, tako da ako ga korisnik ne unese, default vrijednost je “anonim”
    # b) delete_comment_by_title (title)
        # Brise comment u odnosu na naslov komentara
    # c) delete_comments_by_author (author)
        # Brise komentare u odnosu na autora komentara
    # d) get_comment_by_title (title)
        # Vraća komentar koji ima vrijednost parametra title
    # e) get_comments_by_author (author)
        # Vraća komentare koji imaju vrijednosti za autora vrijednost parametra author

# TODO

# Idemo ka prakticnijoj postavci (niko vam u praksi nece reci kako da imenujete funkcije)
# Takodje, niko vam nece reci sta funkcija treba da radi, sta od podataka da primi, itd
# 3. Napisati sledece funkcije:
    # a) Funkcija koja vraća sve articles na osnovu imena autora
    # b) te article treba upisati u  
    #   b1) CSV fajl sortirane po broju komentara  
    #   b2) JSON fajl sortirane po broju pregleda

# TODO




