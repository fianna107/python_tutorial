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
        data['date'].append(split_line[0])
        data['time'].append(split_line[1])
        data['tempout'].append(float(split_line[2]))



# DEBUG
#for datum in data [0:10:2]: #[start:stop:step]
#    print(datum)
#print(data[8])
#print(data[8][0:-1:2])
print(data['tempout'])




















