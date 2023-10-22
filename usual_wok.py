import math
import sys


def controlFlow():
    number = input("Please enter a number: ")
    if number.isdigit():
        if eval(number) > 0:
            print('Pass !')
        else:
            print('Not Pass !')
    else:
        print("Please enter numbers, Try again!")

controlFlow()


if not False:
    print("it works")


def pay_cal():
    hours = input("plz enter your hours: ")
    if hours.isdigit():
        if 35 >= int(hours) > 0:
            print(f"Your pay is {int(hours)*51.45}")
        else:
            print(f"Your pay is {(int(hours)-35)*88.9 + 35*51.45}")
    else:
        print("plz try again !")

pay_cal()

letters = ['a','b','c','d']
for tup in enumerate(letters[1:]):
    print(tup)

    def find_the_max(lst):
        max = -sys.maxsize - 1
        for i in lst:
            if int(i) > max:
                max = int(i)
        print(f"the largest number is: {max}")

    lst = [3,9,-1,5,7,2,11,0,3,12,3,15]
    find_the_max(lst)

    print(sorted(lst))

    print(max(lst))

    for i in range(1,4):
        for m in range(1,4):
            if m >= i:
                print(i,m)


    a = "Hi"
    if a:
        print(f"{a} There")

    a = 1
    b = 0
    print( a and b)

lst1 = "abcdefg ihj"

print('ihj' in lst1)


def even_number(lst):
    lst1 = []
    for i in lst:
        if i % 2 == 0:
            lst1.append(i)
    return lst1

print(even_number([0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]))

pairs = [('a',1),('b',2),('c',3)]
dic = {m : n for m,n in pairs}
# for m,n in pairs:
#     dic[m] = n

print(dic)

lst1 = [2,3,10,14,20,21,25,13,15]
lst = [x for x in lst1 if x**2 > 150]
print(lst)

numbers = [0,1,1,2,5,6,8,2,4,6,8]
lst = [x for x in numbers if x % 2 == 0]
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(sorted(lst1))
print(lst)

dic = { 'a': 'b', 'c': 'd'}
print(dic)

import pandas as pd

# Part (a)
# Create a pandas series called series_abc with
# index ['a', 'b', 'c'] and values [1, 2, 3]
series_abc = pd.Series(data=[1,2,3], index=['a','b','c'])
print(series_abc)

# Part (b)
# Given the stock price-date dictionary prc_date
# listed below, create a pandas series series_stk
# with the dates as indices and the prices as values.
prc_date = {
    7.1600: '2020-01-02',
    7.1900: '2020-01-03',
    7.0000: '2020-01-06',
    7.1000: '2020-01-07',
    6.8600: '2020-01-08',
    6.9500: '2020-01-09',
    7.0000: '2020-01-10',
    7.0200: '2020-01-13',
    7.1100: '2020-01-14',
    7.0400: '2020-01-15',
    }
series_stk = pd.Series(data=prc_date.keys(), index=prc_date.values())

# Part c
# Given the dictionary
dic = {i:i+1 for i in range(10000)}
# create a Pandas series called series_ones
# with indices from 0 through 9999 and with
# all values equal to 1.
# Do not use a secondary dictionary to create the series in Pandas.
# Instead, specify the data and index arguments directly.
series_ones = pd.Series(data=[1 for x in range (0, 10000)], index=[x for x in range(0,10000)])

import pandas as pd
import numpy as np

aud_usd_lst = [
    ('2020-09-08', 0.7280),
    ('2020-09-09', 0.7209),
    ('2020-09-11', 0.7263),
    ('2020-09-14', 0.7281),
    ('2020-09-15', 0.7285),
    ]

eur_aud_lst = [
    ('2020-09-08',  1.6232),
    ('2020-09-09',  1.6321),
    ('2020-09-10',  1.6221),
    ('2020-09-11',  1.6282),
    ('2020-09-15',  1.6288),
    ]

# Replace unanswered with your solution.
aud_usd_series = pd.Series(data=[y for x,y in aud_usd_lst], index=[x for x,y in aud_usd_lst])
eur_aud_series = pd.Series(data=[y for x,y in eur_aud_lst], index=[x for x,y in eur_aud_lst])
df = pd.DataFrame({'AUD/USD': aud_usd_series, 'EUR/AUD':eur_aud_series})
print(df)

import pandas as pd
import numpy as np


# Write this function
def mk_df(date_info, aud_usd_info, eur_aud_info):
    """ Combines the information from different sources to produce a dataframe
    with dates row labels. Row labels must be sorted

    Parameters
    ----------
    date_info : list
        date_info = [(row_id, date)]

    aud_usd_info : list
        aud_usd_info = [(row_id, aud/usd)]


    eur_aud_info : list
        eur_aud_info = [(row_id, eur/aud)]

    Returns
    -------
    df
    """

    dict1 = {m: n for m,n in aud_usd_info}
    dict2 = {m: n for m,n in eur_aud_info}
    data_dict = {}
    for m,n in date_info:
        data_dict[n] = {'AUD/USD': dict1.get(m), 'EUR/AUD': dict2.get(m)}
    df = pd.DataFrame.from_dict(data_dict, orient='index')
    print(data_dict)
    return df.sort_index(inplace=False)
# Sample data for you to develop your function
# date_info = [(row_id, date)]
date_info = [
    (11, '2020-09-08'),
    (70, '2020-09-09'),
    (99, '2020-09-10'),
    (4, '2020-09-11'),
    (7, '2020-09-14'),
    (100, '2020-09-15'),
]

# aud_usd_info = [(row_id, aud/usd)]
aud_usd_info = [
    (70, 0.7209),
    (4, 0.7263),
    (11, 0.7280),
    (7, 0.7281),
    (100, 0.7285),
]

# eur_aud_info = [(row_id, eur/aud)]
eur_aud_info = [
    (70, 1.6321),
    (4, 1.6282),
    (99, 1.6221),
    (100, 1.6288),
    (11, 1.6232),
]

df = mk_df(date_info, aud_usd_info, eur_aud_info)
print(df)