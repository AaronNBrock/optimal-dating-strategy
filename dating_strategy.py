import random
import math


def dating_strategy(
    past_partners,
    current_partner,
    number_of_potential_partners
):
    """
    Parameters
    ----------
    past_partners : int[]
        a list of the compatability values of all past partners
    current_partner : int
        the compatability value of your current partner
    number_of_potential_partners : int
        the number of remaining partners you could date

    Returns
    -------
    bool
        If you would like to marry the current partner
    """

    return (
        len(past_partners) > (number_of_potential_partners / math.e) and
        current_partner > max(past_partners)
    )


results = []
for _ in range(1000):

    # for the purpases of this program, all partners will be 
    # uniformly generated between 0 and 100 however, it should
    # be noted that one should not assume that will be the case
    potential_partners = [random.randint(0, 100) for _ in range(random.randint(1, 20))]

    for i in range(len(potential_partners)):
        if i == len(potential_partners) or dating_strategy(potential_partners[:i], potential_partners[i], len(potential_partners)):
            results.append(potential_partners[i])
            break

print('Average Result: {}'.format(sum(results) / len(results)))