from re import split
from typing import List

from string import ascii_lowercase

TEXT = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so you can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""


def slice_and_dice(text: str = TEXT) -> List[str]:
    """
    Get a list of words from the passed in text.
    See the Bite description for step by step instructions
    """
    word_list = text.split('\n')
    return_list =[]
    for word in word_list:
        word = word.lstrip()
        print("word is:" + word)
        if len(word) > 0:
            if word[0] == word[0].lower() and word[0].isalnum():
                print("lower:"+word)
                word = word.rstrip('!')
                word = word.rstrip('.')
                return_list.append(word.split()[-1])
            
    return return_list

print(slice_and_dice())

