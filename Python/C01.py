from math import *
a=0.555
print('######################################## FUNKCJE MATEMATYCZNE ########################################')
print('zmienna a= ',a)
print('po zaokroagleniu poleceniem round() wyglada tak: ', round(a))
print('to jest pi wypisane dzieki(from math import): ', pi)
print('to jest wartosc sinusa(2)', sin(2))
print('wartosc pierwiastka z 9: ', sqrt(9))
print('e do 10: ', pow(e,10))
print('inna komenda na e do 10: ', e**10)
print('logarytm z cwiczen: ', (log10(5+(sin(8))**2))**(1/6))
print('zaokraglenie w dol: ', floor(3.55))
print('zaokraglenie w gore: ', ceil(4.80))

print('/////////////////////////////////////////////////////')
print(u"polskie znaki: światło")
imie = u'RAFAŁ'
nazwisko = u'JAGIELSKI'
print('zamiana wielkosci liter: '+imie.capitalize()+' '+nazwisko.capitalize())
piosenka= 'la la la la lalala'
print('zliczanie wyrazow: ', piosenka.count('la'))
dowolna= 'lubie placki'
print('odwolanie do znakow w stringu przez podanie ich indeksu: ', dowolna[1]+' '+dowolna[len(dowolna)-1])
print('podzial string: ', piosenka.split(' '))
print('zmiennne w stringu: a=%(zm)d' % {'zm':12})
lista= [1,2,3,4]
print('elementy listy w stringu:  %(z1)d %(z2)s' %{'z1':lista[0], 'z2':lista[1]})
fl=1.5
lancuch='abcd'
szes= 9
print('formatowanie w stringu: fl=%(f)f , lancuch=%(l)s , szes=%(s)x' %{'f':fl, 'l':lancuch, 's':szes})
lista2=['ala', 3.14, 2, 1e30, [1,2,3]]
print('zdeklarowana lista:\n', lista2)
lista2.append('ostatni')
print('append(ostatni) do listy: \n', lista2)
lista2.insert(2, 'kot')
print('insert do listy kot na pozycje 2: \n', lista2)
lista2.pop()
print('usuniecie ostatniego indeksu z listy: \n', lista2)
lista2.pop(0)
print('usuniecie wyrazu o zerowym indeksie z listy: \n', lista2)
lista2.remove(3.14)
print('usuniecie wyrazu z listy znajac jego wartosc: \n', lista2)
del lista2[1]
print('usuniecie po indeksie: \n', lista2)
lista2.extend((9,8,7,6))
print('rozszezenie listy poleceniem extend: ', lista2)
lista3=[1,2,3,4,5,6]
print('kolejna lista: \n',lista3)
del lista3[1:5]
print('usuwanie wyrazow z listy po zakresie indeksu: \n',lista3)
i=0
arg =[]
while i<9:
    x=(pi/4)*i
    arg.append(x)
    i+=1

for item in arg:
    print(item,'=>',sin(item))

zdanie = 'lubie placki z miodem i jagodami'
wyrazy =zdanie.split(' ')
print(zdanie)
print(wyrazy)
slownik = {'czarny':'zenek', 'bialy':'stefan', 'czerwony':'wlodzimierz'}
print(slownik['czarny'])


