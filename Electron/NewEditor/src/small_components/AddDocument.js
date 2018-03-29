import React, { Component } from "react";
import Button from "../styled_components/Button";
import DocumentLayout from "../styled_components/DocumentLayout";
import "font-awesome/css/font-awesome.min.css";
import NewDocumentSVG from "../images/New-document.svg";
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

  passImagePreviewUrlToParent = () => {
    console.log("inside passImagePreviewUrlToParent");
    let { imagePreviewUrl } = this.state;
    this.props.getImagePreviewUrl(imagePreviewUrl);

    
    // fetch
    fetch("http://localhost:5000/file", {
      method: 'POST',
      body: this.state.file
    }).then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))

  };


  render() {
    console.log(this.state.file)
    let filename = null;
    let image = null;
    let { imagePreviewUrl } = this.state;
    let btn = null;

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
          src={NewDocumentSVG}
          alt="logo"
          style={{ width: 400, height: 400, margin: "10px" }}
        />
      );

      <FileSelectText>
        Feel like you have not selected any template forms...
      </FileSelectText>;

      filename = (
        <FileSelectText>
          Click on Pick File to select a new template form
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
