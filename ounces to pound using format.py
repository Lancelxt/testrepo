def convert_weight(ounces):
    pounds= ounces/16
    result= "{} equals to {:.2f} pounds".format(ounces,pounds)
    return result

print(convert_weight(10))
print(convert_weight(50.5))
print(convert_weight(110))