import React, { Component } from "react";
import Button from "../small_components/Button";
import DocumentLayout from "../small_components/DocumentLayout";
import "font-awesome/css/font-awesome.min.css";
import Empty_document_svg from "../../images/Empty_document_list.svg";
import FileSelectButton from "../small_components/FileSelectButton";
import FileSelectText from "../small_components/FileSelectText";

class NewDocument extends Component {
  state = {
    selectedFile: null
  };

  fileSelectedHandler = evnet => {
    this.setState({
      selectedFile: event.target.files[0]
    });
  };

  fileUploadHandler = () => {
    console.log(`Selected file: ${this.state.selectedFile.name}`);
  };

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
          src={Empty_document_svg}
          alt="logo"
          style={{ width: 400, height: 400, margin: "10px" }}
        />

        <FileSelectText>
          I feel like you have not selected any template forms...
        </FileSelectText>
        <FileSelectText>Click on Pick File to select a new form</FileSelectText>

        <FileSelectButton>
          <Button onClick={() => this.fileInput.click()}>Pick File</Button>
          <Button onClick={this.fileUploadHandler}>Upload</Button>
        </FileSelectButton>
      </DocumentLayout>
    );
  }
}

export default NewDocument;
