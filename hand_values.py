'''Take a set of cards and determine the strongest hand value.
'''

hand_values = ('Highcard', 'Pair', 'Two pairs', 'Three of a kind', 'Straight', 'Flush', 
                'Full house', 'Four of a kind', 'Straight flush', 'Royal flush')

def determine_hand_value(cards):
    #test if cards are valid hand and fit criteria
    #give best possible hand from cards
    print('done')


def count_suits(cards):
    clubs = 0
    diamonds = 0
    hearts = 0
    spades = 0
    for i in cards:
        if i[1] == 'c':
            clubs += 1
        elif i[1] == 'd':
            diamonds += 1
        elif i[1] == 'h':
            hearts += 1
        elif i[1] == 's':
            spades += 1
    return {'clubs': clubs, 'diamonds': diamonds, 'hearts': hearts, 'spades': spades}



def test_flush(cards):
    if len(cards) >= 5:
        suit_count = count_suits(cards)
        print(suit_count)
        for i in suit_count:
            if suit_count[i] >= 5:
                return 'y'
            else:
                return 'n'
    else:
        return 'n'


print('Testing flush!')
print(test_flush(['As', 'Ks', 'Qs', 'Js', 'Ts']))
print(test_flush(['Ac', 'Kd', 'Qc', 'Jh', 'Th', '9h']))
print(test_flush(['Ah', 'Jc', 'Qh', 'Jh', 'Jd']))