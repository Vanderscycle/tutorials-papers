import { __prod__ } from "../constants";
import { Post } from "../entities/post";
import { MikroORM } from "@mikro-orm/core"

export default {
dbName: "benawad",
entities: [Post],
user: "",
password: "",
type: "postgresql",
debug: !__prod__, //really cool way to not repeat ourselves

} as Parameters<typeof MikroORM.init>[0];//Parameters returns an array 
// as const //casting so that type is not string but postgresql (intermediate)
