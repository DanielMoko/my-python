
#largest no
def greatest():
    numbers = [2,3,4,5,6,7]
    return max(numbers)
print(greatest())
#tuples
wildanimals = ("goose", "lion", "zebra", "gazelle")
print(wildanimals)
animals = list(wildanimals)
print(animals)
animals.append("cheetah") ==[3]
print(animals)
wildanimals = tuple(animals)
print(wildanimals)
#sets
somemovies = {"avengers","dalot", "witcher", "the100"}
somemovies.add("thedictator")
print(somemovies)

somemovies = {"avengers","dalot", "witcher", "the100"}
somemovie=  {"dalot", "witcher", "the100"}
somemovies .update(somemovie)
print(somemovies)

somemovies = {"avengers","dalot", "witcher", "the100", "thedictator"}
somemovies.remove("thedictator")
print(somemovies)
#repeated value
vegetables = ["cheese", "tomatoes", "potatoes", "tomatoes", "ram", "ram"]
repeatedveg = set()
unreapeated =set()
for item in vegetables:
   if vegetables.count(item)>1:
       repeatedveg.add(item)
       print("the reapeated vegetables r:", repeatedveg)
   elif vegetables.count(item)==1:
       unreapeated.add(item)
       print("the unreapeated vegetables r:", unreapeated)




"""
artistik = {
    "name":"moko",git addg
    "time":"midnight",
    "house":"mansion"
}
del artistik["time"]
print(artistik)
"""
vegetables = ["cheese", "tomatoes", "potatoes", "tomatoes", "ram", "ram"]
repeatedveg =[]
for item in vegetables:
   if vegetables.count(item)>1 and item not in repeatedveg:
      repeatedveg .append(item)
print("the reapeated vegetables r:",repeatedveg)
