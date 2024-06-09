import random
from django.conf import settings
from inventory.models import Item, Category

# To run this, run the following command:
# python manage.py populatedb_books
class authorCreate:
    def __init__(self, id, first_name, last_name, birth_date, death_date):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.death_date = death_date

    def dict(self):
        return {
            "author_id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "death_date": self.death_date
        }

# creating author and book list

authors = [
    authorCreate(0, "Patrick", "Rothfuss", "1973-06-06", ""),
    authorCreate(1, "Ben", "Bova", "1932-11-8", ""),
    authorCreate(2, "Isaac", "Asimov", "1920-01-02", "1992-04-06"),
    authorCreate(3, "Bob", "Billings", "1933-12-01", ""),
    authorCreate(4, "Jim", "Jones", "1971-12-16", ""),
  ]

class genreCreate:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def dict(self):
        return {
            "genre_id": self.id,
            "name": self.name
        }

genres =[
    genreCreate(0, "Fantasy"),
    genreCreate(1, "Science Fiction"),
    genreCreate(2, "French Poetry"),
  ]
 
class bookCreate:
    def __init__(self, id, title, description, isbn, author, genres, price):
        self.id = id
        self.title = title
        self.description = description
        self.isbn = isbn
        self.author = author
        self.genres = genres
        self.price = price

    def dict(self):
        return {
            "book_id": self.id,
            "title": self.title,
            "description": self.description,
            "isbn": self.isbn,
            "author_id": self.author.dict(),
            "genres": [ genre.dict() for genre in self.genres ],
            "price": self.price
        }

books = [
    bookCreate(0,
      "The Name of the Wind (The Kingkiller Chronicle, #1)",
      "I have stolen princesses back from sleeping barrow kings. I burned down the town of Trebon. I have spent the night with Felurian and left with both my sanity and my life. I was expelled from the University at a younger age than most people are allowed in. I tread paths by moonlight that others fear to speak of during day. I have talked to Gods, loved women, and written songs that make the minstrels weep.",
      "9781473211896",
      authors[0],
      [genres[0]],
      10.99
    ),
    bookCreate(1,
      "The Wise Man's Fear (The Kingkiller Chronicle, #2)",
      "Picking up the tale of Kvothe Kingkiller once again, we follow him into exile, into political intrigue, courtship, adventure, love and magic... and further along the path that has turned Kvothe, the mightiest magician of his age, a legend in his own time, into Kote, the unassuming pub landlord.",
      "9788401352836",
      authors[0],
      [genres[0]],
      20.99
    ),
    bookCreate(2,
      "The Slow Regard of Silent Things (Kingkiller Chronicle)",
      "Deep below the University, there is a dark place. Few people know of it: a broken web of ancient passageways and abandoned rooms. A young woman lives there, tucked among the sprawling tunnels of the Underthing, snug in the heart of this forgotten place.",
      "9780756411336",
      authors[0],
      [genres[0]],
      99.99
    ),
    bookCreate(3,
      "Apes and Angels",
      "Humankind headed out to the stars not for conquest, nor exploration, nor even for curiosity. Humans went to the stars in a desperate crusade to save intelligent life wherever they found it. A wave of death is spreading through the Milky Way galaxy, an expanding sphere of lethal gamma ...",
      "9780765379528",
      authors[1],
      [genres[1]],
      40.99,
    ),
    bookCreate(4,
      "Death Wave",
      "In Ben Bova's previous novel New Earth, Jordan Kell led the first human mission beyond the solar system. They discovered the ruins of an ancient alien civilization. But one alien AI survived, and it revealed to Jordan Kell that an explosion in the black hole at the heart of the Milky Way galaxy has created a wave of deadly radiation, expanding out from the core toward Earth. Unless the human race acts to save itself, all life on Earth will be wiped out...",
      "9780765379504",
      authors[1],
      [genres[1]],
      60.99,
    ),
    bookCreate(5,
      "Test Book 1",
      "Summary of test book 1",
      "ISBN111111",
      authors[4],
      [genres[0], genres[1]],
      101.99
    ),
    bookCreate(6,
      "Test Book 2",
      "Summary of test book 2",
      "ISBN222222",
      authors[4],
      [],
      30.99
    ),
  ]

def populate_db_with_books():
    category_instance = Category.objects.filter(name="Books")
    if not category_instance:
        category_instance = Category.objects.create(name="Books")
    else:
        category_instance = category_instance[0]
    for book in books:
        if not Item.objects.filter(extra_fields__isbn=book.isbn):
            item_instance = Item()
            item_instance.name = book.title
            item_instance.description = book.description
            item_instance.price = book.price
            item_instance.number_in_stock = random.randint(0, 100)
            item_instance.extra_fields = book.dict()
            item_instance.save()
            item_instance.url = f"/app/{category_instance.name.lower()}/items/{item_instance.id}"
            item_instance.category.add(category_instance)
            item_instance.save()
        else:
            print(f"Book Item, name:{book.title}, ISBN: {book.isbn} already exists")