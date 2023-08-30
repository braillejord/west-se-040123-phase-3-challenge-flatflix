#!/usr/bin/env python3
import ipdb

from classes.movie import Movie
from classes.review import Review
from classes.viewer import Viewer

#! You can test your code by running this file and checking what got printed out
#! You can also invoke a method, place a breakpoint in that method and use the debugger
#! if you like ipdb and it works for you, uncomment line 2 and 14

# Data seeding

if __name__ == "__main__":
    # Movies
    movie_1 = Movie(title="101 Dalmatians")
    movie_2 = Movie(title="Matrix")
    movie_3 = Movie(title="Mean Girls")

    # Viewers
    viewer_1 = Viewer(username="Smirky")
    viewer_2 = Viewer(username="Sminty")
    viewer_3 = Viewer(username="Podgey")
    viewer_4 = Viewer(username="Trudys")

    # Reviews
    review_1 = Review(movie=movie_1, viewer=viewer_1, rating=5)
    review_2 = Review(movie=movie_1, viewer=viewer_2, rating=4)
    review_3 = Review(movie=movie_1, viewer=viewer_2, rating=3)
    review_4 = Review(movie=movie_2, viewer=viewer_3, rating=3)
    review_5 = Review(movie=movie_3, viewer=viewer_4, rating=2)

    ipdb.set_trace()

# #! Testing Review class properties and attributes
# print("Testing Review class properties and attributes")
# print("If correct, you should see five Trues and one exception. Then comment out the line for the first exception and check if the second exception is raised")
# print(Review.all == [review_1, review_2, review_3, review_4, review_5]) #=> Should return True given the seeding above
# print(review_1.rating == 5) #=> Should return True given the seeding above
# review_5.rating = 1 #=> Should not raise exception
# print(review_5.rating == 1) #=> Should return True given the seeding above
# print(review_1.movie == movie_1) #=> Should return True given the seeding above
# print(review_1.viewer == viewer_1) #=> Should return True given the seeding above
# Review(movie='test', viewer='matteo', rating=4) #=> Should raise exception and please comment it out once verified!
# Review(movie=movie_1, viewer=viewer_1, rating=6) #=> Should raise exception and please comment it out once verified!

# #===============================================================================
# #! Testing Movie class properties and attributes
# print("Testing Movie class properties and attributes")
# print("If correct, you should see three Trues and one exception")
# print(Movie.all == [movie_1, movie_2, movie_3]) #=> Should return True given the seeding above
# print(movie_1.title == "101 Dalmatians") #=> Should return True given the seeding above
# movie_1.title = "new title" #=> Should not raise exception
# print(movie_1.title == "new title") #=> Should return True given the seeding above
# Movie("") #=> Should raise exception and please comment it out once verified!

# #! Testing Movie class association methods
# print("Testing Movie class association methods")
# print("If correct, you should see two Trues")
# print(movie_1.reviews() == [review_1, review_2, review_3]) #=> Should return True given the seeding above
# print(movie_1.reviewers() == [viewer_2, viewer_1]) #=> Should return True given the seeding above as uniqueness IS required

# #! Testing Movie class aggregate methods
# print("Testing Movie class aggregate methods")
# print(movie_1.average_rating() == 4) #=> Should return True given the seeding above
# print(Movie.highest_rated() == movie_1) #=> Should return True given the seeding above

# #===============================================================================

# #! Testing the Viewer class properties and attributes
# print("Testing Viewer class properties and attributes")
# print("If correct, you should see two Trues and one exception")
# print(viewer_1.username == "Smirky") #=> Should return True given the seeding above
# viewer_1.username = "new username" #=> Should not raise exception
# print(viewer_1.username == "new username") #=> Should return True given the seeding above
# Viewer("tests") #=> Should raise exception and please comment it out once verified!

# #! Testing Viewer class association methods
# print("Testing Viewer class association methods")
# print("If correct, you should see two Trues")
# print(viewer_2.reviews() == [review_2, review_3]) #=> Should return True given the seeding above
# print(viewer_2.reviewed_movies() == [movie_1, movie_1]) #=> Should return True given the seeding above as uniqueness is not required

# #! Testing Viewer class aggregate methods
# print("Testing Viewer class aggregate methods")
# print("If correct, you should see two Trues")
# print(viewer_2.has_reviewed_movie(movie_1) == True) #=> Should return True given the seeding above
# print(viewer_2.has_reviewed_movie(movie_2) == False) #=> Should return True given the seeding above
