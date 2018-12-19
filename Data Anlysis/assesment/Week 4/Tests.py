import pygal

def true_or_false(input1,input2):
    '''

    int :param input1:
    int :param input2:
    :return: True if input1 > input2
    '''
    if input1 > input2:
        return True
    else:
        return False
#
# pygal_countries = pygal.maps.world.COUNTRIES
# print(pygal_countries)
#
# [-20.0 pts] build_map_dict_by_code(
#     {'min_year': 2000, 'country_name': 'Country Name', 'separator': ',', 'quote': '"', 'max_year': 2005, 'country_code': 'Code', 'gdpfile': 'gdptable1.csv'},
#     {'plot_codes': 'Cd2', 'quote': "'", 'codefile': 'code2.csv', 'data_codes': 'Cd3', 'separator': ','},
#     {'C5': 'c5', 'C2': 'c2', 'C4': 'c4', 'C3': 'c3', 'C1': 'c1'}, '2001')
#
# expected ({'C3': 1.041392685158225, 'C1': 0.30102999566398114}, {'C2', 'C5', 'C4'}, set())
# but received ({}, {'C2', 'C5', 'C3', 'C4', 'C1'}, set()) (Exception: Invalid Keys)
# Expected dictionary {'C3': 1.041392685158225, 'C1': 0.30102999566398114} has a different number of keys than received dictionary {}

x = 'c2'
x2 = 'C2'
print (x.upper() == x2)


build_map_dict_by_code(
    {'max_year': 1958, 'country_name': 'Country Name', 'separator': ',', 'country_code': 'Code', 'gdpfile': 'gdptable2.csv', 'quote': '"', 'min_year': 1953},
    {'separator': ',', 'plot_codes': 'Cd2', 'data_codes': 'Cd1', 'codefile': 'code2.csv', 'quote': "'"},
    {'C4': 'c4', 'C1': 'c1', 'C2': 'c2', 'C5': 'c5', 'C3': 'c3'}, '1953')

expected ({'C2': 0.0}, {'C1', 'C5', 'C3'}, {'C4'}) but received ({}, {'C4', 'C1', 'C5', 'C2', 'C3'}, set()) (Exception: Invalid Keys) Expected dictionary {'C2': 0.0} has a different number of keys than received dictionary {}