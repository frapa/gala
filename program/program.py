import context
import modules

class Program(context.CodeObject):
    def __init__(self):
        super(Program, self).__init__(None)

        self.main_module = modules.Module(self, 'main');

    def get_main_module(self):
        return self.main_module

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.main_module.to_c())