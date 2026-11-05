def stringMatching(words):
    result = []

    for i, word in enumerate(words):
        if any(word in other for j, other in enumerate(words) if i != j):
            result.append(word)

    return result
print(stringMatching(["mass","as","hero","superhero"]))