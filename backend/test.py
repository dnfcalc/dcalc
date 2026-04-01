from core.basic.character import createCharacter

char = createCharacter('GF.gunner_female.spitfire_female')

char.calc_init({'oaths': {'0': {'id': '2010201', 'adaptation': 3}, '11': {'id': '2050200', 'adaptation': 0}}, 'equips': {}})


for oath in char.charOathInfo:
    print(oath.id, oath.adaptation, oath.oathInfo.position, oath.oathInfo.max_adaptation, oath.oathInfo.Point)
