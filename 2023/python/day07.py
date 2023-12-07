def handtype(hand: str):
    cards = list(set(hand))
    ncards = len(cards)
    if ncards == 1:
        return 6  # five of a kind
    elif ncards == 2:
        a = cards[0]
        # b = cards[1]
        alen = list(hand).count(a)
        if alen in [1, 4]:
            return 5  # four of a kind
        elif alen in [2, 3]:
            return 4  # full house
    elif ncards == 3:
        # a, b, c = cards
        lens = [list(hand).count(x) for x in cards]
        if max(lens) == 3:
            return 3  # three of a kind
        if max(lens) == 2:
            return 2  # two pairs
    elif ncards == 4:
        return 1  # one pair
    else:
        return 0


def process(lines, joker=False):
    cards = list("AKQT98765432J") if joker else list("AKQJT98765432")
    data = [[], [], [], [], [], [], []]
    for line in lines:
        hand, bid = line.split()
        bid = int(bid)
        indices = "".join([str(cards.index(c)).zfill(2) for c in hand])
        new_hand = hand
        if joker:
            if "J" in hand:
                handlist = list(set(hand))
                handlist.remove("J")
                if len(handlist) == 0:
                    pass
                else:
                    counts = [hand.count(x) for x in handlist]
                    maxidx = counts.index(max(counts))
                    maxcard = handlist[maxidx]
                    new_hand = new_hand.replace("J", maxcard)
        _type = handtype(new_hand)
        data[_type].append([hand, bid, _type, indices])

    for i in range(len(data)):
        data[i] = sorted(data[i], key=lambda d: d[3])[::-1]

    _rank = 1
    total = 0
    for _d in data:
        for __d in _d:
            total += __d[1] * _rank
            _rank += 1

    print(total)

    return total


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            lines = f.read().splitlines()

    p1 = process(lines)
    p2 = process(lines, joker=True)
