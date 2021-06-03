

def print_comparison(name, dates, times, original_data, computed_data):
    """
    Print a comparison of two timeseries (original & computed)

    Parameters:
        name: A string name for thr data being compared (limited to 3 characters in length)
        dates: List of strings representing dates for each data
        times: list of strings representing times for each data
        original_data: List of original data (floats)
        computed_data: List of computed data (floats)
    """
    # Output comparison of data
    print('                Original  Computed')
    print(f' Date    Time  {name.upper():>9} {name.upper():>9} Difference')
    print('------- ------ --------- --------- ----------')
    zip_data = zip(dates,times,original_data,computed_data)
    for date, time, orig, comp in zip_data:
        diff = orig - comp
        print(f'{date} {time:>6} {orig:9.6f} {comp:9.6f} {diff:10.6f}')


