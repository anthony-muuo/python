# function with outputs day 10

def format_name(f_name:str, l_name:str):
    first_name= f_name.capitalize()
    last_name =l_name.capitalize()

    full_name = f"{first_name} {last_name}"

    return full_name


print(format_name("anthony ", "MUUO"))

# can also use .title() eg f_name.title()