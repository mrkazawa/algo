"""
Tony is not a morning person and is late for work with 0.5 probability. Andy is a generous
supervisor, so tries not to care for Tony's being late. But Andy scolds Tony if Tony is late
for work three times in a row. Calculate the probability that Tony is not being scolded at
all if he has attended for twenty days.

Ian is also not a morning person and is late for work with 2/3 probability. Calculate the
probability that Ian is not being scolded by Andy at all if he has attended for twenty days.
"""

import sys
sys.setrecursionlimit(100) # just a safeguard :)

def prob_of_consecutive_late(num_days, late_limit, late_prob, saved=None):
    """ Returns the probability of the employees getting n numbers of
        consecutive late.

    Parameters:
        num_days        the total number of days that the employee works
        late_limit      the total of late allowable before the employee
                        start getting scolded
        late_prob       the late probability of the employee
        saved           the DP aspect of the algorithm, no need to calculate
                        already calculated value from the previous step

    Returns:
        result          the late probability

    """
    if saved == None: saved = {}
    ID = (num_days, late_limit, late_prob)

    if ID in saved: return saved[ID]
    else:
        if late_limit > num_days or num_days <= 0:
            result = 0;
        else:
            result = late_prob ** late_limit
            for firstLate in range(1, late_limit+1):
                pr = prob_of_consecutive_late(num_days - firstLate, late_limit, late_prob, saved)
                result += (late_prob ** (firstLate - 1)) * (1 - late_prob) * pr

        saved[ID] = result
        return result

# test for employee Tony
print('Tony work for n days, probability of not getting scolded at all')
scolded_prob = 1 - prob_of_consecutive_late(3,3,0.5)
print('n = 3; probability =', scolded_prob)
scolded_prob = 1 - prob_of_consecutive_late(7,3,0.5)
print('n = 7; probability =', scolded_prob)
scolded_prob = 1 - prob_of_consecutive_late(14,3,0.5)
print('n = 14; probability =', scolded_prob)
scolded_prob = 1 - prob_of_consecutive_late(21,3,0.5)
print('n = 21; probability =', scolded_prob)

# test for employee Ian
print()
print('Ian work for n days, probability of not getting scolded at all')
scolded_prob = 1 - prob_of_consecutive_late(3,3,0.666)
print('n = 3; probability =', scolded_prob)
scolded_prob = 1 - prob_of_consecutive_late(7,3,0.666)
print('n = 7; probability =', scolded_prob)
scolded_prob = 1 - prob_of_consecutive_late(14,3,0.666)
print('n = 14; probability =', scolded_prob)
scolded_prob = 1 - prob_of_consecutive_late(21,3,0.666)
print('n = 21; probability =', scolded_prob)