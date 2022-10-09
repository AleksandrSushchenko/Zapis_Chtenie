receptu = []
with open('recept.txt' ,'r', encoding='utf8') as f:
    for line in f:
        bludo = line.strip()
        recept = {'naz_bludo': bludo, 'kol':[]}
        kol_ingr = f.readline()
        for i in range(int(kol_ingr)):
            s=f.readline()
            ingr, kol, ed_izm = s.split(' | ')
            sostav = {'ingr': ingr, 'kol': kol, 'ed_izm': ed_izm}
            recept['kol'].append(kol)
        f.readline()
        receptu.append(recept)





print(recept)
