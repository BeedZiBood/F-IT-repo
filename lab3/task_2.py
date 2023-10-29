def find_common_participants(participants_first_group, participants_second_group, delimiter=","):
    participants_first_list = participants_first_group.split(delimiter)
    participants_second_list = participants_second_group.split(delimiter)
    participants_first_set = set(participants_first_list)
    participants_second_set = set(participants_second_list)
    intersection_of_participants = participants_second_set.intersection(participants_first_set)
    intersection_list = list(intersection_of_participants)
    intersection_list.sort()
    return intersection_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
