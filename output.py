Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ```python
SyntaxError: invalid syntax
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is <JOUW NAAM HIER>')
Mijn naam is <JOUW NAAM HIER>
>>> print('Mijn naam is Miyaki')
Mijn naam is Miyaki
>>> naam = 'Miyaki'
>>> print(naam)
Miyaki
>>> print(naam.upper())
MIYAKI
>>> print(naam[0:2])
Mi
>>> print(naam[::-1])
ikayiM
>>> leeftijd = 17
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Miyaki ben je al 17 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
18
>>> leeftijd-=1
>>> leeftijd
17
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')

    
Over 1 jaar wordt je 18
>>> elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
    
SyntaxError: invalid syntax
>>> else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')
    # Let op: hier 2x een enter doen!
    
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
    
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> from random import randint
>>> randint(0,1000)
996
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
120
>>> willekeurig_getal
120
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 120
>>> from datetime import datetime
>>> datum = datetime.now()
>>> datum = datetime.now()
>>> print(datum)
2021-09-16 09:36:07.852610
>>> datum.strftime('%A %d %B %Y')
'Thursday 16 September 2021'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'donderdag 16 september 2021'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'giovedì 16 settembre 2021'
>>> 