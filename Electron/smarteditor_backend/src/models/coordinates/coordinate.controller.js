import Coordinate from "./coordinate.model.js";

// Set new Coordinates
export const setCoordinates = async (req, res) => {
  const { id, x, y, width, height } = req.body;
  const newCoord = new Coordinate({
    id,
    x,
    y,
    width,
    height
  });

  try {
    return res.status(201).json({
      coordinate: await newCoord.save()
    });
  } catch (error) {
    return res.status(error.status).json({
      error: true,
      message: "Error in setting new Coordinates!"
    });
  }
};

get