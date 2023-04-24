from collections import OrderedDict
from enum import Enum
from functools import partial


def return_longest_non_overlapping(matches):
    final_matches = OrderedDict()
    previous_end = -1
    for match in sorted(matches, key=lambda x: x.start_ix):
        start_ix = match.start_ix
        end_ix = match.end_ix
        if start_ix >= previous_end or (start_ix in final_matches and end_ix > final_matches[start_ix].end_ix):
            final_matches[start_ix] = match
            previous_end = end_ix
    return list(final_matches.values())


def return_all(matches):
    return matches


def return_first_non_overlapping(matches):
    final_matches = OrderedDict()
    previous_end = -1
    for match in sorted(matches, key=lambda x: x.start_ix):
        start_ix = match.start_ix
        end_ix = match.end_ix
        if start_ix >= previous_end:
            final_matches[start_ix] = match
            previous_end = end_ix
    return list(final_matches.values())


class MatchMode(Enum):
    ALL = partial(return_all)
    LONGEST_NON_OVERLAPPING = partial(return_longest_non_overlapping)
    FIRST_NON_OVERLAPPING = partial(return_first_non_overlapping)
