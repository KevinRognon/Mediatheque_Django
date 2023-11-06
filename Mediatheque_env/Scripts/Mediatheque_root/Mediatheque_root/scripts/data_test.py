from member.models import Member
from Mediatheque_root.models import Book, Cd, Dvd, BoardGame

# Création de 4 membres
members = [
    Member(firstname="Alice", lastname="Dubois"),
    Member(firstname="Bob", lastname="Martin"),
    Member(firstname="Carla", lastname="Durand"),
    Member(firstname="David", lastname="Moreau")
]

for member in members:
    member.save()

# Création de plusieurs livres
books = [
    Book(name="Le Petit Prince", author="Antoine de Saint-Exupéry", available=True),
    Book(name="Le Comte de Monte-Cristo", author="Alexandre Dumas", available=True),
    Book(name="1984", author="George Orwell", available=True),
    Book(name="Le Seigneur des Anneaux", author="J.R.R. Tolkien", available=True)
]

for book in books:
    book.save()

# Création de plusieurs CD
cds = [
    Cd(name="Back in Black", artist="AC/DC", available=True),
    Cd(name="The Dark Side of the Moon", artist="Pink Floyd", available=True),
    Cd(name="Thriller", artist="Michael Jackson", available=True),
    Cd(name="Nevermind", artist="Nirvana", available=True)
]

for cd in cds:
    cd.save()

# Création de plusieurs DVD
dvds = [
    Dvd(name="Le Parrain", realisator="Francis Ford Coppola", available=True),
    Dvd(name="Forrest Gump", realisator="Robert Zemeckis", available=True),
    Dvd(name="Le Silence des agneaux", realisator="Jonathan Demme", available=True),
    Dvd(name="Pulp Fiction", realisator="Quentin Tarantino", available=True)
]

for dvd in dvds:
    dvd.save()

# Création de plusieurs jeux de plateau
board_games = [
    BoardGame(name="Les Aventuriers du Rail", creator="Alan R. Moon"),
    BoardGame(name="Catan", creator="Klaus Teuber"),
    BoardGame(name="Carcassonne", creator="Klaus-Jürgen Wrede"),
    BoardGame(name="Pandemic", creator="Matt Leacock")
]

for board_game in board_games:
    board_game.save()
