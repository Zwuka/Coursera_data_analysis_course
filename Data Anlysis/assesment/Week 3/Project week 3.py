"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal
#from pygal.maps.world import COUNTRIES


# countries = {value: key for key,value in COUNTRIES.items()}


def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    countries = {value: key for key, value in plot_countries.items()}
    # Angola : ab
    countries_new = {}

    not_found_countries = set()
    for key in countries:
        if key in gdp_countries:
            countries_new[countries[key]]= key
        else:
            not_found_countries.add (countries[key])


    return countries_new, not_found_countries


def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """

    dict_country_gdp_data = {}
    # make dict for contries Country name: GDP data (need to add log base 10)
    with open(gdpinfo['gdpfile'],'rt',newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   delimiter = gdpinfo['separator'],
                                   quotechar = gdpinfo["quote"])
        for row in csvreader:
            fl_year = row[year]
            try:
                fl_year = math.log(float(fl_year),10)
            except ValueError:
                fl_year = ''

            dict_country_gdp_data[row[gdpinfo['country_name']]] = fl_year


    dict2_country_code_country = {}
    set_not_found_countries = set()

    dict2_country_code_country,set_not_found_countries = \
        reconcile_countries_by_name(plot_countries,dict_country_gdp_data)
    #ab : Anogla, and set of not found

    set_not_found_gdp_data = set()
    dict_country_code_gdp_data = {}
    for key,value in dict2_country_code_country.items():
        if dict_country_gdp_data[value] != '':
            dict_country_code_gdp_data[key] = dict_country_gdp_data[value]
        else:
            set_not_found_gdp_data.add(key)




    return dict_country_code_gdp_data, set_not_found_countries, set_not_found_gdp_data


def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    d_code_gdp = {}
    set1 = set()
    set2 = set()
    d_code_gdp,set1,set2 = build_map_dict_by_name(gdpinfo,plot_countries,year)

    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Gdp data for' + year
    worldmap_chart.add('In'+year, d_code_gdp)
    worldmap_chart.add('1', set1)
    worldmap_chart.add('2'+year, set2)
    worldmap_chart.render_to_file(map_file)
    worldmap_chart.render_in_browser()


    return


def test_render_world_map():
    """
    Test the project code for several years.
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

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES
    #pygal_countries.render_in_browser()
    #1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    # render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    # render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    # render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

# test_render_world_map()



