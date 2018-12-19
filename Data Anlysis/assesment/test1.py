import csv
def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    table = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            table.append(row)
    return table

table = read_csv_as_list_dict('batting1.csv',',','"')

#print (table)

def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """
##    dict1 = {}
##    for row in statistics:
##        if row[playerid] in dict1:
##            for field in fields:
##                dict1[row[playerid]][field] = dict1[row[playerid]][field] + int(row[field])
##        else:
##            dict1[row[playerid]] = {}
##            dict1[row[playerid]][playerid] = row[playerid]
##            for field in fields:
##                dict1[row[playerid]][field] = int(row[field])
##    
##    return dict1

    dict1 = {}
    for row in statistics:
        if row[playerid] in dict1:
            for field in fields:
                dict1[row[playerid]][field] += int(row[field])
        else:
            dict1[row[playerid]] = {}
            dict1[row[playerid]][playerid]=row[playerid]
            for field in fields:
                dict1[row[playerid]][field] = int(row[field])
    
    return dict1

dict1 = aggregate_by_player_id(table, 'player', ['atbats','triples'])
print (dict1)