NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    return list(dict.fromkeys([name.title() for name in names])) 


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    return sorted(dedup_and_title_case_names(names), key=lambda name: name.split()[-1], reverse=True)
    # ...


def shortest_first_name(names):
    """Returns the shortest first name (str).
    You can assume there is only one shortest name.
    """
    return min(dedup_and_title_case_names(names), key=lambda name: len(name.split()[0])).split()[0]

print(dedup_and_title_case_names(NAMES))
print(shortest_first_name(NAMES))
