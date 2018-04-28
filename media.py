import webbrowser


class Movie():
    """ Define variables for details needed of a movie """
    def __init__(self, movie_title, movie_storyline, image_url, trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_url

    # Play movie trailer
    """ Automatically open the trailer youtube url in default browser """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
