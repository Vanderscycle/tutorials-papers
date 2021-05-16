//https://mikro-orm.io/docs/defining-entities
import { Entity, PrimaryKey, Property } from "@mikro-orm/core";

@Entity()
export class Post {
    @PrimaryKey()
    id!: number;

    @Property() // {type: "date"}
    createdAt: Date = new Date();

    @Property({ onUpdate: () => new Date() })
    updatedAt: Date = new Date();

    @Property({type: 'text'})
    title!: string;
}
