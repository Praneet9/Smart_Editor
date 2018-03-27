import React from "react";
import { Switch, Route } from "react-router-dom";
import NewDocument from "../main_components/NewDocument";
import EditDocument from "../main_components/EditDocument";
import UseDocument from "../main_components/UseDocument";
import DragDocument from "../main_components/DragDocument";
import crop from "../main_components/crop";
import styled from "styled-components";

const MainWrapper = styled.div`
  display: grid;
  grid-column: 2/3;
`;

const Main = () => (
  <MainWrapper>
    <Switch>
      <Route exact path="/" component={crop} />
      <Route exact path="/edit" component={EditDocument} />
      <Route exact path="/use" component={UseDocument} />
      {/* <Route exact path="/drag" component={DragDocument} /> */}
      {/* <Route exact path="/crop" component={crop} /> */}
    </Switch>
  </MainWrapper>
);

export default Main;
