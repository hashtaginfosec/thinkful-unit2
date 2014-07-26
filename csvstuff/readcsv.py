import csv
def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["first_name"], line["last_name"])


if __name__ == "__main__":
    with open("data.csv") as f_obj:
        csv_dict_reader(f_obj)