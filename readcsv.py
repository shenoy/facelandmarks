import numpy as np

def read_csv(filename):
    x = []
    y = []
    with open(filename, 'r') as f:
        for line in f:
            x_val, y_val = line.split(',')
            x.append(x_val)
            y.append(y_val)
    return x, y



x, y = read_csv('csv_files/markzuckerberg.csv')

x_arr = np.array(x)
y_arr = np.array(y)

x_arr = x_arr.astype(float)
y_arr = y_arr.astype(float)
# normalize x
x_norm = x_arr / np.linalg.norm(x)

# normalize y
y_norm = y_arr / np.linalg.norm(y)

print (x_norm)
print (y_norm)


def output_coords_to_csv(x_coords, y_coords, csv_filename):
    with open(csv_filename, 'w') as f:
        for i in range(len(x_coords)):
            x = x_coords[i]
            y = y_coords[i]
            f.write(str(x) + ',' + str(y) + '\n')
    print('Coordinates written to CSV file.')


output_coords_to_csv(x_norm, y_norm, "normalized_csv/markzuckerberg.csv")


