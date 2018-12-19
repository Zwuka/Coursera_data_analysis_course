"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal


def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """

    dict_codes = {}
    with open(codeinfo['codefile'],newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                  delimiter = codeinfo["separator"],
                                   quotechar = codeinfo["quote"])
        for row in csvreader:
            dict_codes[row[codeinfo["plot_codes"]]]=row[codeinfo["data_codes"]]

    return dict_codes

# codeinfo = {
#         "codefile": "isp_country_codes.csv",
#         "separator": ",",
#         "quote": '"',
#         "plot_codes": "ISO3166-1-Alpha-2",
#         "data_codes": "ISO3166-1-Alpha-3"
#     }
# dict1 = build_country_code_converter(codeinfo)
# for key,item in dict1.items():
#     print(key, item)

def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.

      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """

    d_compare_cod = build_country_code_converter(codeinfo) #AB:ABA
    d_compare_codes = {}
    for key,item in d_compare_cod.items():
        d_compare_codes[key.upper()]=item
    gdp_countries_new = {}
    for key in gdp_countries:
        key_upper = key.upper()
        gdp_countries_new[key_upper]=key

    dict_codes = {}
    codes_not_found = set()
    for key in plot_countries:
        if key.upper() in d_compare_codes:
            gdp_code_upper = d_compare_codes[key.upper()].upper()
            if gdp_code_upper in gdp_countries_new:
                dict_codes[key]=gdp_countries_new[gdp_code_upper]
            else:
                codes_not_found.add(key)
        else:
            codes_not_found.add(key)

    return dict_codes, codes_not_found


def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """

    gdp_data = {}
    with open(gdpinfo['gdpfile'], newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   delimiter = gdpinfo['separator'],
                                   quotechar = gdpinfo['quote'])
        for row in csvreader:
            fl_year = row[year]
            try:
                fl_year = math.log(float(fl_year),10)
            except ValueError:
                fl_year = ''
            gdp_data[row[gdpinfo["country_code"]]] = fl_year

    #gdp_data = ab:1.111
    codes_plot_gdp = {}
    not_found_code = set()

    codes_plot_gdp,not_found_code = reconcile_countries_by_code(codeinfo,plot_countries,gdp_data)
    plot_data = {}
    no_data = set()
    for key,value in codes_plot_gdp.items(): #ab:ABA
        if gdp_data[value] != '':
            plot_data[key] = gdp_data[value]
        else:
            no_data.add(key)
    return plot_data, not_found_code, no_data

def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """
    d_code_gdp = {}
    set1 = set()
    set2 = set()

    d_code_gdp,set1,set2 = build_map_dict_by_code(gdpinfo,codeinfo,plot_countries,year)
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Gdp data for' + year
    worldmap_chart.add('In' + year, d_code_gdp)
    worldmap_chart.add('No data', set1)
    worldmap_chart.add('Not found code' + year, set2)
    worldmap_chart.render_to_file(map_file)
    worldmap_chart.render_in_browser()


    return


def test_render_world_map():
    """
    Test the project code for several years
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    codeinfo = {
        "codefile": "isp_country_codes.csv",
        "separator": ",",
        "quote": '"',
        "plot_codes": "ISO3166-1-Alpha-2",
        "data_codes": "ISO3166-1-Alpha-3"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1960", "isp_gdp_world_code_1960.svg")

    # 1980
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")

    # 2000
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")

    # 2010
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

# test_render_world_map()