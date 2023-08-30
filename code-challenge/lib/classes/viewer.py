class Viewer:
    all = []

    def __init__(self, username):
        self.username = username
        Viewer.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if type(new_username) is str and 6 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise Exception("Username must be a string between 6 and 16 characters.")

    def reviews(self):
        return [review for review in Review.all if review.viewer == self]

    def reviewed_movies(self):
        return [review.movie for review in Review.all if review.viewer == self]

    def has_reviewed_movie(self, movie):
        if [review for review in Review.all if review.movie == movie]:
            return True
        else:
            return False


from classes.review import Review
from classes.movie import Movie
