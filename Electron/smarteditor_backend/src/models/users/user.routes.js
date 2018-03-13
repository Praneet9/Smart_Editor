import { Router } from "express";
import * as UserController from "./user.controller";

const routes = new Router();

routes.post("/signup", UserController.createUser);
routes.post("/signin", UserController.SigninUser);

export default routes;
