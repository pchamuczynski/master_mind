from random import randrange

def verify_alphabet(secret, alphabet):
    for character in secret:
        if character not in alphabet:
            return False
    return True

def solutions(alphabet, length):
    result = []
    if length == 1:
        for char in alphabet:
            result.append(char)
    else:
        for solution in solutions(alphabet, length - 1):
            for char in alphabet:
                result.append(solution +char)
    return result

def apply(solution, secret):
    match = ""
    other_solution = ""
    other_secret = ""
    for i in range(len(solution)):
        if solution[i] == secret[i]:
            match += solution[i]
        else:
            other_solution += solution[i]
            other_secret += secret[i]
    exact = len(match)
    position = 0
    for i in range(len(other_solution)):
        if other_solution[i] in other_secret:
            position+=1
            other_secret = other_secret.replace(other_solution[i], '', 1)
    return '+' + str(exact) + '-' + str(position)


def solve(secret, alphabet):
    if verify_alphabet(secret, alphabet) == False:
        print ("Secret contains a character not included in the alphabet")
    possible_solutions = solutions(alphabet, len(secret))
    print('original size of possible_solutions: ' + str(len(possible_solutions)))
    while len(possible_solutions) > 1:
        candidate = possible_solutions[randrange(len(possible_solutions))]
        res = apply(candidate, secret)
        result = input('candidate ' + candidate + ': ')
        if result == '':
            candidate = input('candidate:')
            result = input('result:')
        # print('trying ' + str(candidate) + ': ' + str(res))
        possible_solutions = [solution for solution in possible_solutions if apply(solution, candidate) == result]
        print(str(len(possible_solutions)) + ' possible solutions')
    if len(possible_solutions) == 1: return possible_solutions[0]
    return None

print(str(solve('abcde', '1234567890')))