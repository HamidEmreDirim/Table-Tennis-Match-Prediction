# Table Tennis Match Predictor

A machine learning and data science project that can predict the result of a professional table tennis match

## Roadmap

- Gathering data: Unfortunately, I could not found any public API for both Player data and match history. The API data was either to shallow or not in the format that I could train my model , so I used **Selenium** and got my data from directly websites. I finally got all the data I needed to feed my machine learning algorithm after scraping over 20.000 match records.


- Preprocess data: The data I had was useless on its own. I had to make cleaning and formatting changes to the data. I used Pandas library for this.


- Select a machine learning model: Since I didn't have enough data to train neural networks. Therefore I went back to machine learning algorithms. For the nature of my data, I had 3 machine learning algorithms to choose from: linear regression, logistic regression, or a decision tree. After exhaustive research, I have decided to use logistic regression. It works by finding the best linear combination of the input features (e.g., players' attributes) to predict the output class.


- Train the model: It was the simplest part to train the model. All I had to do was make some imports and put the data in them.  

- Model Performance:
![alt text](https://github.com/HamidEmreDirim/porfolio_projects/TableTennisMatchPredictor/result.jpg?raw=true)


- Deploy the model: When I was finished with the model, I saved it as **match_predictor.pickle**. And also included a function called **predictMatch** at the end of **main.ipynb** file. With this function its pretty simple to make prediction. All needs to be done is put a two professional table tennis name (for now only works with top 1000 men's name) and get your prediction.
 

## Acknowledgements

 - [Sklearn Documentation](https://scikit-learn.org/stable/user_guide.html)
 - [Website that is scraped for match data and player informations](https://tabletennis.guide/ittftournaments.php?page=1)

