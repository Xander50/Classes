# car = {
#     "Name":"BMW",
#     "Year":2005,
#     "Color":"Black",
#     "Year":

# }

# print(car)
# print(car["Year"])
# print(len(car))

book = {
    "Name":"Harry Potter",
    "Series":["series 1","series 2","series 3", "series 4"],
    "Year":2015,
    "Good":True
}

print(book)
print(type(book))
print(book["Series"])
print(book.get("Series"))
print(book.keys())
print(book.values())
print(book.items())

book["Series"]="series 5"
print(book)

book.update({"Series":["series 1", "series 2","series 3", "series 4","series 5"]})
print(book)

book.update({"Characters":"Harry Potter"})
print(book)

book.pop("Year")
print(book)

book.popitem()
print(book)

book.clear()
print(book)
# person = dict(Name = "Cordin",Age=13,Country="U.S")
# print(person)