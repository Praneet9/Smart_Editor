import React from "react";
import { Switch, Route } from "react-router-dom";
import NewDocument from "../main_components/NewDocument";
import EditDocument from "../main_components/EditDocument";
import UseDocument from "../main_components/UseDocument";

const Main = () => (
  <Switch>
    <Route exact path="/" component={NewDocument} />
    <Route exact path="/edit" component={EditDocument} />
    <Route exact path="/use" component={UseDocument} />
  </Switch>
);

export default Main;
