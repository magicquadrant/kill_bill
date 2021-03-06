class Movie():
	""" This class provides a way to store movie related information."""
	VALID_RATINGS = ["G","PG","PG-13","R"]

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, itunes_link, rt_link):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.itunes_link=itunes_link
		self.rt_link=rt_link
