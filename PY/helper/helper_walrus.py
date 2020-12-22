



# Walrus operator in use
data = [1,2,3,4]
f_data = [y for x in data if (y := f(x)) is not 4]

# More efficient than the alternative:
f_data = [f(x) for x in data if f(x) is not 4]
# Which has to run it twice



