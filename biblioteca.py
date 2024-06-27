from tinydb import TinyDB 
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class livro:
    nome_livro: str
    quantidade: int

    def dict(self):
        return asdict(self)

    def teste():
        livros = input(f"Digite os nomes dos livro separados por virgula: ").replace(' ','')
        livro_lista = livros.split(',')
        quantidades = input(f'Digite a quantiddes dos livro separados por virgula: ').replace(' ','')
        quantidades_lista = quantidades.split(',')

        print(livro_lista, quantidades_lista)
    teste()
    

t1 = livro('ojh','4')


db_path = Path(__file__).parent /'biblioteca.json'
db = TinyDB(db_path, indent=4)

db.truncate()

index = db.insert(t1.dict())
print(index)


