import logo  # imported the logo python file

# created a list with all the alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

# print the logo form logo.py(which we imported)
print(logo.logo)


# created the encode function
def encode(words, shift):  # initiated the function with words and shift as input
    # created an empty list in which the individual words of the sentence will be stored and there is only one word
    # it will still work as there can be only 1 element in a list
    vals = []
    # loop through the words list
    for j in words:
        # create an empty string variable
        ans = ''
        # loop through the letters of the word from the words list
        for i in j:
            # create a variable and store the index of the letter in it
            loc = alphabets.index(i)
            # create a new variable and store the new index in it
            new_loc = loc - shift
            # edge case when the new index becomes less than -26
            if new_loc < (-26):
                mult = (new_loc * (-1)) // 26
                new_loc = new_loc + (mult * 26)
            # add the new letter in the ans variable to create a word after encoding
            ans += alphabets[new_loc]
        # now append the word in the empty list we created
        vals.append(ans)
    # print the whole sentence by joining the words with a space between them
    print(' '.join(vals))
    # taking an input from the user if the user want to continue using the program
    cont = input('Do you want to continue??(yes or no)')
    # return the value of the cont to the while loop
    return cont


# created the decode function
def decode(words, shift):  # initiated the function with words and shift as input
    # created an empty list in which the individual words of the sentence will be stored and there is only one word
    # it will still work as there can be only 1 element in a list
    vals = []
    # loop through the words list
    for j in words:
        # create an empty string variable
        ans = ''
        # loop through the letters of the word from the words list
        for i in j:
            # create a variable and store the index of the letter in it
            loc = alphabets.index(i)
            # create a new variable and store the new index in it
            new_loc = loc + shift
            # edge case when the new index becomes greater than 25 (in alphabets list the indexing starts from 0)
            if new_loc > 25:
                mult = new_loc // 26
                new_loc = (new_loc - (mult * 26))
            # add the new letter in the ans variable to create a word after encoding
            ans += alphabets[new_loc]
        # now append the word in the empty list we created
        vals.append(ans)
    # print the whole sentence by joining the words with a space between them
    print(' '.join(vals))
    # taking an input from the user if the user want to continue using the program
    cont = input('Do you want to continue??(yes or no)')
    # return the value of the cont to the while loop
    return cont


# made a variable cont(short for continue) to make the while loop stop later
cont = 'yes'

# created a while loop which will go until the value of cont is 'no'
while cont != 'no':
    # taking the input of the user on what process to initiate - encode or decode?
    process = input('What do you want to do ?? encode or decode:').lower()
    # taking the input from the user on which the process should be applied
    word = input('Enter a string:')
    # if the input has more than 1 word in-short a sentence then to deal with it I created another list in which
    # individual words are saved
    words = word.split(' ')
    # taking the input of the user on how much the shift is required
    shift = int(input('How much is the shift:'))

    # if the user input for process is 'encode' then the next 2 lines will run
    if process == 'encode':
        cont = encode(words, shift)
    # else these next 2 lines will run
    else:
        cont = decode(words, shift)
