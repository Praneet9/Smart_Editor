import styled from "styled-components";
import Color from "../utils/Color";
import React, { Component } from "react";

const SubsidebarWrapper = styled.div`
  grid-column: 3/4;
  grid-row: 2/3;
  background-color: ${Color.subsidebar.BACKGROUND_COLOR};
  display: flex;
  border-left: 1px solid rgb(220, 220, 220);
  flex-direction: column;
`;

// Document list heading
const DocumentListHeading = styled.div`
  padding: 0;
  margin: 0;
  width: 100%;
  height: 26px;
  display: flex;
  align-items: center;
  padding: 18px;
  align-items: flex-start;
`;
const DocumentListHeadingText = styled.span`
  line-height: 1;
  display: block;
  opacity: 1;
  text-align: left;
  width: 100%;
  font-size: 17px;
  transition: color 0.1s ease-out;
  white-space: nowrap;
  color: ${Color.header.FONT_COLOR};
  font-weight: 600;
`;

// Search icon
// const SearchWrapper = styled.div`
//   flex: 1;
//   border-color: #fff;
//   box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
//   display: flex;
//   align-items: center;
//   padding: 2px 0;
//   height: 34px;
//   border-radius: 0.35rem;
//   border: 1px solid #fff;
// `;

// const SearchIconWrapper = styled.div`
//   width: 30px;
//   flex: none;
// `;

// const SearchIcon = {
//   flex: "none",
//   top: 0,
//   left: 0,
//   marginLeft: "5px",
//   textShadow: "none",
//   opacity: 1,
//   width: " 17px",
//   height: "17px",
//   lineHeight: "17px",
//   position: "static",
//   color: "#fff"
// };

class Subsidebar extends Component {
  render() {
    return (
      <SubsidebarWrapper>
        {/* <SearchWrapper>
          <SearchIconWrapper>
            <i className="far fa-search" style={SearchIcon} />
          </SearchIconWrapper>
        </SearchWrapper> */}

        <DocumentListHeading>
          <DocumentListHeadingText>Document List</DocumentListHeadingText>
        </DocumentListHeading>
      </SubsidebarWrapper>
    );
  }
}

export default Subsidebar;
