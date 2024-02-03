# Function with Outputs

def format_name(f_name, l_name):
    """
    Take a first and last name and format it to
    return the title case version of the name
    :param f_name:
    :param l_name:
    :return:
    """
    if f_name == "" or l_name == "":
        return "You didn't enter any name"
    return f"Result: {f_name.title()} {l_name.title()}"


print(format_name(
    input("What is your first name? "),
    input("What is your last name? ")
))
