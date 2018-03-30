import React, { Component } from "react";
import { BrowserRouter } from "react-router-dom";
import Sidebar from "./containers/Sidebar";
import Main from "./containers/Main";
import SubSidebar from "./containers/SubSidebar";
import AppLayout from "./styled_components/AppLayout";
import Header from "./main_components/Header";

class App extends Component {
  state = {
      data: ''
  }

  sidebarData = thisIsSidebarData => {
    this.setState({data: thisIsSidebarData})
  }

  componentDidMount() {
    console.log(this.state.data)
  }


  render() {
  console.log(this.state.data);
  return (
    <BrowserRouter>
      <AppLayout>
        <Sidebar />
        <Header documentName="Form Name" />
        <Main sendTemplateDataToMain={this.state.data}/>
        <SubSidebar getSidebarDataFromSubSidebar={this.sidebarData}/>
      </AppLayout>
    </BrowserRouter>
  );
 }
};

export default App;
