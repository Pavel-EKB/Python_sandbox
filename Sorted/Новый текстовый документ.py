class Snake(object):
    def __init__(self, name, toxicity, aggression):
        self.name = name
        self.toxicity = toxicity
        self.aggression = aggression

    def __repr__(self):
        return "<%s>" % self.name

gardenSnake = Snake('gardenSnake', 10, 0.1)
rattleSnake = Snake('rattleSnake', 100, 0.25)
kingCobra = Snake('kingCobra', 50, 1.0)
snakes = [rattleSnake, kingCobra, gardenSnake]

def byDangerous_key(snake):
    return snake.toxicity * snake.aggression

result = sorted(snakes, key = byDangerous_key)
print(result) # [<gardenSnake>, <rattleSnake>, <kingCobra>]

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
print (name, languages in favorite_languages[1])