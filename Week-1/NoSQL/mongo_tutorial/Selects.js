

//Get All
db.personas.find();
// Look in complex fields
db.personas.find({'direccion.altura': 400});

//Creating a document with a specific ID


db.modelosCelulares.find()
// Look for id
db.modelosCelulares.find({_id: ObjectId('5c9547a8058f615dd41c40e2')});

db.modelosCelulares.find({"marca":"Nokia",pantalla:"monocromática" })

db.modelosCelulares.find({"introduccion": { $gt: 2003}})

//TOP 5
db.personas.find({}).limit(100);

//Filtering greater than 100
db.personas.find({edad:{$gt: 50}})
db.personas.find({edad:{$lt: 24}})

// Projection, to specify a specific columns
db.personas.find({"direccion.altura":{$gt: 100}},{ nombre: 1, apellido: 1 } ) 
// avoid _id field
db.personas.find({"direccion.altura":{$gt: 100}},{ nombre: 1, apellido: 1, _id:0 } ) 
// Excluding fields
db.personas.find({"direccion.altura":{$gt: 100}},{ nombre: 0, apellido: 0, _id:0 } ) 
// in nested documents
db.personas.find({"direccion.altura":{$gt: 100}},{ nombre: 1, apellido: 1, "direccion.altura": 1 } ) 
// To Select the document with a value different of... USE $NE instead of $not
db.personas.find({edad: {$ne: 24}}) // will show documents with age different of 24.

//Filtering by document array field with multiple conditions
db.personas.find({ 
    carros:{ 
        $elemMatch: { 
            marca: "Mazda",
            Año: { $gt: 2010, $lt: 2017} 
        }  
    } 
})

// Comparing two fields from a single document
db.personas.find( { $expr: { $gt: [ "$edad" , "$direccion.altura" ] } } ) // It will show just the document which have the age greater than the address high. 

db.personas.find( { "carros": { $size: 3 } } )// Filtering by the array size ???

//To verify if a specified field exits 
db.personas.find({carros:{ $exists: true}}) // just select the documents with the 'carros' field

// manipulating arrays projection as nested documents
db.personas.find({"carros.Año": {$gt: 2017}}) // filter the document based on the element array, but the array is being displayed completely
db.personas.find({"carros.Año": {$gt: 2017}},{"carros.$":1})
db.personas.find({},{ carros:{ $slice: -1} } ) // Return the first element on the array cars
db.personas.find({},{ carros:{ $slice: 3} } ) // Return the tree element on the array cars
db.personas.find({},{ carros:{ $slice: -1} } ) // Return the last element on the array cars
db.personas.find({},{ carros:{ $slice: [1,2]} } ) // skip one element and take the next two from the array cars
db.personas.find({},{ carros:{ $elemMatch: { Año: 2019 }  } } ) // Return the element array that meet the condition 
db.personas.find({},{ 
    carros:{ 
        $elemMatch: { 
            marca: "Mazda",
            Año: { $gt: 2010} 
        }  
    } 
}) // Return the element array that meet the condition with multiple criteria, JUST RETURN THE FIRST ELEMENT OF THE ARRAY...
