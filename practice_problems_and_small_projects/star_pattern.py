def star_generator(number):
    """
    This function generates the stars string as many times the number.
    """
    char = "*"
    stringg = ""
    for i in range(number):
        stringg = char + stringg
    return stringg


def space_generator(number):
    """
    This function generates the spaces string as many times the number.
    """
    char = " "
    stringg = ""
    for i in range(number):
        stringg = char + stringg
    return stringg


def each_line_stars_list(number_of_lines):
    """
    this function uses both the above functions, takes the number as an input and gives the final list with stars in each line.
    """
    line_count = number_of_lines
    stars_list = []
    space_count = 0

    while line_count > 0:
        no_of_stars = (line_count)*2 - 1

        if space_count == 0:
            stars = star_generator(no_of_stars)
            stars_list.append(stars)
        
        else:
            stars_with_space = space_generator(space_count//2) + star_generator(no_of_stars) + space_generator(space_count//2)
            stars_list.append(stars_with_space)

        line_count = line_count - 1
        space_count = space_count + 2

    return stars_list[::-1]


if __name__=="__main__":
    input_int = int(input("Plz enter the value of n\n"))
    print("your pattern is\n\n\n\n")
    print(each_line_stars_list(input_int))