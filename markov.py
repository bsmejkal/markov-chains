"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path1, file_path2):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path1) as f:
        text1 = f.read()

    with open(file_path2) as f:
        text2 = f.read()

    return text1 + ' ' + text2


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    text_string.strip()
    words = text_string.split()

    i = 0

    words.append(None)

    for word in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)
        
        i = i + 1

    sorted(chains.keys())

    return chains


def make_text(chains):
    """Return text from chains."""

    statement = True

    while statement == True:
        key_names = choice(list(chains.keys()))

        words = [key_names[0], key_names[1]]

        if key_names[0].istitle():
            random_value = choice(chains[key_names])
            statement = False

        else:
            statement = True

    while random_value is not None:
        key_names = (key_names[1], random_value)
        words.append(random_value)
        random_value = choice(chains[key_names])
    
    return " ".join(words)


input_path1 = "gettysburg.txt"
input_path2 = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path1, input_path2)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
