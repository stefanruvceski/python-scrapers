
import csv

def read_from_csv(name):
    with open(f'{name}.csv', newline='',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = []
        for row in reader:
            data.append(row)
         
    return data
         
if __name__ == '__main__':
    data = read_from_csv('prodaja')
    for d in data:
        print(f"{d[0]} {d[1]} {d[2]}")