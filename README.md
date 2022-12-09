# emoji_dictionary
    Look up emojis by keyword or using the emoji itself.

# Commands:
    Type quit, exit, stop, end, or escape to finish.
    Anything else searches the dictionary for emojis.


In the code, the emoji_dictionary is a Python dictionary that maps emoji characters to their corresponding English names. The code then iterates through each key-value pair in the dictionary and prints them out.

After that, the code enters a while loop that prompts the user for input. If the user inputs one of the predefined "quit" words, the loop will terminate. If the user inputs an emoji character that exists in the emoji_dictionary, the corresponding name of the emoji will be printed. If the user inputs a description of an emoji (e.g. "face with tears of joy"), the code will search the emoji_dictionary for any emojis whose names match the description and print them out. Otherwise, if no matching emojis are found, the code will inform the user that no emoji was found fitting that description. Once the loop ends, the code will print a message saying "Okay, let's (quit word).".
