'use strict';
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = void 0;
const loader_1 = require("./trailing-spaces/loader");
function activate(context) {
    let trailingSpacesLoader = new loader_1.default();
    trailingSpacesLoader.activate(context.subscriptions);
}
exports.activate = activate;
//# sourceMappingURL=extension.js.map