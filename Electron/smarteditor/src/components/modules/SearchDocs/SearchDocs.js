import React from "react";
import "./SearchDocs.css";

const SearchDocs = () => (
  <div className="compass-sidebar-filter">
    <i className="fa fa-search compass-sidebar-search-icon" />
    <input className="compass-sidebar-search-input" placeholder="filter" />
  </div>
);

export default SearchDocs;
