import csv


# Updating csv files
def update_file_csv(path_in: str, path_to: str):
    op = open(path_in, "r")
    dt = csv.DictReader(op)
    up_dt = []
    for r in dt:
        print(r)
        row = {'intent': r['\ufeffintent'], 'value': r['value']}
        up_dt.append(row)
    print(up_dt)
    op.close()
    op = open(path_to, "a", newline='')
    headers = ['intent', 'value']
    data = csv.DictWriter(op, delimiter=',', fieldnames=headers)
    data.writerow(dict((heads, heads) for heads in headers))
    data.writerows(up_dt)

    op.close()


# Only when this is the original executable file is the condition true
if __name__ == '__main__':
    # update_file_csv('ancillary.csv', 'answers.csv')
    update_file_csv('ancillary.csv', 'questions.csv')
    # pass
