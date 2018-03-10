import React, { Component } from "react";
import "./App.css";
import { BrowserRouter, Route, Link, Switch, Redirect } from "react-router-dom";
// import FontAwesomeIcon from "@fortawesome/react-fontawesome";
import "font-awesome/css/font-awesome.min.css";

import Add from "./components/AddComponent";
import Edit from "./components/EditComponent";
import Use from "./components/UseComponent";
// import Hello from "./components/HelloComponent";

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div className="App">
          <div className="Sidebar">
            <button className="Add-docs-button">Add new document</button>
            <ul>
              <li>
                <i
                  className="fa fa-plus"
                  style={{ color: "#8268FC", marginRight: "8px" }}
                />
                <Link to="/" style={{ color: "#000" }}>
                  Add
                </Link>
              </li>
              <li>
                <i
                  className="fa fa-edit"
                  style={{ color: "#FFC53A", marginRight: "8px" }}
                />
                <Link to="/edit" style={{ color: "#000" }}>
                  Edit
                </Link>
              </li>
              <li>
                <i
                  className="fa fa-thumbs-up"
                  style={{ color: "#EB3569", marginRight: "8px" }}
                />
                <Link to="/use" style={{ color: "#000" }}>
                  Use
                </Link>
              </li>
            </ul>
          </div>

          <Switch className="Main">
            <Route exact path="/" component={Add} />
            <Route path="/edit" component={Edit} />
            <Route path="/use" component={Use} />
            {/* <Route path="/books" component={Books} /> */}
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
