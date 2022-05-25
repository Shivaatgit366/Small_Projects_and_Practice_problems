# Write a Python code to find the longest continuous series of small alphabetic letters in a text.
# e.g. input:"This is just an example123 of an ExtrEmely long string".
# output: "example"


def lower_cased_list(content:str) -> list:
    """
    Returns a list containing lowercased words.
    """
    content_list = content.split()
    lower_cased_list = []

    for item in content_list:
        if item == item.lower():
            lower_cased_list.append(item)
    return lower_cased_list


def string_without_numbers(content:str) -> str:
    """
    Returns only the text content removing the digits.
    """
    newstring = ""
    for i in content:
        if not i.isdigit():
            newstring = newstring + i
    return newstring


def sorted_list(content:str) -> str:
    """
    Takes the string input. Makes a list of lower cased strings, removes digits.
    Sorts the list, returns the final lengthy string.
    """
    content_list = lower_cased_list(content)
    string_without_digits = [string_without_numbers(item) for item in content_list]
    result = sorted(string_without_digits, key=len)
    return result[-1]


if __name__ == "__main__":
    input = "This is just an example123 of an ExtrEmely long string"
    output = sorted_list(input)
    print(output)

