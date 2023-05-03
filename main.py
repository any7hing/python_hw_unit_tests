geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def filter_logs():
    for i in reversed(range(len(geo_logs))):
        for item in geo_logs[i].items():
            if "Россия" not in item[1]:
                del geo_logs[i]
    return geo_logs


def unique_id():
    sort_list = []
    for item in ids.values():
        for val in item:
            if val not in sort_list:
                sort_list.append(val)
    return sort_list


def max_stats():
    return max(stats.values())


if __name__ == "__main__":
    filter_logs()
    unique_id()
    max_stats()
