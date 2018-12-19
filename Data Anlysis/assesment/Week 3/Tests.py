import csv
import math
import pygal
#from pygal.maps.world import COUNTRIES


# countries = {value: key for key,value in COUNTRIES.items()}
#
# build_map_dict_by_name({'separator': ',', 'gdpfile': 'gdptable1.csv', 'country_name': 'Country Name',
#                         'country_code': 'Code', 'quote': '"', 'min_year': 2000, 'max_year': 2005},
#
#                        {'C4': 'Country4', 'C2': 'Country2', 'C5': 'Country5', 'C1': 'Country1', 'C3': 'Country3'}, '2003')
# expected ({'C2': 1.1139433523068367, 'C1': 0.6020599913279623},
#           {'C4', 'C3', 'C5'}, set())
# x = math.log(2953333419,10)
