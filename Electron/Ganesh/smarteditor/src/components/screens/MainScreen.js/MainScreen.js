import React, { Component } from "react";
import "./MainScreen.css";
import { BrowserRouter, Route, Link, Switch, Redirect } from "react-router-dom";
// import FontAwesomeIcon from "@fortawesome/react-fontawesome";
import "font-awesome/css/font-awesome.min.css";

import FilterDocs from "../../modules/Filterdocs/FilterDocs";
import OCRThisDocument from "../OCRThisDocument/OCRThisDocument";

class MainScreen extends Component {
  render() {
    return (
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
            <div className="instance-header-items-right-details">Document</div>
          </div>
        </div>
        {/* body */}
        <div className="page">
          {/* sidebar */}
          <FilterDocs />

          {/* content */}
          <div className="content">{/* <OCRThisDocument /> */}</div>
        </div>
      </div>
    );
  }
}

export default MainScreen;
