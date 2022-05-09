db.getCollection("restaurants").find({})

//Write a MongoDB query to display all the documents in the collection restaurants.

db.restaurants.find()

//Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.

db.restaurants.find({},{"restaurant_id":1, "name":1, "borough":1,"cuisine":1})

//Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine, but exclude the field _id for all the documents in the collection restaurant

db.restaurants.find({}, {"_id":0, "name":1," cuisine": 1, "borough": 1, "restaurant_id": 1})

//Write a MongoDB query to display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all the documents in the collection restaurant

db.restaurants.find({},{"_id":0,"restaurant_id": 1,"name":1,"address.zipcode": 1, "borough": 1})

//Write a MongoDB query to display all the restaurant which is in the borough Bronx.

db.restaurants.find({"borough":"Bronx"})

//Write a MongoDB query to display the first 5 restaurant which is in the borough Bronx.

db.restaurants.find({"borough":"Bronx"}).limit(5)

//Write a MongoDB query to display the next 5 restaurants after skipping first 5 which are in the borough Bronx.

db.restaurants.find({"borough":"Bronx"}).skip(5).limit(5)

//Write a MongoDB query to find the restaurants who achieved a score more than 90.

db.restaurants.find({"grades.score":{$gt : 90}})

//Write a MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100.

db.restaurants.find({$and : [{"grades.score" : {"$gt" : 80}},{"grades.score" : {"$lt" : 100}}]})

//Write a MongoDB query to find the restaurants which locate in latitude value less than -95.754168.

db.restaurants.find({"address.ccord.0":{$lt:-95.754168}})

//Write a MongoDB query to find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168.

db.restaurants.find({$and :[{"cuisine":{$ne:"American"}}, {"grades.score" : {"$gt" : 70}},{"address.ccord.0" : {"$lt" :-65.754618}}]})

//Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168. Note : Do this query without using $and operator.

db.restaurants.find({"cuisine":{$ne:"American"}, "grades.score" : {"$gt" : 70},"address.ccord.0" : {"$lt" :-65.754618}})







