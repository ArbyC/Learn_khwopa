import csv
import operator


with open('Monthly_Attendance.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    int_csv = []
    header = next(csv_reader)

    for items in csv_reader:
        items[-2] = int(items[-2])
        int_csv.append(items)
    sort_list = sorted(int_csv, key=operator.itemgetter(7), reverse=True)
    print(header)

with open('present.csv', 'w') as f:
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerow(header)
    csv_writer.writerows(sort_list[:100])
