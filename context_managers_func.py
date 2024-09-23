################################################################################
######################### CONTEXT MANAGER WITH FUNCITON ########################
################################################################################

from contextlib import contextmanager

@contextmanager
def myopenfile(path_, mode_, encoding_ = 'utf8'):
    try:
        file = open(path_, mode_, encoding = encoding_)
        yield file
    
    except Exception as e:
        print('Attention, occurred an error: ', e.__class__.__name__)
        print('Class of error: ', e.__class__)
    
    finally:
        file.close()
        print('File was success closed.')
    
################################################################################
################################## OPERATIONS ##################################
################################################################################

with myopenfile('context_managers_func.txt', '+a') as file:
    file.write('Hi! This is a test of context manager make with a function and \
decorator.\n')


print('Code completed.')