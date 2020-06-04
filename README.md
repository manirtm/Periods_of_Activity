# Periods_of_Activity

* Periods_of_Activity is a django application with two models as **User** and **Activity_periods**.
* It is used to describe all the user and their corrosponding periods of activity across multiple months.
* To dispaly the data, wrote a custom management command to populate the database with some dummy data.
* Used two serialize functions **Activity_periods_serializers** and **User_serialize** to serialize data for the expected json format.
* Design an API to serve that data in the json format as given in
[link](https://drive.google.com/open?id=1xZa3UoXZ3uj2j0Q7653iBp1NrT0gKj0Y)

## It runs under following requirements:

* Django 3.0.7
* Python 3.6.8
* psycopg2 2.8.5

