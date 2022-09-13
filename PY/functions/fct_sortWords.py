def sort_words(input):
    return ' '.join(sorted(input.split(), key = str.casefold))
 
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))




# Notes
# input='banana ORANGE apple'
# input.split() # splits the content by spaces into a list
# sorted(input.split(), key = str.casefold) # Sorts the elements in the list
# ' '.join(sorted(input.split(), key = str.casefold)) # Joins it all back together

