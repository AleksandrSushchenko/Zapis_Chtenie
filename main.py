import os

print('________________Задача 1_____________________')
cook_book = {}
with open('recept.txt', 'r', encoding='utf8') as f:
    for line in f:
        naz_bludo = line
        bludo = []
        kol_indig = f.readline()
        for i in range(int(kol_indig)):
            stroka = f.readline()
            produkt, kol, ed_izm = stroka.split(' | ')
            sostav_produkta = {'indigrient_name': produkt, 'quantity': kol, 'measure': ed_izm.strip()}
            bludo.append(sostav_produkta)
        recept = {line.strip(): bludo}
        f.readline()
        cook_book.update(recept)

print(cook_book)
print('________________Задача 2_____________________')

e = {}
dishes = []


def get_shop_list_by_dishes(dishes, person_count):
    for i in dishes:
        f = cook_book.get(i)
        for j in f:
            f = {
                j.get('indigrient_name'): {'quantity': int(j.get('quantity')) * int(person_count),
                                           'measure': j.get('measure')}
            }
            e.update(f)
    print(e)


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)

print('________________Задача 3_____________________')

s={}
with open('1.txt', 'r', encoding='utf8') as f1:
    s1 = {os.path.basename('1.txt') : len(f1.readlines())}
    s.update(s1)

with open('2.txt', 'r', encoding='utf8') as f2:
    s2 = {os.path.basename('2.txt') : len(f2.readlines())}
    s.update(s2)

with open('3.txt', 'r', encoding='utf8') as f3:
    s3 = {os.path.basename('3.txt') : len(f3.readlines())}
    s.update(s3)

sorted_tuples = sorted(s.items(), key=lambda item: item[1])
#sorted_dict = {k: v for k, v in sorted_tuples}
print(sorted_tuples)
with open('4.txt', 'w') as p:
    a = sorted_tuples[0][0]
    b = sorted_tuples[0][1]
    print(a)
    p.write(a)










