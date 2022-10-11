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
    for j in range(len(dishes)):
        if dishes[j] in cook_book.keys():
            for i in cook_book[dishes[j]]:
                p = {'quantity': int(i.get('quantity')) * int(person_count), 'measure': i.get('measure')}
                f = {i.get('indigrient_name'): p}
                e.update(f)
            print(e)
        else:
            print('no')

get_shop_list_by_dishes(['Омлет','Фахитос','Утка по-пекински'], 10)
