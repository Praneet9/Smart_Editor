import React, { Component } from "react";
// import objectAssign from "object-assign";
// import RegionSelect from "./RegionSelect";
import "./style";
import Button from "../styled_components/Button";
import DocumentLayout from "../styled_components/DocumentLayout";
import "font-awesome/css/font-awesome.min.css";
import NewDocumentSVG from "../images/New-document.svg";
import FileSelectButton from "../styled_components/FileSelectButton";
import FileSelectText from "../styled_components/FileSelectText";
const $ = window.$;
const jQuery = window.jQuery;

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
    // this.regionRenderer = this.regionRenderer.bind(this);
    // this.onChange = this.onChange.bind(this);
    this._handleImageChange = this._handleImageChange.bind(this);
  }

  state = {
    regions: [],
    file: "",
    imagePreviewUrl: ""
  };

  // crop 

  componentDidMount() {

    console.log(window.$);
    $(document).ready(function () {
      console.log("Inside Ready");
    $('img#example').selectAreas({
      minSize: [10, 10],
      onChanged: debugQtyAreas,
      width: 700
    });
    $('#btnView').click(function () {
      var areas = $('img#example').selectAreas('areas');
      displayAreas(areas);
    });
    $('#btnViewRel').click(function () {
      var areas = $('img#example').selectAreas('relativeAreas');
      displayAreas(areas);
    });
    $('#btnReset').click(function () {
      output("reset")
      $('img#example').selectAreas('reset');
    });
    $('#btnDestroy').click(function () {
      $('img#example').selectAreas('destroy');

      output("destroyed")
      $('.actionOn').attr("disabled", "disabled");
      $('.actionOff').removeAttr("disabled")
    });
    $('#btnCreate').attr("disabled", "disabled").click(function () {
      $('img#example').selectAreas({
        minSize: [10, 10],
        onChanged : debugQtyAreas,
        width: 500,
      });

      output("created")
      $('.actionOff').attr("disabled", "disabled");
      $('.actionOn').removeAttr("disabled")
    });
    $('#btnNew').click(function () {
      var areaOptions = {
        x: Math.floor((Math.random() * 200)),
        y: Math.floor((Math.random() * 200)),
        width: Math.floor((Math.random() * 100)) + 50,
        height: Math.floor((Math.random() * 100)) + 20,
      };
      output("Add a new area: " + areaToString(areaOptions))
      $('img#example').selectAreas('add', areaOptions);
    });
    $('#btnNews').click(function () {
      var areaOption1 = {
        x: Math.floor((Math.random() * 200)),
        y: Math.floor((Math.random() * 200)),
        width: Math.floor((Math.random() * 100)) + 50,
        height: Math.floor((Math.random() * 100)) + 20,
      }, areaOption2 = {
        x: areaOption1.x + areaOption1.width + 10,
        y: areaOption1.y + areaOption1.height - 20,
        width: 50,
        height: 20,
      };
      output("Add a new area: " + areaToString(areaOption1) + " and " + areaToString(areaOption2))
      $('img#example').selectAreas('add', [areaOption1, areaOption2]);
    });
  });

  var selectionExists;

  function areaToString (area) {
    return (typeof area.id === "undefined" ? "" : (area.id + ": ")) + area.x + ':' + area.y  + ' ' + area.width + 'x' + area.height + '<br />'
  }

  function output (text) {
    $('#output').html(text);
  }

  // Log the quantity of selections
  function debugQtyAreas (event, id, areas) {
    console.log(areas.length + " areas", arguments);
  };

  // Display areas coordinates in a div
  function displayAreas (areas) {
    var text = "";
    $.each(areas, function (id, area) {
      text += areaToString(area);
    });
    output(text);
  };
}
// crop end

  // onChange(regions) {
  //   this.setState({
  //     regions: regions
  //   });
  // }

  // changeRegionData(index, event) {
  //   const region = this.state.regions[index];
  //   let color;
  //   switch (event.target.value) {
  //     case "1":
  //       color = "rgba(0, 255, 0, 0.5)";
  //       break;
  //     case "2":
  //       color = "rgba(0, 0, 255, 0.5)";
  //       break;
  //     case "3":
  //       color = "rgba(255, 0, 0, 0.5)";
  //       break;
  //     default:
  //       color = "rgba(0, 0, 0, 0.5)";
  //   }

  //   region.data.regionStyle = {
  //     background: color
  //   };

  //   this.onChange([
  //     ...this.state.regions.slice(0, index),
  //     objectAssign({}, region, {
  //       data: objectAssign({}, region.data, { dataType: event.target.value })
  //     }),
  //     ...this.state.regions.slice(index + 1)
  //   ]);
  // }

  // regionRenderer(regionProps) {
  //   if (!regionProps.isChanging) {
  //     return (
  //       <div style={{ position: "absolute", right: 0, bottom: "-1.5em" }}>
  //         <select
  //           onChange={event => this.changeRegionData(regionProps.index, event)}
  //           value={regionProps.data.dataType}
  //         >
  //           <option value="1">Green</option>
  //           <option value="2">Blue</option>
  //           <option value="3">Red</option>
  //         </select>
  //       </div>
  //     );
  //   }
  // }

  // image rendring

  // _handleSubmit(e) {
  //   e.preventDefault();
  //   // TODO: do something with -> this.state.file
  //   console.log("handle uploading-", this.state.file);
  // }

  // select image

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
    // const regionStyle = {
    //   background: "rgba(255, 0, 0, 0.5)"
    // };

    // image render
    let { imagePreviewUrl } = this.state;
    // let $ImageDiv = null;
    // if (imagePreviewUrl) {
    //   $ImageDiv = <img src={imagePreviewUrl} />;
    // } else {
    //   $ImageDiv = (
    //     <div className="previewText">Please select an Image for Preview</div>
    //   );
    // }


    // if file selected then show file with drag or
    // show the emmpty file select svg
    if(this.state.file) {
      return (
        <DocumentLayout>
          <h1>jQuery Select Areas Plugin Demos</h1>
          <img src={imagePreviewUrl} />
          {/* <div style={ImageDiv}>
            <img alt="Image principale" id="example" src={$ImageDiv}/>
          </div> */}
          <table>
            <tbody>
            <tr>
              <td className="actions">
                <input type="button" id="btnView" value="Display areas" className="actionOn" />
                <input type="button" id="btnViewRel" value="Display relative" className="actionOn" />
                <input type="button" id="btnNew" value="Add New" className="actionOn" />
                <input type="button" id="btnNews" value="Add 2 New" className="actionOn" />
                <input type="button" id="btnReset" value="Reset" className="actionOn" />
                <input type="button" id="btnDestroy" value="Destroy" className="actionOn" />
                <input type="button" id="btnCreate" value="Create" className="actionOff" />
              </td>
              <td>
                <div id="output" className='output'> </div>
              </td>
            </tr>
            </tbody>
          </table>
        </DocumentLayout>
      );
    } else {
      return(
        <DocumentLayout>
        <input
          type="file"
          onChange={e => this._handleImageChange(e)}
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
          {/* <Button onClick={this.fileSelectAndRender.bind(this)}>
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
        </FileSelectButton>
      </DocumentLayout>
      )
    }

    // return (
    //   <div style={{ display: "flex" }}>
    //     <input
    //       type="file"
    //       onChange={e => this._handleImageChange(e)}
    //       ref={fileSelect => (this.fileSelect = fileSelect)}
          
    //     />
    //     <div>
    //       <RegionSelect
    //         maxRegions={1}
    //         regions={this.state.regions}
    //         regionStyle={regionStyle}
    //         constraint
    //         onChange={this.onChange}
    //         regionRenderer={this.regionRenderer}
    //         style={{ border: "1px solid black" }}
    //       >
    //         <div className="ImageDiv">{$ImageDiv}</div>
    //       </RegionSelect>
    //     </div>
    //   </div>
    // );
  }
}

export default DragDocument;
