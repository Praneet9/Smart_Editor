import React, { Component } from "react";
import "./App.css";
import { BrowserRouter, Route, Link, Switch, Redirect } from "react-router-dom";

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
            <ul>
              <li>
                <Link to="/hello">Hello</Link>
              </li>
              <li>
                <Link to="/about">About</Link>
              </li>
              <li>
                <Link to="/books">Books</Link>
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
