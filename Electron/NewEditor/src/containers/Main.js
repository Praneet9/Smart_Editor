import React from "react";
import { Switch, Route } from "react-router-dom";
import styled from "styled-components";
import EditDocument from "../main_components/EditDocument";
import UseDocument from "../main_components/UseDocument";
import MainDocument from "../main_components/MainDocument";
import ShowLables from "../small_components/ShowLables";

const MainWrapper = styled.div`
  display: grid;
  grid-column: 2/3;
`;

const Main = () => {


  return (
    <MainWrapper>
      <Switch>
        <Route
          exact
          path="/"
          component={MainDocument}
        />
        <Route exact path="/edit" component={EditDocument} />
        <Route exact path="/use" component={UseDocument} />
        <Route exact path="/showlabelÍ" component={ShowLables} />
      </Switch>
    </MainWrapper>
  );
};

export default Main;
