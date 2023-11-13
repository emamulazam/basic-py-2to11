def build_preson(first_name, last_name, age=''):
    "Return a full name, neatly formatted"
    person = {'first': first_name, 'last': last_name}
    if age:
        person["age"] = age
    return person

musiician = build_preson('jimi', 'hendix', age= 27)
print(musiician)