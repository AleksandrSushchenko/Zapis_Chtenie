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
