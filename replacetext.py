# importing the list of symbols that we have created. This can be increased as per the requirement
from listofkeys import*

# This function is used to replace the any part of the text generated from our list of symbols if there is a match


def text_replace(text):
    # Creating a duplicate array
    newtext = text.split(" ")
    # Looping through the enitire text that we have received
    for everyword in newtext:
        for key in replace_list.keys():
            # compare spoken word and symbol data set. If the spoken word matches, replace the word with it's symbol
            if(everyword.lower() == key):
                # replacing the word with it's corresponding symbol
                newtext[newtext.index(everyword)] = replace_list[key]
                pass

    return " ".join(newtext)
