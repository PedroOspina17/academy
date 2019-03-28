
//Update the entire object

var celToUpdate = ({_id: ObjectId('5c9547a8058f615dd41c40e2')})
db.modelosCelulares.update(celToUpdate,
 { 
   "marca" : "Motorola", 
   "modelo" : "C115", 
   "introduccion" : 2006 
 }
);

//Update the columns specified 
db.modelosCelulares.update(
    {"introduccion": { $gt: 2003}},
    {$set: {
        "pantalla": "monocromática",
        "tecnologia": "GSM"
    }},
    {multi: true}
)



// DELETE



var celToDelete = ({_id: ObjectId('5c9547a8058f615dd41c40e1')});
db.modelosCelulares.remove(celToDelete)

