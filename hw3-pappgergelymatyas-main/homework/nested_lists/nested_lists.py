def nested_lists(records):
    grades = sorted(set(record[1] for record in records))
    second_lowest_grade = grades[1]
    second_lowest_students = [record[0] for record in records if record[1] == second_lowest_grade]
    return sorted(second_lowest_students)
    pass