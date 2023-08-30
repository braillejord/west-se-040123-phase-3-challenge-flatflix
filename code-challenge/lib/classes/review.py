class Review:
    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        Review.all.append(self)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if type(new_rating) is int and 1 <= new_rating <= 5:
            self._rating = new_rating
        else:
            raise Exception("Rating must be an integer between 1 and 5 (inclusive).")

    @property
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self, new_viewer):
        if isinstance(new_viewer, Viewer):
            self._viewer = new_viewer
        else:
            raise Exception("Viewer must be of type Viewer.")

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, new_movie):
        if isinstance(new_movie, Movie):
            self._movie = new_movie
        else:
            raise Exception("Movie must be of type Movie.")


from classes.movie import Movie
from classes.viewer import Viewer
