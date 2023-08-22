def solve(s):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    values = {char: ord(char) - 96 for char in consonants}
    max_value = 0
    current_value = 0
    for char in s:
        if char in values:
            current_value += values[char]
            max_value = max(max_value, current_value)
        else:
            current_value = 0
    return max_value
