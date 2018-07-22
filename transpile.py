import program

def transpile(ast, filename=''):
    prog = program.Program()

    print(ast)
    print
    print '#####################'
    print

    if ast.type == 'stmt_list':
        for t in ast.children:
            print 'Type:', t.type
            if t.type == 'fun':
                prog.get_main_module().add_function(t)
            # else:
            #     prog.get_main_module().add_main_statement(t)

    prog.write_to_file(filename)
