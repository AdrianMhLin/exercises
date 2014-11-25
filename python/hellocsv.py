import csv

csvfile = open('rock.csv', 'rb')
reader = csv.DictReader(csvfile)


def songs_from_year(year):
	songs = []
	for item in reader:
		if item["Release Year"] == str(year):
			songs.append(item)
	print songs
	print "these are the songs from " + str(year)

songs_from_year(1981)




def number_songs_from_before(year):
	ordered_by_year = []
	for item in reader:
		

