def pwe_print_lol(the_list, level =1):
    for each_item in the_list:
        if isinstance(each_item, list):
            pwe_print_lol(each_item, level+1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(each_item)

movies = ['The Holy Grail', 1975,
            'The Life of Brian', 91, ['Graham Cahpman',
            ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle']]]

pwe_print_lol(movies)
pwe_print_lol(movies, level =0)
