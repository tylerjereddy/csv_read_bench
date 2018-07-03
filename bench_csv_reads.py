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
for row_count in list_row_counts:
    fname = "csv_input_{row_count}.csv".format(row_count=row_count)
    # first for NumPy
    start = time.time()
    np.loadtxt(fname=fname,
               delimiter=',')
    end = time.time()
    print("row_count:", row_count)
    print("NumPy time (s):", end - start)

    # and now for pandas
    start = time.time()
    pandas.read_csv(fname)
    end = time.time()
    print("pandas time (s):", end - start)

print("np.__version__:", np.__version__)
print("pandas.__version__:", pandas.__version__)
