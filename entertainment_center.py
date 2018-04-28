import fresh_tomatoes
import media

# Movie details set up
frozen = media.Movie('Frozen',
                     'This is storyline',
                     'http://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781608875979/frozen-the-poster-collection-9781608875979_lg.jpg',
                     'https://youtu.be/TbQm5doF_Uc')

wonderwoman = media.Movie('Wonder Woman',
                          'This is storyline',
                          'https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg',
                          'https://youtu.be/VSB4wGIdDwo')

how_to_train_your_dragon_2 = media.Movie('How to Train Your Dragon 2',
                                         'This is storyline',
                                         'https://upload.wikimedia.org/wikipedia/en/a/af/How_to_Train_Your_Dragon_2_poster.jpg',
                                         'https://youtu.be/2BP38770KNo')

brave = media.Movie('Brave',
                    'This is storyline',
                    'https://vignette.wikia.nocookie.net/disney/images/c/ca/Brave_-_Poster.png/revision/latest?cb=20140902165221',
                    'https://youtu.be/TEHWDA_6e3M')

tangled = media.Movie('Tangled',
                      'This is storyline',
                      'https://vignette.wikia.nocookie.net/disney/images/c/ca/Tangled_rapunzel_poster_20.jpg/revision/latest?cb=20110929034113',
                      'https://youtu.be/2f516ZLyC6U')

real_steel = media.Movie('Real Steel',
                         'This is storyline',
                         'https://images-na.ssl-images-amazon.com/images/I/51ulq%2BI7vHL.jpg',
                         'https://youtu.be/T75j9CoBVzE')


movies = [frozen,
          wonderwoman,
          how_to_train_your_dragon_2,
          brave, tangled,
          real_steel]

# open website in browser when run py
fresh_tomatoes.open_movies_page(movies)
