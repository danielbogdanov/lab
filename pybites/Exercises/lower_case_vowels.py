VOWELS = "aeiou"
EXTENSIONS = [".mp3", ".jpg", ".jpeg", ".pdf", ".txt", ".mp4", ".png", ".exe"]


def uppercase_vowels(text: str) -> str:
    return_string = ''
    str_split = text.split('.')
    print(str_split)
    if '.' + str_split[-1] in EXTENSIONS:
        for letter in str_split[0]:
            if letter.lower() in VOWELS:
                return_string += letter.upper()
            elif not letter.isalnum():
                return_string += ' '
            else:
                return_string += letter.lower()
        return_string = return_string + '.' + str_split[1]
    else:
        for letter in text:
            if letter.lower() in VOWELS:
                return_string += letter.upper()
            elif not letter.isalnum():
                return_string += ' '
            else:
                return_string += letter.lower()
     
    print(return_string) 
    return return_string


uppercase_vowels('file monk.exe')
uppercase_vowels('data.jpg foul')
uppercase_vowels('_.aBCEDF')
uppercase_vowels('-,.?~a')
