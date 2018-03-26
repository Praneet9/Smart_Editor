import React, { Component } from "react";
import objectAssign from "object-assign";
import RegionSelect from "./RegionSelect";
import "./style";
import myImg from "../static/form.png";

const ImageDiv = {
  textAlign: "center",
  margin: "5px 15px",
  height: "200px",
  width: "500px",
  borderLeft: "1px solid gray",
  borderRight: "1px solid gray",
  borderTop: "5px solid gray",
  borderBottom: "5px solid gray",
  background: "#e8e8e8"
};

class DragDocument extends Component {
  constructor(props) {
    super(props);
    this.regionRenderer = this.regionRenderer.bind(this);
    this.onChange = this.onChange.bind(this);
    this._handleImageChange = this._handleImageChange.bind(this);
  }

  state = {
    regions: [],
    file: "",
    imagePreviewUrl: ""
  };

  onChange(regions) {
    this.setState({
      regions: regions
    });
  }

  changeRegionData(index, event) {
    const region = this.state.regions[index];
    let color;
    switch (event.target.value) {
      case "1":
        color = "rgba(0, 255, 0, 0.5)";
        break;
      case "2":
        color = "rgba(0, 0, 255, 0.5)";
        break;
      case "3":
        color = "rgba(255, 0, 0, 0.5)";
        break;
      default:
        color = "rgba(0, 0, 0, 0.5)";
    }

    region.data.regionStyle = {
      background: color
    };

    this.onChange([
      ...this.state.regions.slice(0, index),
      objectAssign({}, region, {
        data: objectAssign({}, region.data, { dataType: event.target.value })
      }),
      ...this.state.regions.slice(index + 1)
    ]);
  }

  regionRenderer(regionProps) {
    if (!regionProps.isChanging) {
      return (
        <div style={{ position: "absolute", right: 0, bottom: "-1.5em" }}>
          <select
            onChange={event => this.changeRegionData(regionProps.index, event)}
            value={regionProps.data.dataType}
          >
            <option value="1">Green</option>
            <option value="2">Blue</option>
            <option value="3">Red</option>
          </select>
        </div>
      );
    }
  }

  // image rendring

  // _handleSubmit(e) {
  //   e.preventDefault();
  //   // TODO: do something with -> this.state.file
  //   console.log("handle uploading-", this.state.file);
  // }

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

  render() {
    // drag
    const regionStyle = {
      background: "rgba(255, 0, 0, 0.5)"
    };

    // image render
    let { imagePreviewUrl } = this.state;
    let $ImageDiv = null;
    if (imagePreviewUrl) {
      $ImageDiv = <img src={imagePreviewUrl} />;
    } else {
      $ImageDiv = (
        <div className="previewText">Please select an Image for Preview</div>
      );
    }

    return (
      <div style={{ display: "flex" }}>
        <input
          type="file"
          onChange={e => this._handleImageChange}
          ref={fileSelect => (this.fileSelect = fileSelect)}
          style={{ display: "none" }}
        />
        <div>
          <RegionSelect
            maxRegions={1}
            regions={this.state.regions}
            regionStyle={regionStyle}
            constraint
            onChange={this.onChange}
            regionRenderer={this.regionRenderer}
            style={{ border: "1px solid black" }}
          >
            <div className="ImageDiv">{$ImageDiv}</div>
          </RegionSelect>
        </div>
      </div>
    );
  }
}

export default DragDocument;
