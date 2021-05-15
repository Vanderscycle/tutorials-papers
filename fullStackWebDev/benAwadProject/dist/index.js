"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const core_1 = require("@mikro-orm/core");
const post_1 = require("./entities/post");
const config_1 = __importDefault(require("./mikro-orm/config"));
const main = () => __awaiter(void 0, void 0, void 0, function* () {
    const orm = yield core_1.MikroORM.init(config_1.default);
    console.log("hello world");
    const post = orm.em.create(post_1.Post, { title: "My first post" });
    yield orm.em.persistAndFlush(post);
    console.log("--------sql2--------");
    yield orm.em.nativeInsert(post_1.Post, { title: "my second post" });
});
main().catch((err) => {
    console.error(err);
});
//# sourceMappingURL=index.js.map