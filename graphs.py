import csv
import matplotlib.pyplot as plt
import os

filename = "runs.csv"
outputFolder = "graphs"

os.makedirs(outputFolder, exist_ok=True)

with open(filename, newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = list(reader)

sequences = list(zip(*data))
sequences = [[float(value) for value in seq] for seq in sequences]

for i, seq in enumerate(sequences):
    label = headers[i]
    parts = label.replace("p=", "").replace("k=", "").split("_")
    p0 = parts[0]
    k = parts[1]

    seq_trimmed = seq[1:]
    iterations = list(range(1, len(seq_trimmed) + 1))  

    
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, seq_trimmed, color='green')
    plt.title(f"Logistic Sequence: p0 = {p0}, k = {k}")
    plt.xlabel("n (iteration)")
    plt.ylabel("p")
    plt.grid(True)
    plt.xlim(1, 100)
    plt.xticks(range(0, 101, 10))  
    plt.ylim(0, 1)


    sanitized_label = label.replace("=", "").replace(".", "_")
    filepath = f"{outputFolder}/{sanitized_label}.png"
    plt.savefig(filepath)
    plt.close()

print(f"Exported {len(sequences)}")
