import React from "react";
import styled from "styled-components";
// import { Header } from "semantic-ui-react";
import Color from "../utils/Color";
import "font-awesome/css/font-awesome.min.css";

const HeaderWrapper = styled.div`
  grid-column: 2/4;
  grid-row: 1;
  background-color: ${Color.header.BACKGROUND_COLOR};
  line-height: 1.3;
  font-size: 18px;
  margin: 0;
  border-bottom: 1px solid rgb(220, 220, 220);
`;

const FormHeader = styled.div`
  display: flex;
  background: ${Color.header.BACKGROUND_COLOR};
  align-items: center;
  height: 100%;
  box-shadow: 1px 1px 0 0 0 #e8e8e8;
`;

const FormNameHeader = styled.div`
  display: flex;
  flex: 1;
  min-width: 1px;
  color: #ffffff;
`;

const HeaderLeft = styled.div`
  display: flex;
  flex: 1;
  min-width: 1px;
  color: ${Color.header.BACKGROUND_COLOR};
  flex-direction: column;
`;

const FormnameContainer = styled.div`
  display: flex;
  transition: 0.15s;
  user-select: none;
`;

const FormnameSpan = styled.span`
  line-height: 1.3;
  font-size: 18px;
  display: flex;
  min-width: 1px;
  user-select: text;
  margin: 0 0 -2px;
  font-weight: 900;
  padding: 0 0.1rem 0 1.3rem;
  color: ${Color.header.FONT_COLOR};
  cursor: pointer;
  align-items: baseline;
`;
const FormDetails = styled.div`
  display: flex;
  align-items: center;
  margin-top: 5px;
  padding-left: 1.3rem;
  font-size: 0.8125rem;
  font-weight: 400;
  line-height: 1.16;
  color: ${Color.header.SUBFONT_COLOR};
`;

const FormDetailsHeader = styled.div`
  display: flex;
  flex: 1;
  min-width: 1px;
  justify-content: flex-end;
  margin-right: 16px;
`;

const FormDetailIcon = styled.div`
  background: 0 0;
  border: none;
  padding: 0;
  display: inline-block;
  width: 32px;
  height: 32px;
  line-height: 1;
  margin-left: 1px;
  margin-top: 4px;
  color: #717274;
  border-radius: 0.25rem;
  align-items: center;
  justify-content: center;
  display: flex;
`;

const SearchContainer = styled.div`
  flex: 1;
  position: relative;
  z-index: 0;
  max-width: 300px;
  margin: 0 8px 0 8px;
`;
const SearchForm = styled.form`
  border-color: #717274;
  display: flex;
  align-items: center;
  padding: 2px 0;
  height: 34px;
  border-radius: 0.35rem;
  border: 1px solid #a0a0a2;
`;

const SearchIcon = styled.div`
  width: 30px;
  flex: none;
  flex: none;
  top: 0;
  left: 0;
  z-index: 1;
  margin-left: 8px;
  margin-right: 6px;
  text-shadow: none;
  opacity: 1;
  width: 18px;
  height: 18px;
  line-height: 18px;
  position: static;
  color: #717274;
`;

const SearchInput = styled.div`
  font-size: 15px;
  display: flex;
  align-items: baseline;
  flex: 1;
  min-width: 0;
  box-shadow: none;
  padding: 0;
  border: none;
  border-radius: 0;
  display: block;
`;

export default ({ documentName }) => (
  <HeaderWrapper>
    <FormHeader>
      <FormNameHeader>
        {/* left */}
        <HeaderLeft>
          <FormnameContainer>
            <FormnameSpan>{documentName}</FormnameSpan>
          </FormnameContainer>

          <FormDetails>Modified at</FormDetails>
        </HeaderLeft>
      </FormNameHeader>

      <FormDetailsHeader>
        <FormDetailIcon>
          <i className="far fa-file-alt" />
        </FormDetailIcon>

        <FormDetailIcon>
          <i className="far fa-star" style={{ fontSize: "18px" }} />
        </FormDetailIcon>

        <SearchContainer>
          <SearchForm>
            <SearchIcon>
              <i
                className="fa fa-search"
                style={{ color: "#717274", fontSize: "18px", fontWeight: 300 }}
              />
            </SearchIcon>
            <SearchInput>Search</SearchInput>
          </SearchForm>
        </SearchContainer>

        <FormDetailIcon>
          <i className="fa fa-ellipsis-v" />
        </FormDetailIcon>
      </FormDetailsHeader>

      {/* right */}
    </FormHeader>
  </HeaderWrapper>
);
