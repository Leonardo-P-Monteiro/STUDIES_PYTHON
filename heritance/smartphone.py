from log import LogFileMixin

class Eletronic:

    def __init__(self, name):
        self.name = name
        self._on = False

    def on(self):
        if not self._on:
            self._on = True
    
    def off(self):
        if self._on:
            self._on = False
    

class SmarthPhone(Eletronic, LogFileMixin):

    def on(self):
        super().on()

        if self._on:
            msg = f'{self.name} is on.'
            self.log_sucess(msg)

    def off(self):
        super().off()

        if not self._on:
            msg = f'{self.name} is off.'
            self.log_sucess(msg)
    
    def erro(self):
        
        msg = f'{self.name} showed an erro.'
        self.log_erro(msg)


# s1 = SmarthPhone('Telefone')
# s1.log_sucess('Deu certo')