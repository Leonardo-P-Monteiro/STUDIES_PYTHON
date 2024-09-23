from pathlib import Path

LOG_FILE_SAVE = Path(__file__).parent / 'log_file.txt'


class Log:

    def _log(self, msg):
        raise NotImplementedError('Implemente esse método.')
    
    def log_erro(self, msg):
        return self._log(f'Erro: {msg}')

    def log_sucess(self, msg):
        return self._log(f'Success: {msg}')

class LogFileMixin(Log):
    
    def _log(self, msg):
        
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log: ', msg_formatada)
        with open(LOG_FILE_SAVE, '+a', encoding='utf8') as file:
            file.write(msg_formatada)
            file.write('\n')
            file.close()

class LogPrintMixin(Log):

    def _log(self, msg):
        return print(f'{msg} ({self.__class__.__name__})')


if __name__ == "__main__":
    l = LogFileMixin()
    l.log_erro('Algo deu errado. 😭')
    l.log_sucess('Deu certo. 😎') 