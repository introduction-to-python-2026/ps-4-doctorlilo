def split_before_each_uppercases(formula):
    elements = []
    start = 0
    for i, char in enumerate(formula):
      if char.isupper() and i > 0:
        elements.append(formula[start: i])
        start = i
    elements.append(formula[start:])
    return elements


def split_at_first_digit(formula):
    digit_location =len(formula) 
    for i, char in enumerate(formula):
      if char.isdigit():
        digit_location = i
        prefix = formula[0: digit_location]
        numeric = formula[digit_location: len(formula)]
        break
      else:
        prefix = formula[0: digit_location]
        numeric = 1
    return prefix, numeric
