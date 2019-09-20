foods = {}
        main_menu = print('Main menu\n1: add\n2: delete\n3: view\n4: exit\n--------')
        options = int(input('\nEnter menu number: '))

        while options != 4:
            if options == 1:
                    food = input('Food name: ')

                            if food in foods:
                                        print(food, 'is already in foods.')
                                                    quty = int(input('How many?: '))
                                                                foods[food] = quty + foods[food]

                                                                        else:
                                                                                    quty = int(input('How many?: '))
                                                                                                foods[food] = quty
                                                                                                        for item in foods:
                                                                                                                    print('\n',item,':',foods[item])
                                                                                                                        elif options == 2:
                                                                                                                                food = input('Food name:')

                                                                                                                                        del(foods[food])

                                                                                                                                                for item in foods:
                                                                                                                                                            print('\n',item,':',foods[item])
                                                                                                                                                                elif options == 3:
                                                                                                                                                                        for item in foods:
                                                                                                                                                                                    print('\n',item,':',foods[item])

                                                                                                                                                                                        options = int(input('\n\nEnter menu number: '))
