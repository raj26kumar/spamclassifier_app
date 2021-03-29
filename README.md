# spamclassifier_app
This application basically predicts and shows that msg/sms is a spam or not .
This is an end to end machine learning project.

* Preprocessed that dataset using Natural Language Processing techniches
* Used multinomial naive bayes for prediction 
* Then created a flask app to deployed our ml model
* Also deployed this application using Heroku

I used lil bit of bootstrap for styling


> First see jyputer note book , there developed our ml model
> using pickle ,created tfidf.pkl (for reusing tfidf-transformer in production) and spam_model.pkl (for resuing trained model)
> they created main.py where our logic is written for web app and then rendered the templates
