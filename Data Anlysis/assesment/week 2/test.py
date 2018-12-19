import csv

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, 'rt', newline = '') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   delimiter = separator,
                                   quotechar = quote)
        for row in csvreader:
            table[row[keyfield]] = row
    
    return table



def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.

    Output: 
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    
    #table = [(x, float(gdpdata[str(x)])) for x in range(gdpinfo["min_year"], gdpinfo["max_year"]+1)]
    table = []
    for x in range(gdpinfo["min_year"],gdpinfo["max_year"]+1):
        try:
            GDP = float(gdpdata[str(x)])
            table.append((x,GDP))
        except ValueError:
            GDP = 0
    
    return table

    
gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2016,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }
dict1 = read_csv_as_nested_dict('isp_gdp.csv', "Country Name", ',', '"')
dict2 = dict1["Aruba"]
print (dict2)
print (dict2['2003'])
table = build_plot_values(gdpinfo, dict2)
print (table)
