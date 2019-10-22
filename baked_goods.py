# calculate_purchasing_plan - provides a strategy to minimize costs
# to a family receiving bread deliveries from sellers that turn up to a 
# pre-defined schedule.  The family starts out with 10 loaves of bread that goes 
# stale after 30 days.  There are N days on which bakers will deliver bread for a price
# After total_days, bread will be freely available again.


def empty(interval):
    return interval[1] <= interval[0]


# precondition:
# lhs <= rhs - ie: lhs[0] <= rhs[0] && lhs[1] <= rhs[1]
def intersect(lhs, rhs):
    if lhs[1] > rhs[0]:
        return [rhs[0], lhs[1]]
    else:
        return None


# precondition:
# lhs = [l_begin, l_end], rhs = [r_begin, r_end]
# lhs <= rhs - ie: lhs[0] <= rhs[0] && lhs[1] <= rhs[1]
def diff(rhs, lhs):
    if lhs[1] > rhs[0]:
        return [lhs[1], rhs[1]]
    else:
        return None


# precondition: interval = [begin, end]
def length(interval):
    return interval[1] - interval[0] if interval[1] > interval[0] else 0;


# check if stale
def is_stale(total_days, sellers):
    if sellers[0][0] > 10 or total_days - sellers[-1][0] > 30:
        return True
    last_day = sellers[0][0]
    for day, _ in sellers:
        if day - last_day > 30:
            return True
        else:
            last_day = day

    return False


# precondition
# total_days > 0
# sellers = [(t0, p0), ..., (tn, pn)], t0 < ... < tn, pi >= 0
# NOTE - we do not assume that total_days > ti.
def calculate_purchasing_plan(total_days, sellers):
    # we have fewer days to go than loaves of bread,
    # don't have to buy
    if total_days <= 10:
        return [0] * len(sellers)

    if is_stale(total_days, sellers):
        return None

    num_sales = len(sellers)
    # total_days may not be at the end of the sellers schedule ...
    intervals = [[dt, min(dt + 30, total_days)] for (dt, price) in sellers]

    for i in range(num_sales):
        (dt, price_i) = sellers[i]
        interval = intervals[i]

        if not empty(interval):
            end = interval[1]
            j = i + 1
            while j < num_sales and end >= intervals[j][0]:
                price_j = sellers[j][1]
                if price_j < price_i:
                    intervals[i][1] = intervals[j][0]
                else:
                    intervals[j][0] = intervals[i][1]
                j += 1

    return [length(interval) for interval in intervals]
