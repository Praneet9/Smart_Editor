import styled from "styled-components";
import Color from "../utils/Color";
import React, { Component } from "react";

const SubsidebarWrapper = styled.div`
  grid-column: 2;
  grid-row: 1 / 4;
  background-color: ${Color.subsidebar.BACKGROUND_COLOR};
  display: flex;
  flex-direction: column;
  align-itmes: center;
`;

const DocumentListHeading = styled.div`
  padding: 0;
  margin: 0;
  width: 100%;
  height: 26px;
  display: flex;
  align-items: center;
  padding-top: 18px;
`;
const DocumentListHeadingText = styled.span`
  line-height: 1;
  display: block;
  opacity: 1;
  text-align: center;
  width: 100%;
  transition: color 0.1s ease-out;
  white-space: nowrap;
  color: #fff;
`;

class Subsidebar extends Component {
  render() {
    return (
      <SubsidebarWrapper>
        <DocumentListHeading>
          <DocumentListHeadingText>Document List</DocumentListHeadingText>
        </DocumentListHeading>
      </SubsidebarWrapper>
    );
  }
}

export default Subsidebar;
