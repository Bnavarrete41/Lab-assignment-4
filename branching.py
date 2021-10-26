# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year= int(input("Greetings! What is your year of origin?")) # corrected parenthesis, quotation mark, and = sign.

if year <= 1900:  # added :
    print("Woah, that's the past!")  # added end of quote and fixed print
elif year > 1900 & year < 2020:         # erased extra &
    print("That's totally the present!")
elif year > 1900 & year > 2020:         # added the expression to make print true
    print("Far out, that's the future!!")
