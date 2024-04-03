import utils

def main():
    while True:
        try:
            pk = int(input('Введите номер студента\n'))
            break
        except:
            print('Введите номер студента - это должно быть число')
    student = utils.get_student_by_pk(pk)
    if student:
        name = student['full_name']
        skills = student['skills']
        print(f'Студент {name}')
        print('Знает', end=' ')
        print(*skills, sep=', ')
        title = input(f'Выберите специальность для оценки студента {name}\n')
        profession = utils.get_profession_by_title(title)
        if profession:
            student_info = utils.check_fitness(student, profession)
            fit = student_info.get('fit_percent') if student_info.get('fit_percent') else 0
            has = student_info.get('has') if student_info.get('has') else ['ничего из того что нужно']
            lacks = student_info.get('lacks') if student_info.get('lacks') else ['? Да все он знает']
            print(f'Пригодность: {fit} %')
            print(f'{name} знает', end=' ')
            print(*has, sep=', ')
            print(f'{name} не знает', end=' ')
            print(*lacks, sep=', ')
        else:
            print('У нас нет такой специальности')
    else:
        print('У нас нет такого студента')

main()
