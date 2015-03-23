import reviews
import webbrowser

class Video():
    """
    Define the properties of a video with a title, trailer, thumbnail,
    rating, genre and associate reviews with it
    """

    def __init__(self, title, trailer_youtube_url, poster_image_url, genre, rating):
        VALID_GENRES = ["Drama","Childrens","Suspense","Action"]
        VALID_RATINGS = ["G","PG","PG-13","R"]
       
        # Check to see if genre is in the genre list
        if genre in VALID_GENRES:
            self.genre = genre
        else:
            self.genre = "No genre"
            
        # Check to see if genre is in the ratings list
        if rating in VALID_RATINGS:
            self.rating = rating
        else:
            self.rating = "No rating"
            
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

        # associate reviews with the title
        self.reviews = reviews.return_review(title)

    # Predict audience based on genre and rating
    def audience(self):
       AUDIENCE = ["Children","Teens","Adults"]
       if self.rating == "G" | self.rating == "PG":
           self.audience = AUDIENCE[0]
       if self.rating == "PG-13" | self.rating == "R":
           if self.genre == "Drama" | self.genre == "Suspense":
               self.audience = AUDIENCE[2]
           if self.genre == "Action":
               self.audience = AUDIENCE[1]
           

    def play_trailer(self):
        webbrowser.open(self.trailer)
        
