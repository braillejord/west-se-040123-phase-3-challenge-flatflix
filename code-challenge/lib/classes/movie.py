class Movie:
    all = []

    def __init__(self, title):
        self.title = title
        Movie.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if type(new_title) is str and len(new_title) > 0:
            self._title = new_title
        else:
            raise Exception("Title must be a string that has more than one character.")

    def reviews(self):
        return [review for review in Review.all if review.movie == self]

    def reviewers(self):
        return list(set([review.viewer for review in Review.all if review.movie == self]))

    def average_rating(self):
        search = [review.rating for review in Review.all if review.movie == self]

        return sum(search) / len(search)

    @classmethod
    def highest_rated(cls):
        if cls.all:
            highest_rated_movie = None
            highest_rating = 0
            for movie in cls.all:
                if movie.average_rating() > highest_rating:
                    highest_rated_movie = movie
                    highest_rating = movie.average_rating()
            return highest_rated_movie
        return None


from classes.review import Review
from classes.viewer import Viewer
