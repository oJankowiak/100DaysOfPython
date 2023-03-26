#Function with outputs

# def format_name(f_name, l_name):
#     name = (f_name + " " + l_name).title()
#     print(name)

# format_name ("aleskandra", "JanKowiak")

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     print(f"{formated_f_name} {formated_l_name}")


def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name ("aleskandra", "JanKowiak")
print(formated_string)