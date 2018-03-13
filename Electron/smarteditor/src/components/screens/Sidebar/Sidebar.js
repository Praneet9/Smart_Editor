import React from "react";
import "./Sidebar.css";
import "font-awesome/css/font-awesome.min.css";
import TabList from "../../modules/TabList/TabList";
// import SearchDocs from "../../modules/SearchDocs/SearchDocs";

const Sidebar = () => {
  return (
    <div className="compass-sidebar">
      {/* search */}
      {/* <SearchDocs /> */}

      {/* left documenent list */}
      <TabList />
    </div>
  );
};

export default Sidebar;
