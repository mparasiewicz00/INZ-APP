import wfdb

#Wczytanie i wyświetlenie sygnału
record = wfdb.rdrecord('a0006', sampto=8000)
wfdb.plot_wfdb(record=record, title='Input signal')


