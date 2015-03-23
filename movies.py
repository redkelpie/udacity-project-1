import videos
import fresh_tomatoes

silence_of_the_lambs = videos.Video("Silence of the Lambs",
                                    "http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=video&cd=6&cad=rja&uact=8&ved=0CDgQtwIwBQ&url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DlQKs169Sl0I&ei=qiAGVauiEcjVggTqmICoCA&usg=AFQjCNEimO7agksQ8TbC765RYJ5CrqceTQ&bvm=bv.88198703,d.eXY",
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
ferngully = videos.Video("FernGully",
                        "http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=0CDcQtwIwAg&url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DI2OHc4OvjVc&ei=h-QAVfy5DIKeNoKggoAM&usg=AFQjCNH8zcN8GmfH4_gzwL4X0nHsKKeyDw&bvm=bv.87920726,d.eXY",
                        "http://ia.media-imdb.com/images/M/MV5BNDMyOTMzMjc0NV5BMl5BanBnXkFtZTcwNDc4MzEzMQ@@._V1_SX640_SY720_.jpg",
                        "Childrens",
                        "G"
                        )
homeward_bound = videos.Video("Homeward Bound",                        
                        "http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=video&cd=4&cad=rja&uact=8&ved=0CCwQtwIwAw&url=http%3A%2F%2Fvideo.disney.com%2Fwatch%2Fhomeward-bound-the-incredible-journey-trailer-4be1030a70ad049519ec4e85&ei=tdgEVeTtLYyWgwSkzIOYCA&usg=AFQjCNEj2rQsceRQhh2VDTcxvqxSAOm7hg&bvm=bv.88198703,d.eXY",
                        "http://ia.media-imdb.com/images/M/MV5BMjAyNTE4NDU2Nl5BMl5BanBnXkFtZTcwNTgyNjQyMQ@@._V1_SY317_CR4,0,214,317_AL_.jpg",
                        "Childrens",
                        "PG"
                        )
hunger_games = videos.Video("Hunger Games",
                        "http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=0CDcQtwIwAg&url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DI2OHc4OvjVc&ei=h-QAVfy5DIKeNoKggoAM&usg=AFQjCNH8zcN8GmfH4_gzwL4X0nHsKKeyDw&bvm=bv.87920726,d.eXY",
                        "http://ia.media-imdb.com/images/M/MV5BNDMyOTMzMjc0NV5BMl5BanBnXkFtZTcwNDc4MzEzMQ@@._V1_SX640_SY720_.jpg",
                        "Action",
                        "PG-13"
                        )
momento = videos.Video("Momento",
                      "http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=0CDcQtwIwAg&url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DI2OHc4OvjVc&ei=h-QAVfy5DIKeNoKggoAM&usg=AFQjCNH8zcN8GmfH4_gzwL4X0nHsKKeyDw&bvm=bv.87920726,d.eXY",
                      "http://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                      "Suspense",
                      "R"
                        )
movies = [silence_of_the_lambs,host,ferngully,homeward_bound,hunger_games,momento]
fresh_tomatoes.open_movies_page(movies)
