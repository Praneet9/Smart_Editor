import React, { Component } from "react";

class Home extends Component {
  state = {
    selectedFile: null
  };

  fileSelectedHandler = event => {
    // console.log(event.target.files[0]);
    this.setState({
      selectedFile: event.target.files[0]
    });
  };

  fileUploadHandler = () => {
    // Upload file to the database
    // const fd = new FormData();
    // axios
    //   .post("url", fd, {
    //     onUploadProgress: progressEvent => {
    //       console.log(
    //         "Upload Progress: " +
    //           Math.round(progressEvent.loaded / progressEvent.total * 100) +
    //           "%"
    //       );
    //     }
    //   })
    //   .then(res => {
    //     console.log(res);
    //   });
    // console.log(`Selected file is ${JSON.stringify(this.state.selectedFile)}`);
    console.log(
      `Selected file name is ${JSON.stringify(this.state.selectedFile.name)}`
    );
  };

  render() {
    return (
      <div>
        <input
          type="file"
          style={{ display: "none" }}
          onChange={this.fileSelectedHandler}
          ref={fileInput => (this.fileInput = fileInput)}
          onChange={this.fileSelectedHandler}
        />
        <button onClick={() => this.fileInput.click()}>
          Pick a new document
        </button>
        <button onClick={this.fileUploadHandler}>Upload</button>
      </div>
    );
  }
}

export default Home;
