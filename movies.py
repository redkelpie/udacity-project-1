import videos
import fresh_tomatoes

# Build Video instances
# Instance variables used (title, trailer, thumbnail image, genre, rating)
silence_of_the_lambs = videos.Video("Silence of the Lambs",
                                    "https://www.youtube.com/watch?v=lQKs169Sl0I",
                                    "http://ia.media-imdb.com/images/M/MV5BMTQ2NzkzMDI4OF5BMl5BanBnXkFtZTcwMDA0NzE1NA@@._V1_SX640_SY720_.jpg",
                                    "Drama",
                                    "R"
                                    )
host = videos.Video("Host",
                   "https://www.youtube.com/watch?v=FCsBMwK40hw",
                   "http://ia.media-imdb.com/images/M/MV5BMTQyNTk4NzAyMF5BMl5BanBnXkFtZTcwMTM2ODE0MQ@@._V1_SX214_AL_.jpg",
                   "Drama",
                   "R"
                        )
ferngully = videos.Video("Ferngully",
                        "https://www.youtube.com/watch?v=I2OHc4OvjVc",
                        "http://ia.media-imdb.com/images/M/MV5BNDMyOTMzMjc0NV5BMl5BanBnXkFtZTcwNDc4MzEzMQ@@._V1_SX640_SY720_.jpg",
                        "Childrens",
                        "G"
                        )
homeward_bound = videos.Video("Homeward Bound",                        
                        "https://www.youtube.com/watch?v=U8LO9hRL3fQ",
                        "http://ia.media-imdb.com/images/M/MV5BMjAyNTE4NDU2Nl5BMl5BanBnXkFtZTcwNTgyNjQyMQ@@._V1_SY317_CR4,0,214,317_AL_.jpg",
                        "Childrens",
                        "PG"
                        )
hunger_games = videos.Video("Hunger Games",
                        "https://www.youtube.com/watch?v=4S9a5V9ODuY",
                        "http://ia.media-imdb.com/images/M/MV5BNDMyOTMzMjc0NV5BMl5BanBnXkFtZTcwNDc4MzEzMQ@@._V1_SX640_SY720_.jpg",
                        "Action",
                        "PG-13"
                        )
memento = videos.Video("Memento",
                      "www.youtube.com/watch?v=0vS0E9bBSL0",
                      "http://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                      "Suspense",
                      "R"
                        )
# Add movie instances to a list
movies = [silence_of_the_lambs,host,ferngully,homeward_bound,hunger_games,memento]
fresh_tomatoes.open_movies_page(movies)
