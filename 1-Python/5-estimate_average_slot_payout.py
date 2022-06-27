def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    """
    average = 0
    for iterations in range(n_runs):
        average += play_slot_machine()
    average = average / n_runs
    """
    # -1 because the operation costs 1$
    return sum([play_slot_machine()-1 for iterations in range(n_runs)])/n_runs
