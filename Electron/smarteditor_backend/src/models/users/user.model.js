import mongoose, { Schema } from "mongoose";

const UserSchema = new Schema(
  {
    name: {
      type: String,
      required: [true, "Name is required!"]
    },
    email: {
      type: String,
      required: [true, "Email is required!"],
      unique: true
    },
    password: {
      type: String,
      required: [true, "Password is required!"]
    }
  },
  { timestamp: true }
);

export default mongoose.model("User", UserSchema);
