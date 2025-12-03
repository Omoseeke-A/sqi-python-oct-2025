# cities = ["Lagos", "Abuja", "Kano", "Ibadan", "Benin City"]
# newlist = [x for x in cities if "a" in x]
# print(newlist)
# new = [x for x in range(15) if x<=5]
# print(new)

languages = ["Python", "Java","Java","Javelin", "C++", "JavaScript", "Ruby"]
# new_language = [x if x!="Javascript" else x=="Typescript" for x in languages]
# print(new_language)
dicto = {lang:languages.count(lang) for lang in languages}
print(dicto)

names = []