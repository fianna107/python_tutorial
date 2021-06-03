
def read_data(columns, types={},filename="data/wxobs20170821.txt"):
    """
    Read data from CU Boulder Weather Station data file

    Parameters:
        columns: A dictonary of column names mapping to column indicies
        tyoes: A dictionary of column names mapping the types to which to convert each column of data
        filenames: A string path pointing to the CU Boulder Weather Station data file
    """
    # Initialize my data variable
    data = {}
    for column in columns:
        data[column] = []

    #Read the data file
    with open(filename, 'r') as datafile:
        # read the first 3 lines (header)
        for _ in range (3):
        headerline = datafile.readline()
        print(headerline)
    # read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)

    return data












