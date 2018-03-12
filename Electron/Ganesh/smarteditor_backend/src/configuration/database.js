import mongoose from "mongoose";
import constants from "./constants";

mongoose.Promise = global.Promise;

try {
  mongoose.connect(constants.MONGO_URL);
} catch (error) {
  mongoose.createConnection(constants.MONGO_URL);
}

mongoose.connection
  .once("open", () => console.log("MongoDB is running"))
  .on("error", error => {
    console.log("Something is wrong with MongoDB: ", error);
    throw error;
  });
