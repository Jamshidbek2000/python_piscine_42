ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}


# --------------------------------- LIST
# Ordered collection of elements.
# Elements can be of different data types.
# Mutable: Elements can be added, modified, or removed after creation.
# Accessed by index.
# Useful for sequences where order matters and elements might change.

# method 1
ft_list[1] = "World!"

# method 2
# ft_list.insert(1, "Hello!")

# method 3
# ft_list.pop()
# ft_list.append("Hello!")

# --------------------------------- TUPLE
# Ordered collection of elements.
# Elements can be of different data types.
# Immutable: Once created, elements cannot be modified.
# Accessed by index.
# Often used when data should remain constant and ordered.

# method 1
ft_tuple = ("Hello", "Germany!")

# --------------------------------- SET
# Unordered collection of unique elements.
# No duplicate elements allowed.
# Elements can be of different data types.
# Mutable: Elements can be added or removed after creation.
# Useful for storing unique values and membership testing.

# method 1
ft_set.remove("tutu!")
ft_set.add("Heilbronn!")

# --------------------------------- DICTIONARY
# Unordered collection of key-value pairs.
# Keys are unique and immutable (usually strings or numbers).
# Values can be of different data types.
# Mutable: Values can be added, modified, or removed after creation.
# Efficient for key-based access, data mapping, and associations.

# method 1
ft_dict["Hello"] = "42Heilbronn!"

# method 2
# ft_dict.update({"Hello" : "42Heilbronn!"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
