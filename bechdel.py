# Difficulty level: Advanced

# Goal #1: Create a program that will print out a list of movie titles and a set of ratings defined below into a particular format.

# First, choose any five movies you want.

# Next, look each movie up manually to find out four pieces of information:
#		Their parental guidance rating (G, PG, PG-13, R)
#		Their Bechdel Test Rating (See http://shannonvturner.com/bechdel or http://bechdeltest.com/)
#		Their IMDB Rating from 0 - 10 (See http://imdb.com/)
# 		Their genre according to IMDB

# You'll need a variable for movie_titles, a variable for parental_rating, a variable for bechdel_rating, a variable for imdb_rating, and a variable for genre.

# Since you have five sets of facts about five movies, you'll want to use lists to hold these pieces of information.

titles = ['American Sniper','Birdman','Boyhood','The Grand Budapest Hotel','The Imitation Game']
parental_rating = ['R', 'R', 'R', 'R', 'PG-13']
bechdel_rating = ['1', '3', '3', '1', '2']
imdb_rating = ['7.4', '8.0','8.1', '8.1', '8.2']
genre = ['Action / Biography / Drama', 'Comedy / Drama', 'Drama', 'Adventure / Comedy / Drama', 'Biography / Drama / Thriller']

# Once all of your information is stored in lists, loop through those lists to print out information with each part separated by a comma, like this:

for titles, parental_rating, bechdel_rating, imdb_rating, genre in zip(titles, parental_rating, bechdel_rating, imdb_rating, genre):
<<<<<<< HEAD
    print "{0}, {1}, {2}, {3}, {4}".format(titles, parental_rating, bechdel_rating, imdb_rating, genre)
=======
    print "{0}, {1}, {2}, {3}, {4}".format(titles, parental_rating, bechdel_rating, imdb_rating, genre)
>>>>>>> origin/master
