from itertools import permutations


def permute(lst):
    perms = permutations(lst)
    return [''.join(perm) for perm in perms]