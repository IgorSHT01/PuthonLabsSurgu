#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5



# distances = {'Moscow': {'London': round(((sites['Moscow'][0] - sites['London'][0]) ** 2
#                                          + (sites['Moscow'][1] - sites['London'][1]) ** 2) ** 0.5
#                                         , 2),
#                         'Paris': round(((sites['Moscow'][0] - sites['Paris'][0]) ** 2
#                                         + (sites['Moscow'][1] - sites['Paris'][1]) ** 2) ** 0.5
#                                        , 2),
#                         },
#              'London': {'Moscow': round(((sites['London'][0] - sites['Moscow'][0]) ** 2
#                                          + (sites['London'][1] - sites['Moscow'][1]) ** 2) ** 0.5
#                                         , 2),

#                         'Paris': round(((sites['London'][0] - sites['Paris'][0]) ** 2
#                                         + (sites['London'][1] - sites['Paris'][1]) ** 2) ** 0.5
#                                        , 2),
#                         },

#              'Paris': {'Moscow': round(((sites['Paris'][0] - sites['Moscow'][0]) ** 2
#                                         + (sites['Paris'][1] - sites['Moscow'][1]) ** 2) ** 0.5
#                                        , 2),

#                        'London': round(((sites['Paris'][0] - sites['London'][0]) ** 2
#                                         + (sites['Paris'][1] - sites['London'][1]) ** 2) ** 0.5
#                                        , 2),
#                        }
#              }

distances2 = {}

def a(x1,x2,y1,y2):
   return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

for i in sites:
   distances2[i] = {}
   for n in sites:
      distances2[i][n] = a(sites[i][0], sites[n][0], sites[i][1], sites[n][1])
print(distances2)



