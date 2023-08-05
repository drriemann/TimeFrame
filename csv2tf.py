import csv
import numpy as np

with open('tab.csv') as f:
    reader = csv.reader(f)

    l = len(reader.__next__())
    s = str(' ' * 256)

    data = np.array([[s for _ in range(l)] for _ in range(l)])
    for i, row in enumerate(reader):
        data[i] = row[::]
    print(data)
