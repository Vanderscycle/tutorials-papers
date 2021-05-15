"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const constants_1 = require("../constants");
const post_1 = require("../entities/post");
exports.default = {
    dbName: "benawad",
    entities: [post_1.Post],
    user: "",
    password: "",
    type: "postgresql",
    debug: !constants_1.__prod__,
};
//# sourceMappingURL=config.js.map