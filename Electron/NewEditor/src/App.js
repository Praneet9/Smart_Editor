import React from "react";
import { BrowserRouter } from "react-router-dom";
import Sidebar from "./containers/Sidebar";
import Main from "./containers/Main";
import SubSidebar from "./containers/SubSidebar";
import AppLayout from "./styled_components/AppLayout";
import Header from "./main_components/Header";

const App = props => {
  return (
    <BrowserRouter>
      <AppLayout>
        <Sidebar />
        <Header documentName="Form Name" />
        <Main />
        <SubSidebar />
      </AppLayout>
    </BrowserRouter>
  );
};

export default App;
