def stringpermutations(_str):
    ll = len(_str)
    if ll == 1:
        return [_str]
    permutations = []
    for ii, cc in enumerate(_str):
        _substr = _str[:ii] + _str[ii+1:]
        permutations += [cc + pp for pp in stringpermutations(_substr)]
    return permutations

if __name__ == '__main__':
    _str = input('Input > ')
    output = ['Output >'] + stringpermutations(_str)
    print('\n'.join(output))
