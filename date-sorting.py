### This script checks your .pdf or .txt or .docx file for dates and creates
### an orderly sheet with all dates. It is aimed at lawyers who oftentimes have
### to deal with huge amount of dates. Structuring all dates from a file
### can be time consuming labor. This script aims to fix this.


#imports
import re
print(' ----- Ihr Datenblatt: ------')
f = open('demofile_2.txt', encoding="utf8")

search_this_text = (f.read())
match_obj = re.findall(r"[0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9]", search_this_text)

# print(type(match_obj))
# print(match_obj)

daten_blatt = open('Datenblatt.txt', 'w+')
daten_blatt.write('______________________________  \n')
daten_blatt.write('      D A T E N B L A T T  \n')

print('Jahr | Monat | Tag')
# print(type(match_obj))

my_list_1 = []
for match in match_obj:
    # print(match)
    sorti_1 = match[6:10]
    # print(sorti_1)
    
    sorti_2 = match[3:6]
    # print(sorti_2)
    
    sorti_3 = match[0:3]
    # print(sorti_3)

    rearange = sorti_1 + sorti_2 + sorti_3
    rearange_2 = rearange.replace('.', '')
    # print(rearange_2, '\n')
    # print(type(rearange_2))
    my_list_1.append(rearange_2)

#Ergebnis:
# print(my_list_1) ### alle Elemente sind jetzt nach umgekehrt, nämlich nach Jahr, Monat, Tag sortiert


my_list_2 = []
for i in my_list_1:
    neu_int = int(i)
    # print(type(neu_int))
    my_list_2.append(neu_int)


#Ergebnis:
# print(my_list_2) ### alle Elemente in my_list_2 sind jetzt integer


my_list_2.sort()
# print(my_list_2)

numma = 0
for i in my_list_2:
    numma = numma + 1
    print(f'\nNr.', numma)
    schdring = str(i)
    print(schdring[6:9]+'.'+schdring[4:6]+'.'+schdring[0:4])
    daten_blatt.write('Nr.')
    daten_blatt.write(str(numma)+'\n')
    daten_blatt.write(schdring[6:9]+'.'+schdring[4:6]+'.'+schdring[0:4]+'\n')
    daten_blatt.write('Information: >>> ' + '\n \n \n')