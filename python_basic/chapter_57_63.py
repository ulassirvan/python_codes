from icecream import ic
cities = ['Los Angeles', 'New York', 'Chicago']
cities.append("Houston")
ic (cities)

idx = ['001', '002', '001', '003', '001']
arama = "001"
ic(idx.count(arama))


text = 'Python programming'
text = text.lower()
ic(text )
characters = list(set(text))
ic(characters)
characters.remove(' ')
characters.sort()
ic(characters)


filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0,"phone.jpg")
filenames.pop()
ic(filenames)

day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']

ic(day1+day2)


techs = ('python', 'java', 'sql', 'aws')
ic(sorted(techs))


hashtags = ['summer', 'time', 'vibes']
ic('#' + '#'.join(hashtags))