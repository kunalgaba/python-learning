name = input("camelCase: ")
camel_case_name = ""
for i in range(len(name.strip())):
    if name[i].isupper():
        camel_case_name = camel_case_name + "_" + name[i].lower()
    else:
        camel_case_name += name[i]
print(f"{camel_case_name}")
