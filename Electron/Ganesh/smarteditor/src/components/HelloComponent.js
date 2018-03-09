import React from "react";

const Hello = () => {
  return (
    <h1>
      <h1>Hello, world!</h1>
      <p style={{ display: "flex" }}>
        I recently built an Electron app using create-react-app. I didn’t need
        to muck about with Webpack, or “eject” my app, either. I’ll walk you
        through how I accomplished this. I was drawn to the idea of using
        create-react-app because it hides the webpack configuration details. But
        my search for existing guides for using Electron and create-react-app
        together didn’t bear any fruit, so I just dove in and figured it out
        myself. If you’re feeling impatient, you can dive right in and look at
        my code. Here’s the GitHub repo for my app. Before we get started, let
        me tell you about Electron and React, and why create-react-app is such a
        great tool.
      </p>
    </h1>
  );
};

export default Hello;
