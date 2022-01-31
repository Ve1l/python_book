def search4vowels(phrase: str) -> set:
    """Возвращает гласные, найденные в указанном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


print(search4vowels('argumentiruy'))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Возвращает множество букв из "letters", найденных в указанной фразе."""
    return set(letters).intersection(set(phrase))


print(search4letters('argumentiruy'))
