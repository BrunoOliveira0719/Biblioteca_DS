from tinydb import TinyDB 
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class todo:
    nome_livro: str
    quantidade: int

    def dict(self):
        return asdict(self)


t1 = todo('ojh','4')



db_path = Path(__file__).parent /'biblioteca.json'
db = TinyDB(db_path, indent=4)

db.truncate()

index = db.insert(t1.dict())
print(index)


