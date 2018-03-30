import React, { Component } from "react";
import Button from "../styled_components/Button";
import DocumentLayout from "../styled_components/DocumentLayout";
import "font-awesome/css/font-awesome.min.css";
import SearchDocument from "../images/SearchDocument.svg";
// import FileSelectButton from "../styled_components/FileSelectButton";
import FileSelectText from "../styled_components/FileSelectText";

export default class AddDocument extends Component {
  constructor(props) {
    super(props);
    this._handleImageChange = this._handleImageChange.bind(this);
  }

  state = {
    regions: [],
    file: "",
    imagePreviewUrl: ""
  };

  _handleImageChange(e) {
    e.preventDefault();

    let reader = new FileReader();
    let file = e.target.files[0];

    reader.onloadend = () => {
      this.setState({
        file: file,
        imagePreviewUrl: reader.result
      });
    };

    reader.readAsDataURL(file);
  }

  // callTwoFunctions = event => {
  //   console.log("callTwoFunctions");
  //   this.passImagePreviewUrlToParent;
  //   this.getHeaderFormName;
  // };

  passImagePreviewUrlToParent = () => {
    console.log("inside passImagePreviewUrlToParent");
    let { imagePreviewUrl } = this.state;

    // this.props.getImagePreviewUrl({
    //   imagedata: imagePreviewUrl,
    //   handle: true
    // });
    this.props.getImagePreviewUrl(imagePreviewUrl);
  };

  // getHeaderFormName = () => {
  //   let { file } = this.state;
  //   this.props.headerFormName(file.name);
  // };

  render() {
    let filename = null;
    let image = null;
    let { imagePreviewUrl } = this.state;
    let btn = null;

    console.log(this.props.sendTemplateDataToEditDocument);

    if (this.state.file && this.state.imagePreviewUrl) {
      image = (
        <img
          src={imagePreviewUrl}
          alt="logo"
          style={{ width: 450, height: 650, margin: "10px" }}
        />
      );
      filename = (
        <div>
          <FileSelectText>You have selected</FileSelectText>

          <FileSelectText>
            <strong>{this.state.file.name}</strong>
          </FileSelectText>
        </div>
      );

      btn = <Button onClick={this.passImagePreviewUrlToParent}>Upload</Button>;
    } else {
      image = (
        <img
          src={SearchDocument}
          alt="logo"
          style={{ width: 400, height: 400, margin: "10px" }}
        />
      );

      <FileSelectText>
        Select your fill form...
      </FileSelectText>;

      filename = (
        <FileSelectText>
          Click on Pick File to select your fill form
        </FileSelectText>
      );

      btn = <Button onClick={() => this.fileInput.click()}>Pick File</Button>;
    }

    return (
      <DocumentLayout>
        <input
          type="file"
          onChange={e => this._handleImageChange(e)}
          style={{ display: "none" }}
          ref={fileInput => (this.fileInput = fileInput)}
        />

        {image}

        {filename}

        {btn}
      </DocumentLayout>
    );
  }
}
