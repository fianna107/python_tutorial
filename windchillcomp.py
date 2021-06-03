
from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_windchill

# Colomn names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

# Data types for each column (only if non-string)
types = {'tempout': float,'windspeed': float, 'windchill': float}

# Read data from file
data = read_data(columns, types=types)

# Running the function to compute wci
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp,windspeed))

# DEBUG
#for wc_data, wc_comp in zip(data['windchill'],windchill):
#    print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data-wc_comp:.5f}')

# Output comparison of data
print_comparison('WINDCHIll',data['date'],data['time'],data['windchill'],windchill)






# DEBUG
#for datum in data [0:10:2]: #[start:stop:step]
#    print(datum)
#print(data[8])
#print(data[8][0:-1:2])
#print(data['tempout'])

#for i,j in zip([1,2],[3,4,5]):
#    print (i,j)


















