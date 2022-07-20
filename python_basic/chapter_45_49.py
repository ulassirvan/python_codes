from icecream import ic

subjects = {'mathematics', 'biology'}
subjects.add("engils")
ic(subjects)

text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}
yalın_text=text.replace(" ","").replace(".","").lower()
letters = set(yalın_text)
consonants = letters.difference(vowels)
ic(f'Number of items: {len(consonants)}')

is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
result = is_clicked.intersection(is_bought)
ic(f'Customer ID: {result}')