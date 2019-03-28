//1) Write a MongoDB query to display all the documents in the collection restaurants

db.restaurants.find({});

//2)  Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.
db.restaurants.find({},{restaurant_id:1, name: 1, borough: 1, cuisine: 1 });

//3) Write a MongoDB query to display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all the documents in the collection restaurant.
db.restaurants.find({},{restaurant_id:1, name: 1, borough: 1, "address.zipcode": 1, _id:0 });

//4) Write a MongoDB query to display all the restaurant which is in the borough Bronx
db.restaurants.find({borough: "Bronx"})

//5) Write a MongoDB query to display the first 5 restaurant which is in the borough Bronx.
db.restaurants.find({borough: "Bronx"}).limit(5)

//6) Write a MongoDB query to find the restaurants who achieved a score more than 90.
db.restaurants.find({"grades.score": {$gt: 90}})
//7) Write a MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100
db.restaurants.find({ 
    "grades": { 
        $elemMatch: { 
            score: {$gt: 80 , $lt: 100}
        }
    }
});
//7) Write a MongoDB query to find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168
db.restaurants.find({
    cuisine: {$ne: "American "},
    "grades.score": {$gt: 70 },
    "address.coord.0": {$lt: -65.754168}
    
})

//db.restaurants.find({
//    cuisine: {$ne: "American "},
//    "grades.score": {$gt: 70 },
//    "address.coord.0": {$lt: -65.754168}
//    
//},
//{
//    grades: {
//        $elemMatch: {
//            score: {$gt: 70}
//        }
//    }
//})

//8) Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168.

//I don't understand the differences between the 7th and 8th. just the coord data?
db.restaurants.find({
    cuisine: {$ne: "American "},
    "grades.score": {$gt: 70 },
    "address.coord.1": {$lt: -65.754168}
    
})

//9) Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Wil' as first three letters for its name.
db.restaurants.find({name: /^wil/i },{restaurant_id:1, name: 1, borough: 1, cuisine: 1, _id:0 });

//10) Write a MongoDB query to find the restaurant name, borough, longitude and latitude and cuisine for those restaurants which contain 'Mad' as first three letters of its name.
db.restaurants.find({name: /^mad/i },{name: 1, borough: 1, "address.coord": 1, cuisine: 1, _id:0 });
