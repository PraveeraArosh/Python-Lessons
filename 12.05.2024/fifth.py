val = input("Enter true or False")
def change_model(val : str)->bool:
    var = None
    if val == "true":
        var = False
    if val == "false":
        var = True
    return var


print(change_model(val))



