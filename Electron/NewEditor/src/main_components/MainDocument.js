import React, { Component } from "react";
import DocumentLayout from "../styled_components/DocumentLayout";
import AddDocument from "../small_components/AddDocument";
import DragAndShowLables from '../small_components/DragAndShowLables';

export default class MainDocument extends Component {
  state = {
    imagePreviewUrl: "",
  };

  passImagePreviewUrlToParent = imagedata=> {
    this.setState({ imagePreviewUrl: imagedata});
  };



  render() {

    let whatToShow = null;
    if (this.state.imagePreviewUrl) {
      whatToShow = (
        // <DragThisDocument
        //     setImagePreivewUrl={this.state.imagePreviewUrl}
        // />
         <DragAndShowLables setImagePreivewUrl={this.state.imagePreviewUrl}/>   
      );
    } else {
      whatToShow = (
        <AddDocument getImagePreviewUrl={this.passImagePreviewUrlToParent} />
      );
    }
    return <DocumentLayout>{whatToShow}</DocumentLayout>;





  }
}
