import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { Product } from './product.model';

@Injectable()
export class ProductsService {
  // private products: Product[] = [];
  // build a simple local api and then adds moongoose/typegoose

  constructor(//WARN:don't quite understand how model and service are linkded
    @InjectModel('Product') private readonly productModel: Model<Product>,
  ) {}

  async insertProduct(title: string, desc: string, price: number) {
    const newProduct = new this.productModel({
      title: title,
      description: desc,
      price: price,
    });
    const result = await newProduct.save();
    console.log(result);
    return result.id as string;
    //return 'prodId';
  }

  async getProducts() {
    const products = await this.productModel.find().exec();
    // console.log(products)
    // return products as Product[];
    return products.map((prod) => ({
      id: prod.id,
      title: prod.title,
      description: prod.description,
      price: prod.price,
    })); //if we want to rename some of the tiles.
  }

  async getSingleProduct(productId: string) {
    const product = await this.findProduct(productId); //in this case we need the post actual mongo id
    return {
      id: product.id,
      title: product.title,
      description: product.description,
      price: product.price,
    };
  }

  async updateProduct(
    productId: string,
    title: string,
    desc: string,
    price: number,
  ) {
    //fetch from db and then update
    const updatedProduct = await this.findProduct(productId);
    if (title) {
      updatedProduct.title = title;
    }
    if (desc) {
      updatedProduct.description = desc;
    }
    if (price) {
      updatedProduct.price = price;
    }
    // because mongoose return an object of our data and not a mongoose object we need to extend the class
    updatedProduct.save();
  }

  async deleteProduct(prodId: string) {
    const result = await this.productModel.deleteOne({_id: prodId}).exec();//has to be _id because that's the correct label in the mongosse db
    if (result.n === 0 ) {
      throw new NotFoundException('Product does not exist');

    }
    console.log(result)
  }

  private async findProduct(id: string): Promise<Product> {
    let product; //has to change because of const in try block?
    try {
      product = await this.productModel.findById(id); //findone but uses id as index
    } catch (error) {
      throw new NotFoundException('Could not find product.');
    }
    if (!product) {
      throw new NotFoundException('Could not find product.');
    }
    return product
    // return {
    //   id: product.id,
    //   title: product.title,
    //   description: product.description,
    //   price: product.price,
    // };
  }
}
