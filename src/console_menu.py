class ConsoleMenu:

    def menu_loop(user_input):
        dict_switch = {
            1: "1: Search Book catalogue",
            2: "2: Borrow",
            3: "3: Return",
            4: "4: Logout"
        }
        print(dict_switch.get(input, "Not A Valid Choice"))

        if dict_switch[user_input] == dict_switch[1]:
            {
                ConsoleMenu.example_function()
            }
        elif dict_switch[user_input] == dict_switch[2]:
            {
                ConsoleMenu.example_function_2()
            }
        elif dict_switch[user_input] == dict_switch[3]:
            {
                ConsoleMenu.example_function_3()
            }
        elif dict_switch[user_input] == dict_switch[4]:
            {
                ConsoleMenu.example_function_4()
            }

    def example_function(self):
        pass

    def example_function_2(self):
        pass

    def example_function_3(self):
        pass

    def example_function_4(self):
pass
