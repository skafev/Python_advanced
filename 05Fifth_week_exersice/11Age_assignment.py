def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        for name_initial, age in kwargs.items():
            if name_initial == name[0]:
                result[name] = age
    return result

