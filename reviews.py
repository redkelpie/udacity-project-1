def return_review(title):
    
    silence_of_the_lambs = {'name':'Kathleen Carrol','text':'The movie, scary and graphic to cause timid souls (such as this writer) to close their eyes at certain points, has a vise-like grip on the audience.'}
    host = {'name':'Luke Goodsell','text':'Joon-ho Bong\'s The Host is a very different kettle of mutated fish. '}
    ferngully = {'name':'Scott Weinberg', 'text':'Hey, if the Veggie Tales folks can sell religion in this fashion, then I say the environmental lobby deserves their fair shot as well.'}
    homeward_bound = {'name':'Brian Lowry','text':' A sprightly little entertainment that should enthrall tots without straining the patience of their parents.'}
    hunger_games = {'name':'David Keyes', 'text':' Has all the technical ingredients of a great (and even important) film, but sideswipes them in order to leave the audience feeling like that they have been abandoned in the wilderness of extreme cruelty. '}
    memento = {'name':'Joe Morgenstern','text':' I can\'t remember when a movie has seemed so clever, strangely affecting and slyly funny at the very same time. '}

    reviews = {'Silence of the Lambs':silence_of_the_lambs,
               'Host':host,
               'Ferngully':ferngully,
               'Homeward Bound':homeward_bound,
               'Hunger Games':hunger_games,
               'Memento':memento}

    for (name,data) in reviews.items():
        if name == title:
            review = []
            review.append(data['name'])
            review.append(data['text'])
    
            return review


