# Task 1
def get_budgets(lst_budgets):
    return sum([user['budget'] for user in lst_budgets])
print(get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]))

# Task 2
def get_student_names(dict_names):
    return sorted(dict_names.values())

print(get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}))
print('----------------')
# Task 3
def identical_filter(words):
    new_list = []
    for word in words:
        word_set = set(word)
        if len(word_set) == 1:
            new_list.append(word)
    return new_list


print(identical_filter(["aaaaaa", "bc", "d", "eeee", "xyz"])) # ["aaaaaa", "d", "eeee"]
print('----------------')


# Task 4
def validate_subsets(subsets, one_set):
    one_set = set(one_set)
    for number in subsets:
        number_set = set(number)
        if not number_set.issubset(one_set):
            return False
    return True

print(validate_subsets([[1, 2], [2, 3], [1, 3]], [1, 2, 3]))
print(validate_subsets([[1, 2, 3, 4]], [1, 2, 3]))

# Task 7
def color_invert(rgb):
    l = []
    for i in rgb:
        l.append(255 - i)
    return tuple(l)

print(color_invert((165, 170, 221)))

# Task 8
def check(dict1, dict2, key_ch):
    if key_ch not in dict1 and key_ch not in dict2:
        return "Not found"
    elif key_ch not in dict1 or key_ch not in dict2:
        return "One's empty"
    elif dict1[key_ch] == dict2[key_ch]:
        return True
    else:
        return "Not the same"

dict_first = {"sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright"}
dict_second = {"people": 12, "sun": "star", "book": "bad"}
print(check(dict_first, dict_second, "sun"))
