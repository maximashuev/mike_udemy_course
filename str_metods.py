

# print("=== Модификация регистра ===")
# target="Python:Best course!"
#
# print(target.lower())#lower the hole str
# print(target.upper())#upper the hole str
# print(target.capitalize())#capitalize the first letter
# print(target.title())#capitalize first letter of each word
# print(target.swapcase())#swap case each letter
#
# print("===Delete unnecessary===")
# word="   ...,,,hello?....    "
# print(word.strip())#delete spaces on the eges
# print(word.strip("?.! ,?"))#delete specific characters
# print(word.lstrip(":?.! ,?"))
# print(word.rstrip(":?.! ,?"))

# print("=== String check ===")
# target="Alpha12"
#
# print(target.isalnum())#Return True if the string is an alpha-numeric string(both letters and numbers), False otherwise.
# print(target.isalpha())#Return True if the string is an alphabetic string, False otherwise.
# print(target.islower())#Return True if the string is a lowercase string, False otherwise.
# print(target.istitle())#Return True if the string is a title-cased string, False otherwise.
# print(target.isdigit())#Return True if the string is a digit string, False otherwise.
# print(target.isupper())#Return True if the string is an uppercase string, False otherwise.


# print("=== Length modifiers ===")
# a="test"
# b="some long test string"
# c="10.00"
# #
# # print(a.zfill(44))#Pad a numeric string with zeros on the left, to fill a field of the given width
# # print(b.zfill(100))#Pad a numeric string with zeros on the left, to fill a field of the given width
# # print(c.zfill(10))#Pad a numeric string with zeros on the left, to fill a field of the given width
#
# print(a.center(9))
# print(a.center(9,"_"))
# print(b.center(9,"_"))
# print(c.center(10,"*"))


# print("=== Search metods ===")
# target="Python:Best course!"
#
# print(target.endswith("se!",0,len(target)))#
# print(target.startswith("Py",0,len(target)))#
# print("Python"in target)
# print(target.find("thon"))#return -1 if not match
# print(target.index("Best"))#return Error if not match

# print("=== More helpful methods ===")
# target="Python:Best course!"

# print(target.replace("t","RRR",1))#
#
# table=target.maketrans("Pn:","As_")
# print(target.translate(table))

# print(target.split("t"))#Return a list of the words in the string, using sep as the delimiter string.
# print(list(target))

# print(target.partition("hon"))
# l=["H","e","l","l","o"]
# print("".join(l))