# compare np.loadtxt() vs. pandas read_csv()
# for simple CSV reading case(s)

import numpy as np
import pandas
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

# first create some appropriately-sized simple
# CSV files
list_row_counts = [20, 200, 2000, 20000, 200000]
for row_count in list_row_counts:
    data = np.random.rand(list_row_counts, 3)
    fname = "csv_input_{row_count}.csv".format(row_count=row_count)
    np.savetxt(fname=fname,
               X=data,
               delimiter=',')


# run timings and store data


