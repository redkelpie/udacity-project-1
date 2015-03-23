def return_review(title):
    reviews = {}
    reviews = {
                'silence_of_the_lambs' : {'name':'Bob John','text':'This was by far the most distrubing moview I have seen!'},
                'host' : {'name':'Julian Smith','text':'I could do without the godzilla monster being so cliche'},
                'ferngully':{'name':'Sara Bells','text':'My twin boys love this movie and I love the way it teaches a lesson about nature'},
              }

    for title in reviews:
        if title in reviews:
            reviewer = reviews[title]['name']
            review = reviews[title]['text']

    data = [reviewer,review]
    return data

