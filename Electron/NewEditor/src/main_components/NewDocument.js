import React, { Component } from "react";
import Button from "../small_components/Button";
import DocumentLayout from "../small_components/DocumentLayout";

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
        <Button onClick={() => this.fileInput.click()}>Pick File</Button>
        <Button onClick={this.fileUploadHandler}>Upload</Button>
        <i className="far fa-heart" />
      </DocumentLayout>
    );
  }
}

export default NewDocument;
