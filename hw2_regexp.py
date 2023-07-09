from pprint import pprint
import csv
import re

def extra_data(contacts_list):    
    for num, contact in enumerate(contacts_list):
        if len(contact) > 7:
            del contacts_list[num][7:]
    return contacts_list

#  Task 1
def full_name_task1(contacts_list):
    for num, contact in enumerate(contacts_list):
        if len(contact) > 7:
            del contacts_list[num][7:]

        first_name_split = re.split(re.compile("\s"), contact[0])
        if len(first_name_split) == 3:
            contact[0:3] = first_name_split
        elif len(first_name_split) == 2:
            contact[0:2] = first_name_split
        else:
            last_name_split = re.split(re.compile("\s"), contact[1])
            if len(last_name_split) == 2:
                contact[1:3] = last_name_split
    return contacts_list

# Task 2
def phones_task2(contacts_list):
    pattern = re.compile(r"(\+7|8)\s?[\(\-)]?(\d{3})[\)\-]?\s?(\d{3})[\s\-]?(\d{2})[\s\-]?(\d{2})(\s?)\(?(доб.)?\s?(\d{4})?\)?")
    for contact in contacts_list:
        if contact[-2]:
            contact[-2] = pattern.sub(r"+7(\2)\3-\4-\5\6\7\8", contact[-2])
    return contacts_list

#  Task 3
def duplicates_task3(contacts_list):
    person_dict = {}
    for contact in contacts_list:
        person = ",".join(contact[0:2])
        person_data = contact[2:8]
        if person_dict.get(person):
            for num, data in enumerate(person_dict[person]):
                if data == "":
                    person_dict[person][num] = person_data[num]
        else:
            person_dict[person] = person_data

    contacts_list_new = []
    for name, data in person_dict.items():
        person_full  = name.split(",") + data
        contacts_list_new.append(person_full)
    return contacts_list_new

if __name__ == "__main__":
    with open("phonebook_raw.csv", encoding ="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    titles = contacts_list[0]
    contacts_list.pop(0)

    contacts_list_extra_data = extra_data(contacts_list)
    contacts_list_task1 = full_name_task1(contacts_list_extra_data)
    contacts_list_task2 = phones_task2(contacts_list_task1)
    contacts_list_task3 = duplicates_task3(contacts_list)
    print(contacts_list_task3)    

    with open("phonebook_new.csv", "w", encoding ="utf-8", newline="") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerow(titles)
        datawriter.writerows(contacts_list_task3)