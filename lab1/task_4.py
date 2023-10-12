users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

visits = len(users)
unique_visits = len(set(users))
dict_of_users = {"Общее количество": visits,
                 "Уникальные посещения": unique_visits}
print(dict_of_users)
