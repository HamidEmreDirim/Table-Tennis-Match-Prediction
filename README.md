# Table Tennis Match Predictor

A machine learning and data science project that can predict the result of a professional table tennis match

## Roadmap

- Gathering data: Luckily, I managed to find a public API to get top 500 table tennis players. However, when I tried to find an API for table tennis matches, there was no public API for it, so I used **Selenium**. I finally got all the data I needed to feed my machine learning algorithm after scraping over 10.000 match records.

- Preprocess data: The data I had was useless on its own. I had to make cleaning and formatting changes to the data. I used Pandas library for this.

- Exploratory data analysis: Using visualizations and statistical analyses to explore the data and identify trends or patterns.

- Select a machine learning model: Since I didn't have more than 10,000 pieces of data, I could not use the neural networks. When I tried it, I only got about 49% accuracy, so I went back to machine learning algorithms. For the nature of my data, I had 3 machine learning algorithms to choose from: linear regression, logistic regression, or a decision tree. After exhaustive research, I have decided to use logistic regression. It works by finding the best linear combination of the input features (e.g., players' attributes) to predict the output class.

- Train the model: It was the simplest part to train the model. All I had to do was make some imports and put the data in them.  

- Deploy the model: When I was finished with the model, I saved it as **match_predictor.pickle**.
 

## Acknowledgements

 - [Sklearn Documentation](https://scikit-learn.org/stable/user_guide.html)
 - [API for gathering top table tennis players](https://developer.sportradar.com/docs/read/baseline_sports_coverage/Table_Tennis_v2)
 - [Website that is scraped for match data](https://tabletennis.guide/ittftournaments.php?page=1)

