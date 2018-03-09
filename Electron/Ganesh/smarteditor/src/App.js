import React, { Component } from "react";
import "./App.css";
import { BrowserRouter, Route, Link, Switch, Redirect } from "react-router-dom";
// import FontAwesomeIcon from "@fortawesome/react-fontawesome";
import "font-awesome/css/font-awesome.min.css";

import Home from "./components/HomeComponent";
import Hello from "./components/HelloComponent";
import About from "./components/AboutComponent";
import Books from "./components/BooksComponent";

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
                <Link to="/hello" style={{ color: "#000" }}>
                  Add
                </Link>
              </li>
              <li>
                <i
                  className="fa fa-edit"
                  style={{ color: "#FFC53A", marginRight: "8px" }}
                />
                <Link to="/about" style={{ color: "#000" }}>
                  Edit
                </Link>
              </li>
              <li>
                <i
                  className="fa fa-thumbs-up"
                  style={{ color: "#EB3569", marginRight: "8px" }}
                />
                <Link to="/books" style={{ color: "#000" }}>
                  Use
                </Link>
              </li>
            </ul>
          </div>

          <Switch className="Main">
            <Route exact path="/" component={Home} />
            <Route path="/about" component={About} />
            <Route path="/hello" component={Hello} />
            <Route path="/books" component={Books} />
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
