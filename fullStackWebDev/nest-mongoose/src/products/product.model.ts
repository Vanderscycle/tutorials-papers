import * as mongoose from 'mongoose'

export const ProductSchema = new mongoose.Schema({
  title: {type:String, required: true},//define mongoose types with js types (string is a ts type)
  description: {type:String, required: true},//you can also pass an object
  price:{type:Number, required: true} 
  //what the js object should look like
})//constructor

// export class Product {
//   constructor(
//     public id: string, //mongo creates the pki
//     public title: string,
//     public description: string,
//     public price: number,
//   ) {}
// }
  export interface Product extends mongoose.Document {//requires @types/mongoose
    id: string;
    title: string;
    description: string;
    price: number;
  }
