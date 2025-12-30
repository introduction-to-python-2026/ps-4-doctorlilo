def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


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
    print(prefix, numeric)
