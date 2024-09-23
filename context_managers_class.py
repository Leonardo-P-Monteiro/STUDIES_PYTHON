
################################################################################
########################## CONTEXT MANAGER WITH CLASS ##########################
################################################################################

class MyOpenFile():

    def __init__(self, path_, mode_, encoding_ = 'utf8'):
        self.path_ = path_
        self.mode_ = mode_
        self.enconding = encoding_

    def __enter__(self):
        try:
            print('Opening the file.')
            self.file = open(self.path_, self.mode_, encoding=self.enconding)
        except Exception as e:
            print('Attention, occurred an erro: ', e.__class__.__name__)
            print('Class error: ', e.__class__)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tracbak):
        print('Closing the file.')
        self.file.close()


################################################################################
################################## OPERATIONS ##################################
################################################################################

with MyOpenFile('context_maneger_class.txt', '+a') as file:
    file.write('This is my file with class context manager. \n')
    