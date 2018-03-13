import React, { Component } from "react";
import MainScreen from "../src/components/screens/MainScreen.js/MainScreen";
import { BrowserRouter, Route } from "react-router-dom";
import OCRThisDocument from "./components/screens/OCRThisDocument/OCRThisDocument";

const App = () => (
  <BrowserRouter>
    <Route path="/" component={MainScreen} />
  </BrowserRouter>
);

export default App;
