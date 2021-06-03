from readdata import read_data
from printing import print_comparison
from computation import compute_heatindex

# Colomn names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5, 'heatindex':13} 

# Data types for each column (only if non-string)
types = {'tempout': float,'humout': float, 'heatindex': float}

# Read the data file
data = read_data(columns,types=types)

# Running the function to compute heat index
heatindex = []
for temp, humout in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp,humout))

# DEBUG
#for wc_data, wc_comp in zip(data['windchill'],windchill):
#    print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data-wc_comp:.5f}')

# Output comparison of data
print_comparison('heatindex',data['date'],data['time'],data['heatindex'],heatindex)


# DEBUG
#for datum in data [0:10:2]: #[start:stop:step]
#    print(datum)
#print(data[8])
#print(data[8][0:-1:2])
#print(data['tempout'])

#for i,j in zip([1,2],[3,4,5]):
#    print (i,j)


















