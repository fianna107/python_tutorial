
# Colomn names and column indices to read
columns = {'date':0,'time':1,'tempout':2}

# Data types for each column (only is non-string)
types = {'tempout':float}

# Initialize my data variable
data = {}
for column in columns:
    data[column] = []

# Initialize my data variable
data = {'date':[], 'time':[],'tempout':[]}

#Read the data file

filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:
    # read the first 3 lines (header)
    for _ in range (3):
        datafile.readline()
    # read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)





# DEBUG
#for datum in data [0:10:2]: #[start:stop:step]
#    print(datum)
#print(data[8])
#print(data[8][0:-1:2])
print(data['tempout'])




















