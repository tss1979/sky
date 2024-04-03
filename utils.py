import json


def load_students():
    with open('students.json') as file:
        students = json.loads(file.read())
        return students


def load_professions():
    with open('professions.json') as file:
        professions = json.loads(file.read())
        return professions


def get_student_by_pk(pk):
    students = load_students()
    result = None
    for student in students:
        if student['pk'] == pk:
            result = student
    return result


def get_profession_by_title(title):
    professions = load_professions()
    result = None
    for profession in professions:
        if profession['title'] == title:
            result = profession
    return result



def check_fitness(student, profession):
    studet_skill = set(student['skills'])
    proff_skill = set(profession['skills'])
    has = list(studet_skill.intersection(proff_skill))
    lacks = list(proff_skill.difference(studet_skill))
    return {
                "has": has,
                "lacks": lacks,
                "fit_percent": int((len(has) / len(proff_skill)) * 100),
            }
