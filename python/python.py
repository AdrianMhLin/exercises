
Write a function that takes prints all the even numbers between 1 and 10,000.
def even_numbers_to_10000():
	for i in range(1,10000):
		if i % 2 == 0:
			print i



Write a function that returns a list of the numbers between 1 and 10,000 that are divisible by 3.
def numbers_3():
	amazing_list = []
	for i in xrange(1,10000): #xrange is more efficient, doesnt load to memory
		if i % 3 == 0:
			amazing_list.append(i)

	return amazing_list


The same as 2, but use Python list comprehensions
????

random = ["bob", "mike", "adam", "octopus", "erasmus"]

print [name for name in random if "b" in name]





syllables = ["bob", "tob", "ack", "ko", "im", "a", "lap"]

print [d for d in syllables if d[0] in ["a","e","i","o","u"] ]

def get_closed_syllables(list):
	closed_syllable_list = []
	for syllable in list:
		if syllable[-1] not in ["a","e","i","o","u"]:
			closed_syllable_list.append(syllable)
	return closed_syllable_list

get_closed_syllables(syllables)






print [i for i in xrange(1,10001) if i% 3 == 0]

Write a function get_max that takes a list of numbers and returns the max of those numbers, 
don't use the builtin max() function. Afterward, try using max()'

def get_max(list):
	max = float("-inf")
	for item in list:
		if item > max:
			max = item
	return max



"Write a function is_odd_or_div_by_7 that returns True if a number is odd or divisble by 7 and False otherwise." 
"Then write it using a lambda function."

def is_odd_or_div_by_7(num):
	if num % 2 != 0 or num % 7 == 0:
		return True
	else:
		return False


Use is_odd_or_div_by_7 and list comprehensions to write a function get_sublist_of_numbers_odd_or_div_by_7 that takes in a list 
and returns a sublist of those numbers that are either odd or divisible by 7.

def get(list):
	new_list = []
	print [item for item in list if is_odd_or_div_by_7(item)]



Given a list of food orders, e.g. ["burger", "fries", "burger", "tenders", "apple pie"], 
write a function get_aggregate_order_counts that takes the list and returns a dictionary with the different dishes as keys and 
the number of times they appear in the list as the values. For example, it takes ["burger", "fries", "burger", "tenders", "apple pie"] and 
outputs  { "burger": 2, "fries": 1, "tenders": 1, "apple pie": 1 }

def food(list):
	hist = {}
	for dish in list:
		if dish in hist:
			hist[dish] += 1
		else:
			hist[dish] = 1	
	return hist



Use collections.Counter to achieve the same functionality.
print collections.Counter(list)


Write a function get_most_popular_order_data that takes a list of orders but instead of returning a dictionary with the counts, 
it just outputs a tuple: the dish that appears the most in the list and the number of times it appears in the list. 
So the output given the example would be ("burger", 2)

def mode_food(list):
	# hist = food(list)
	# popular = {}
	# for pair in hist:
	# 	if pair

	print collections.Counter(list).most_common(1)[0]




# Lambda function is an anonymous function
def is_equal_to_7(number):
    return number == 7

other_is_equal_to_7 = lambda number: number == 7





fav_movies = [{"name": "Shawshank Redemption", "imdb_score": 8.7, "fb_fan_count": 900000}, {"name": "Never Say Never", "imdb_score": 1.2, "fb_fan_count": 80000000}, {"name": "Interstellar", "imdb_score": 7.7, "fb_fan_count": 1200000}]

# def get_imdb_score(movies):
# 	return movie["imdb_score"]

# get_fan_count = lambda movie: movie["fb_fan_count"]

print sorted(fav_movies, key=lambda movie: movie["fb_fan_count"])

syntaxes = [{"order": "SVO", "percent": 0.4}, {"order": "SOV", "percent": 0.5}, {"order": "VSO", "percent":0.1}]
sorted(syntaxes, key=lambda syntax: syntax["percent"], reverse=True)



