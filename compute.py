import csv

n = 100
p_values = [0.6572, 0.5, 0.892, 0.121, 0.9932, 0.893, 0.891]        
k_values = [1.964343, 1.2345, 2.7852, 3.321, 3.4729, 3.8342]   

filename = "runs.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    header = [f"p={p}_k={k}" for p in p_values for k in k_values]
    writer.writerow(header)

    sequences = []
    for p0 in p_values:
        for k in k_values:
            p = p0
            sequence = []
            for i in range(n):
                sequence.append(p)
                p = k * p * (1 - p)
            sequences.append(sequence)

    for i in range(n):
        row = [seq[i] for seq in sequences]
        writer.writerow(row)
