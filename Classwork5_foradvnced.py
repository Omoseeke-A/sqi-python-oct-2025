# movie_genre = ("comedy","romance","thriller","action","adventure","horror","sci-fi","anime","musical")
# list_of_movie_genre = [listout.upper() for listout in movie_genre]
# filter_movie_length = [movie for movie in movie_genre if len(movie) < 6]
# print(filter_movie_length)
# print(list_of_movie_genre)

# all_countries = ["Nigeria","USA","Ghana","UAE","Canada","Switzerland","Japan","Germany","Austarlia","Togo","China"]

# developing_countries = ["Nigeria","Togo","Ghana"]


# developed_countries = [kantiri for kantiri in all_countries if kantiri not in developing_countries]
# # print(developed_countries)
# exception_uae = [country for country in all_countries  if country !="UAE"]
# print(exception_uae)

# checker = {country : country.lower().startswith(("a","e","i","o","u")) for country in all_countries}
# print(checker)

# multiples = [number for number in range(1,100) if number % 3 == 0 and number % 5 ==0]
# print(multiples)

names = ["John","Sara","Amanda","Mike"]
names_with_a = [name for name in names if "a" in name]
print(names_with_a)

animals = ["dog","cat","lion","tiger"]
last_character = [animal[-1] for animal in animals] 
print(last_character)

names = ["John","Sara","Amanda","Mike"]
names_with_a = any((name for name in names if "a" in name))
print(names_with_a)

greetings = ["HELLO", "world", "pyTHon","ROCKS"]
checkupper = all((greeting.isupper() for greeting in greetings ))
print(checkupper)