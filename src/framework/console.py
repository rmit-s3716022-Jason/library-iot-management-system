class Console:
    def __init__(self, utility):
        self.states = {}
        self.current_state = None
        self.utility = utility

    def add_state(self, name, state):
        self.states[name] = state

    def set_current_state(self, name):
        self.current_state = self.states[name]

    def run(self):
        while True:
            self.display()
            new_state = self.input()
            if new_state in self.states:
                self.current_state = self.states[new_state]
            elif new_state == "exit":
                break

    def display(self):
        self.current_state.display()

    def input(self):
        input_result = self.current_state.input()
        return self.current_state.handle_input(input_result, self.utility)
