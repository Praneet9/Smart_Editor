import React from "react";
import "./FilterDocs.css";
import DocumentList from "../DocumentList/DocumentList";
import "font-awesome/css/font-awesome.min.css";

const FilterDocs = () => {
  return (
    <div className="compass-sidebar">
      {/* search */}
      <div className="compass-sidebar-filter">
        <i className="fa fa-search compass-sidebar-search-icon" />
        <input className="compass-sidebar-search-input" placeholder="filter" />
      </div>

      {/* left */}
      <DocumentList />
    </div>
  );
};

export default FilterDocs;
