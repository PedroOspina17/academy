db.modelosCelulares.insert({marca: "Nokia", modelo: "1100", introduccion: 2003, _id: ObjectId('123')});
db.modelosCelulares.insert({marca: "Motorola", modelo: "C115", introduccion: 2005, _id: ObjectId('321')});
db.modelosCelulares.insert(
 { 
   "marca" : "Nokia", 
   "modelo" : "1100", 
   "introduccion" : 2003 
 }
);
db.modelosCelulares.insert(
 { 
   "marca" : "Motorola", 
   "modelo" : "C115", 
   "introduccion" : 2005 
 }
);

db.modelosCelulares.insert(
 { 
   "marca" : "Nokia", 
   "modelo" : "5110", 
   "introduccion" : 1998 
 }
);


///With complex fields

 var hector1 = {
  nombre: 'Héctor',
  apellido: 'Espósito',
  direccion: { 
    altura: 4000, 
    calle: 'Cabildo', 
    ciudad: 'Buenos Aires' 
  },
  edad: 24
};


db.personas.insert(hector1);

 var hector2 = {
  nombre: 'Héctor 1',
  apellido: 'Espósito',
  direccion: { 
    altura: 500, 
    calle: 'Cabildo', 
    ciudad: 'Buenos Aires' 
  },
  edad: 242
};
db.personas.insert(hector2);

var hector3 = {
  nombre: 'Héctor2',
  apellido: 'Espósito',
  direccion: { 
    altura: 100, 
    calle: 'Cabildo', 
    ciudad: 'Buenos Aires' 
  },
  edad: 2
};
db.personas.insert(hector3);

 var hector4 = {
  nombre: 'Héctor3',
  apellido: 'Espósito',
  direccion: { 
    altura: 100, 
    calle: 'Cabildo', 
    ciudad: 'Buenos Aires' 
  },
  edad: 26
};
db.personas.insert(hector4);



 var hector5 = {
  nombre: 'Héctor4',
  apellido: 'Espósito',
  direccion: { 
    altura: 500, 
    calle: 'Cabildo', 
    ciudad: 'Buenos Aires' 
  },
  edad: 27
};
db.personas.insert(hector5);





 var hector5 = {
  nombre: 'Héctor5',
  apellido: 'Espósito5',
  direccion: { 
    altura: 21, 
    calle: 'Cabildo5', 
    ciudad: 'Buenos Aires' 
  },
  edad: 27,
  carros[
      {marca: "Mazda", Año: 2011},
      {marca: "Mazda", Año: 2010},
      {marca: "Mazda", Año: 2009},
      {marca: "Renault", Año: 2008},
      {marca: "Renault", Año: 2009}
      ]
};
db.personas.insert(hector5);



 var hector6 = {
  nombre: 'Héctor6',
  apellido: 'Espósito6',
  direccion: { 
    altura: 210, 
    calle: 'Cabildo6', 
    ciudad: 'Buenos Aires' 
  },
  edad: 40,
  carros[
      {marca: "Nisan", Año: 2019},
      {marca: "Nisan", Año: 2018},
      {marca: "Mazda", Año: 2017},
      {marca: "Mazda", Año: 2015},
      {marca: "Renault", Año: 2014}
      ]
};
db.personas.insert(hector6);
