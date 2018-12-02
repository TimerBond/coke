import requests
import csv
from pprint import pprint
import pandas as pd


def main():
    login = '4702014096'
    password = 'waFB3rT$'
    auth(login, password)


def auth(login, password):
    session = requests.Session()
    params = {
        'main_login': login,
        'main_password': password
    }
    session.post('https://edu.tatar.ru/logon',
                 headers={'Referer': 'https://edu.tatar.ru/start/logon-process'},
                 params=params)
    term_parsing(session.get('https://edu.tatar.ru/user/diary/term').text)


def term_parsing(html):
    pd.read_html(html)[0].to_csv('term.csv')
    all_marks = {}
    sr = ''
    with open('term.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for el in reader:
            if len(el[0]) > 0:
                if el[1] == 'ИТОГО':
                    sr = el[2]
                else:
                    sub = el[1]
                    marks_of_sub = list(map(lambda x: int(float(x)),
                            list(filter(lambda x: x != '', el[2:-5])))) \
                            + [float(el[-5])]
                    all_marks[sub] = marks_of_sub
    term_to_csv(all_marks, sr)


def term_to_csv(marks, sr):
    with open('all_marks.csv', 'w') as csv_file:
        fieldnames = ['Предмет', 'Оценки', 'Средний балл']
        writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        sr_all = []
        for subj in marks:
            sr_of_subj = marks[subj][-1]
            sr_all.append(sr_of_subj)
            marks_of_subj = marks[subj][:-1]
            writer.writerow({'Предмет': subj, 'Оценки': marks_of_subj, 'Средний балл': sr_of_subj})
        writer.writerow({'Предмет': 'Все', 'Оценки': sr_all, 'Средний балл': sr})


if __name__ == '__main__':
    main()
