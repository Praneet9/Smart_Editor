import React from "react";
import styled from "styled-components";
import { Header } from "semantic-ui-react";

const HeaderWrapper = styled.div`
  grid-column: 3;
  grid-row: 1;
  background-color: #e8e8e8;
  color: #2c2d30;
  line-height: 1.3;
  font-size: 18px;
  display: flex;
  justify-content: row;
  margin: 0;
  padding-left: 16px
  align-items: center;
`;

export default ({ documentName }) => (
  <HeaderWrapper>
    <i
      className="far fa-file-alt"
      style={{ fontSize: "16px", marginRight: "6px" }}
    />
    <Header textAlign="center">{documentName}</Header>
  </HeaderWrapper>
);
