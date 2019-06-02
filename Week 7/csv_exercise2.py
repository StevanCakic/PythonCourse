import csv

# Zadatak: Izracunati za koji dan se desio najveci skok, a za koji dan najveci
# pad akcija, za 2014. godinu. Porediti akcije na otvaranju i zatvaranju berze
# za svaki dan i naci min i max. Posmatra se procentualna razlika ovih vrijednosti,
# a ne razlika izmedju vrijedosti. Rezultate prikazati kao dictionary sledeceg oblika:
# {biggest_perc_jump: 
#   {date: <datetime>, open: <float>, close: <float>, difference: <float>}
#  biggest_perc_drop:
#   {date: <datetime>, open: <float>, close: <float>, difference: <float>}
# }