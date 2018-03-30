import React, { Component } from "react";
import styled from "styled-components";
import Color from "../utils/Color";
import BlankTemplates from '../small_components/BlankTemplates'
import { Switch, Route } from "react-router-dom";


// const SubsidebarWrapper = styled.div`
//   grid-column: 3/4;
//   grid-row: 2/3;
//   background-color: ${Color.subsidebar.BACKGROUND_COLOR};
//   display: flex;
//   border-left: 1px solid rgb(220, 220, 220);
//   flex-direction: column;
// `;

const SubsidebarWrapper = {
  gridColumn: 3 / 4,
  gridRow: 2 / 3,
  backgroundColor: Color.subsidebar.BACKGROUND_COLOR,
  display: "flex",
  borderLeftWidth: "1px",
  borderLeftStyle: "solid",
  borderLeftColor: "#DCDCDC",
  flexDirection: "column"
};

// Document list heading
const DocumentListHeading = styled.div`
  border-bottom: 1px solid #dcdcdc;
  position: relative;
  z-index: 50;
  background: #f9f9f9;
  padding: 19px 12px;
`;

const DocumentListHeadingRow = styled.div`
  display: flex;
  line-height: 1.125;
  align-items: center;
`;
const DocumentListHeadingText = styled.h2`
  flex: 1;
  margin: 0;
  font-weight: 600;
  line-height: inherit;
  color: ${Color.header.FONT_COLOR};
  display: block;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  font-size: 18px;
`;

const SubsidebarCloseButton = styled.button`
  background: 0 0;
  border: none;
  padding: 0;
  display: inline-block;
  width: 32px;
  height: 32px;
  line-height: 1;
  margin-left: 1px;
  margin-top: 3px;
  color: #717274;
  border-radius: 0.25rem;
  align-items: center;
  justify-content: center;
  display: flex;
  text-shadow: none;
  outline: none;
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
  state = {
    data: ''
  };

  // closeSubSidebarHandler = () => {
  //   console.log("click");
  // };


  templateData = tdata => {
    console.log('inside templateData')
      this.setState({data : tdata })
  }

  sidebarData = () => {
    let { data } = this.state
    this.props.getSidebarDataFromSubSidebar(data)
  }

  componentDidMount() {
    console.log('inside componentDidMount')
    console.log(this.state.data)
  }
  
  
  
  
  render() {
    
    console.log(`${this.state.data}`);
        

    return (
      // <SubsidebarWrapper>
      <div id="mydiv" style={SubsidebarWrapper} className="subsidebar">
        {/* <SearchWrapper>
          <SearchIconWrapper>
            <i className="far fa-search" style={SearchIcon} />
          </SearchIconWrapper>
        </SearchWrapper> */}

        <DocumentListHeading>
          <DocumentListHeadingRow>
            <DocumentListHeadingText>Document List</DocumentListHeadingText>
            <SubsidebarCloseButton>
              <i
                className="far fa-times-circle"
                style={{ fontSize: "18px" }}
                // onClick={this.closeSubSidebarHandler}
              />
            </SubsidebarCloseButton>
          </DocumentListHeadingRow>
        </DocumentListHeading>
  
       <button onClick={this.sidebarData} style={{margin : '6px'}}>Confirm your blank form</button>
   
        <BlankTemplates getTemplateData={this.templateData} />
        
        

      </div>

      // </SubsidebarWrapper>
    );
  }
}

export default Subsidebar;
