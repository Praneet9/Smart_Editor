import React, { Component } from "react";
import { BrowserRouter } from "react-router-dom";
import Sidebar from "./containers/Sidebar";
import Main from "./containers/Main";
import SubSidebar from "./containers/SubSidebar";
import AppLayout from "./small_components/AppLayout";
import Header from "./main_components/Header";

class App extends Component {
  render() {
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
  }
}

export default App;
