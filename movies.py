# Base class: Movie
class Movie:
    def __init__(self, title, director, genre, year):
        self.title = title
        self.director = director
        self.genre = genre
        self.year = year
        self.__rating = None  # Encapsulated (private attribute)

    def play(self):
        print(f"🎥 Now playing: '{self.title}' directed by {self.director} ({self.year})")

    def set_rating(self, rating):
        if 0 <= rating <= 10:
            self.__rating = rating
        else:
            print("❌ Rating must be between 0 and 10.")

    def get_rating(self):
        return f"⭐ Rating for '{self.title}': {self.__rating if self.__rating is not None else 'Not Rated'}"


# Subclass: AnimatedMovie inherits from Movie
class AnimatedMovie(Movie):
    def __init__(self, title, director, year, animation_studio):
        super().__init__(title, director, "Animation", year)
        self.animation_studio = animation_studio

    def play(self):
        print(f"🎬 Watch the animated magic of '{self.title}' by {self.animation_studio}!")


# Testing the classes
m1 = Movie("Inception", "Christopher Nolan", "Sci-Fi", 2010)
m1.play()
m1.set_rating(9)
print(m1.get_rating())

m2 = AnimatedMovie("Coco", "Lee Unkrich", 2017, "Pixar")
m2.play()
m2.set_rating(8.5)
print(m2.get_rating())
