"""Generate Markov text from text files."""

from random import choice, randint


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as f:
        text = f.read()

    return text


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
    words_list = []


    text_string.strip()
    words = text_string.split()

    words_list.extend(words)

    i = 0

    for word in range(len(words_list) - 2):
        key = (words_list[i], words_list[i + 1])
        value = [words_list[i + 2]]

        if key in chains:
            chains[key].extend(value)
        else:
            chains[key] = value

        i = i + 1

    sorted(chains.keys())

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    keys_list = []
    tuple_list = []

    for key in chains:
        keys_list.extend(key)

    # i = randint(0, len(keys_list) - 2)

    # key1 = (keys_list[i], keys_list[i + 2])

    # print(key1)

    # words.extend(key1)

    i = 0

    for word in range(len(keys_list)):
        key_set = (keys_list[i], keys_list[i + 1])
        tuple(key_set)

        tuple_list.append(key_set)
        
        i = i + 2

        if i >= len(keys_list):
            break

    first_key = choice(tuple_list)
    words.extend([first_key[0]])

    while choice(chains[first_key]) != 'am?':
        key1 = ((first_key[1], choice(chains[first_key])))

        print(key1)

        list(key1)

        words.extend([key1[1]])

        first_key = key1

    print(words)

    words.extend(['am?'])

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
