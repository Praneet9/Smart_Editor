import React from "react";
import "./FilterDocs.css";
import "font-awesome/css/font-awesome.min.css";
import DocumentList from "../../modules/DocumentList/DocumentList";
import SearchDocs from "../../modules/SearchDocs/SearchDocs";

const FilterDocs = () => {
  return (
    <div className="compass-sidebar">
      {/* search */}
      <SearchDocs />

      {/* left documenent list */}
      <DocumentList />
    </div>
  );
};

export default FilterDocs;
