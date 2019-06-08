"# wot_bot" 
This project comprises of 3 intents:
      get_news
      get_rates
      show_dog

The get_news intent fetches news using the gnewsclient.
it takes 3 parameters --> news_type
                          language
                          country
based on these 3 parameters the news is retrieved
note: the news_type parameter is necessary

The get_rates intent coverts the currency into indian currency i.e INR
it uses the forex-python library to convert the rates
it takes one parameter that is currency type
this function currently can convert any currency to inr 
it only tells the price on 1 unit of currency 
for eg 1 dollor is 69 rs

the show_dog intent is for ending dog images
it uses the random dog image api listed on "https://dog.ceo/dog-api/documentation/random"
to fetch an url of the image
it is onlhy limited to showing dog image

Thank you for using the project

Ayush
