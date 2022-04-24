from random import choice
 
noun = ['пони', 'анус', 'синхрофазатрон', 'погромист', 'хуй', 'шланг', 'гцц', 'соснолька', 'хуита', 'говно', 'питушня', 'лалка', 'питон', 'енот', 'ватник', 'пидорашка', 'шиндос', 'линупс', 'жопа', 'дед мороз']
verb = ['срёт', 'падает', 'бесит', 'пиздит', 'летает', 'сосёт', 'бегает']
adj = ['сраный', 'ёбаный', 'розовый', 'коричневый', 'охуенный', 'пиздатый', 'тупой', 'ебучий', '']
 
templates = [
    [adj, noun, verb],
    [adj, noun],
    [noun, ['говно']],
    [['У тебя'], adj, noun, verb],
    [['У тебя'], adj, noun],
    [['Какого хуя'], adj, noun, verb, ['\b?']],
    [['Почему'], noun, verb, ['\b?']],
    [['Что такое'], noun, ['\b?']],
    [adj, noun, verb, 'и', verb],
    [noun, verb, ['\b, a'], noun, verb],
]
 
bububu = lambda: (lambda s: s[0].capitalize() + s[1:] + (choice('.!?') if s[-1] not in '.!?' else ''))(' '.join(i for i in map(choice, choice(templates)) if i))
 
 
for _ in range(30):
    print(bububu())