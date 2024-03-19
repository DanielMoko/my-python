
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
vegetables = ["cheese", "greens", "potatoes", "tomatoes", "ram", "ram"]
repeatedveg = []
for item in vegetables:
   if vegetables.count(item)>1:
      repeatedveg .append(item)
print(repeatedveg)

artistik = {
    "name":"moko",
    "time":"midnight",
    "house":"mansion"
}
print(artistik)