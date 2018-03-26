import React, { Component } from "react";
import Button from "../styled_components/Button";
import DocumentLayout from "../styled_components/DocumentLayout";
import "font-awesome/css/font-awesome.min.css";
import NewDocumentSVG from "../images/New-document.svg";
import FileSelectButton from "../styled_components/FileSelectButton";
import FileSelectText from "../styled_components/FileSelectText";
import { Link } from "react-router-dom";

class NewDocument extends Component {
  state = {
    selectedFile: null
  };

  fileSelectedHandler = event => {
    this.setState({
      selectedFile: event.target.files[0]
    });
  };

  fileUploadHandler = () => {
    console.log(`Selected file: ${this.state.selectedFile.name}`);
  };

  fileSelectAndRender = () => {
    this.foo.toogle();
  
  }

  render() {
    return (
      <DocumentLayout>
        <input
          type="file"
          onChange={this.fileSelectedHandler}
          style={{ display: "none" }}
          ref={fileInput => (this.fileInput = fileInput)}
        />
        <img
          src={NewDocumentSVG}
          alt="logo"
          style={{ width: 400, height: 400, margin: "10px" }}
        />

        <FileSelectText>
          I feel like you have not selected any template forms...
        </FileSelectText>
        <FileSelectText>Click on Pick File to select a new form</FileSelectText>

        <FileSelectButton>
          <Button onClick={() => this.fileInput.click()}>Pick File</Button>
          {/* <Button onClick={this.fileUploadHandler}>
            <Link
              to="/drag"
              style={{
                textDecoration: "none",
                color: " #2c2d30",
                fontWeight: 700,
                fontSize: "14px"
              }}
            >
              Upload
            </Link>
          </Button> */}
          <Button onClick={this.fileSelectAndRender.bind(this)}>
            <Link
              to="/drag"
              style={{
                textDecoration: "none",
                color: " #2c2d30",
                fontWeight: 700,
                fontSize: "14px"
              }}
            >
              Upload
            </Link>
          </Button>
        </FileSelectButton>
      </DocumentLayout>
    );
  }
}

export default NewDocument;
