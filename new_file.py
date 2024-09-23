from dataclasses import dataclass, field
from datetime import datetime

def obter_data_hora_atual():
    return datetime.now()

@dataclass
class Registro:
    evento: str
    data_hora: datetime = field(default_factory=obter_data_hora_atual)

registro1 = Registro("Login")
print(registro1)


