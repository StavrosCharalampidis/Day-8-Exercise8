# Complicated formatting of a String
varFormatter = "{} {} {} {} {} {}"

# Print the complicated formatting with some args
print(varFormatter.format(1, 2, 3, 4, 5, 6))

# Print the (one - six) strings
print(varFormatter.format("one", "Two", "Three", "Four", "Five", "Six"))

# Print the formatting of a String with the variable varFormatter
print(varFormatter.format(varFormatter, varFormatter, varFormatter, varFormatter, varFormatter, varFormatter))

# Print the formatting of a String with some string values
print(varFormatter.format("Try Python", "Is Really", "Good", "Programming", "language", "<3"))