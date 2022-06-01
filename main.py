def read_names():
    namelist = []
    with open("./Input/Names/invited_names.txt", "r") as name_file:
        name_data = name_file.readlines()
        for names in name_data:
            namelist.append(names.strip("\n"))
        return namelist


def read_letter():
    with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
        letter_data = letter_file.readlines()
        return letter_data


def write_letter(list_of_people, letter_format):
    new_file_list = []
    index = 0
    while index < len(list_of_people):
        new_file_list.append("./Output/ReadyToSend/letter_for_"+list_of_people[index]+".txt")
        with open(new_file_list[index], 'w') as new_file:
            for line in letter_format:
                first_old_line = line
                first_new_line = first_old_line.replace("[name]", list_of_people[index])
                new_file.write(first_new_line)
            index += 1


def main_function():
    people = read_names()
    letter = read_letter()
    write_letter(people, letter)


main_function()
