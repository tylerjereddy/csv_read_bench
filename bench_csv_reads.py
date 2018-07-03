# compare np.loadtxt() vs. pandas read_csv()
# for simple CSV reading case(s)

import numpy as np
import pandas
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import time

# first create some appropriately-sized simple
# CSV files
list_row_counts = [20, 200, 2000, 20000, 200000]
for row_count in list_row_counts:
    data = np.random.rand(row_count, 3)
    fname = "csv_input_{row_count}.csv".format(row_count=row_count)
    np.savetxt(fname=fname,
               X=data,
               delimiter=',')


# run timings and store data
results_dict = {'numpy': {},
                'pandas': {}}
num_replicates = 10
for row_count in list_row_counts:
    list_numpy_timings = []
    list_pandas_timings = []
    fname = "csv_input_{row_count}.csv".format(row_count=row_count)

    print("row_count:", row_count)
    for replicate in range(num_replicates):
        # first for NumPy
        start = time.time()
        np.loadtxt(fname=fname,
                   delimiter=',')
        end = time.time()
        list_numpy_timings.append(end - start)

        # and now for pandas
        start = time.time()
        pandas.read_csv(fname)
        end = time.time()
        list_pandas_timings.append(end - start)
        print("replicate:", replicate)

    # process the results a bit before storing in dict
    array_numpy_timings = np.array(list_numpy_timings)
    array_pandas_timings = np.array(list_pandas_timings)
    avg_numpy_timings = np.average(array_numpy_timings)
    avg_pandas_timings = np.average(array_pandas_timings)
    std_numpy_timings = np.std(array_numpy_timings)
    std_pandas_timings = np.std(array_pandas_timings)
    results_dict['numpy'][str(row_count)] = {'avg': avg_numpy_timings,
                                             'std': std_numpy_timings}
    results_dict['pandas'][str(row_count)] = {'avg': avg_pandas_timings,
                                             'std': std_pandas_timings}

print("np.__version__:", np.__version__)
print("pandas.__version__:", pandas.__version__)
