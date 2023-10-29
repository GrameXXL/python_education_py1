# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):
    first_group = set(group1.split(separator))
    second_group = set(group2.split(separator))
    common_participants = list(first_group.intersection(second_group))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(f"Общие участники: {find_common_participants(participants_first_group, participants_second_group, separator='|')}")



