import mongoose, { Schema } from "mongoose";

const CoordinateSchema = new Schema({
  id: {
    type: String
  },
  x: {
    type: String
  },
  y: {
    type: String
  },
  width: {
    type: String
  },
  height: {
    type: String
  }
});

export default mongoose.model("User", UserSchema);
