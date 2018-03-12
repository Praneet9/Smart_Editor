import React, { Component } from "react";
import "./App.css";
import { BrowserRouter, Route, Link, Switch, Redirect } from "react-router-dom";
// import FontAwesomeIcon from "@fortawesome/react-fontawesome";
import "font-awesome/css/font-awesome.min.css";

import FilterDocs from "../src/components/modules/FilterDocs/FilterDocs.js";

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div className="page-container">
          {/* header */}
          <div className="instance-header">
            <div className="instance-header-connecting-string">
              <div className="instance-header-icon-container">
                <i className="fa fa-file instance-header-icon-home" />
              </div>
              <div className="instance-header-details">All Documents</div>
            </div>
            <div className="instance-header-items-left ">
              <div className="instance-header-details-left-details">
                {/* content header title which document is open */}
              </div>
            </div>
            <div className="instance-header-items-right">
              <div className="instance-header-items-right-details">
                Document
              </div>
            </div>
          </div>
          {/* body */}
          <div className="page">
            {/* sidebar */}
            <FilterDocs />

            {/* content */}
            <div className="content">
              <OCRThisDocument />
            </div>
          </div>
        </div>

        {/* <div className="Sidebar">
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
          </div> */}

        {/* <Switch className="Main">
            <Route exact path="/" component={Add} />
            <Route path="/edit" component={Edit} />
            <Route path="/use" component={Use} />
            <Route path="/books" component={Books} /> 
          </Switch> */}
      </BrowserRouter>
    );
  }
}

export default App;
