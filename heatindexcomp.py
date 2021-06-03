from readdata import read_data

# Colomn names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5, 'heatindex':13} 

# Data types for each column (only if non-string)
types = {'tempout': float,'humout': float, 'heatindex': float}

# Initialize my data variable
data = {}
for column in columns:
    data[column] = []

# Read the data file
data = read_data(columns,types=types)

# Compute the heat index 
def compute_heatindex(t,hum):
    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = 0.22475541
    e = 0.00683783
    f = 0.05481717
    g = 0.00122874
    h = 0.00085282
    i = 0.00000199
   
    rh = hum/100

    hi = (a+(b*t)+(c*rh)+(d*t*rh)+(e*t**2)+(f*rh**2)+(g*rh*t**2)+(h*t*rh**2)+(i*t**2*rh**2))
    return hi



# Running the function to compute heat index
heatindex = []
for temp, humout in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp,humout))

# DEBUG
#for wc_data, wc_comp in zip(data['windchill'],windchill):
#    print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data-wc_comp:.5f}')

# Output comparison of data
print('                Original  Computed')
print(' Date    Time  HeatIndex HeatIndex Difference')
print('------- ------ --------- --------- ----------')
zip_data = zip(data['date'],data['time'],data['heatindex'],heatindex)
for date, time, hi_orig, hi_comp in zip_data:
    hi_diff = hi_orig - hi_comp
    print(f'{date} {time:>6} {hi_orig:9.6f} {hi_comp:9.6f} {hi_diff:10.6f}')


# DEBUG
#for datum in data [0:10:2]: #[start:stop:step]
#    print(datum)
#print(data[8])
#print(data[8][0:-1:2])
#print(data['tempout'])

#for i,j in zip([1,2],[3,4,5]):
#    print (i,j)


















