import React, { Component } from "react";

const $ = window.$;
// const jQuery = window.jQuery;

export default class DragThisDocument extends Component {
  componentDidMount() {
    console.log(window.$);
    $(document).ready(function() {
      console.log("Inside Ready");
      $("img#example").selectAreas({
        minSize: [10, 10],
        onChanged: debugQtyAreas,
        width: 700
      });
      $("#btnView").click(function() {
        var areas = $("img#example").selectAreas("areas");
        displayAreas(areas);
      });
      $("#btnViewRel").click(function() {
        var areas = $("img#example").selectAreas("relativeAreas");
        displayAreas(areas);
      });
      $("#btnReset").click(function() {
        output("reset");
        $("img#example").selectAreas("reset");
      });
      $("#btnDestroy").click(function() {
        $("img#example").selectAreas("destroy");

        output("destroyed");
        $(".actionOn").attr("disabled", "disabled");
        $(".actionOff").removeAttr("disabled");
      });
      $("#btnCreate")
        .attr("disabled", "disabled")
        .click(function() {
          $("img#example").selectAreas({
            minSize: [10, 10],
            onChanged: debugQtyAreas,
            width: 500
          });

          output("created");
          $(".actionOff").attr("disabled", "disabled");
          $(".actionOn").removeAttr("disabled");
        });
      $("#btnNew").click(function() {
        var areaOptions = {
          x: Math.floor(Math.random() * 200),
          y: Math.floor(Math.random() * 200),
          width: Math.floor(Math.random() * 100) + 50,
          height: Math.floor(Math.random() * 100) + 20
        };
        output("Add a new area: " + areaToString(areaOptions));
        $("img#example").selectAreas("add", areaOptions);
      });
      $("#btnNews").click(function() {
        var areaOption1 = {
            x: Math.floor(Math.random() * 200),
            y: Math.floor(Math.random() * 200),
            width: Math.floor(Math.random() * 100) + 50,
            height: Math.floor(Math.random() * 100) + 20
          },
          areaOption2 = {
            x: areaOption1.x + areaOption1.width + 10,
            y: areaOption1.y + areaOption1.height - 20,
            width: 50,
            height: 20
          };
        output(
          "Add a new area: " +
            areaToString(areaOption1) +
            " and " +
            areaToString(areaOption2)
        );
        $("img#example").selectAreas("add", [areaOption1, areaOption2]);
      });
    });

    function areaToString(area) {
      console.log(`x: ${area.x}`);
      console.log(`y: ${area.y}`);
      console.log(`width: ${area.width}`);
      console.log(`height: ${area.height}`);

      return (
        (typeof area.id === "undefined" ? "" : area.id + ": ") +
        area.x +
        ":" +
        area.y +
        " " +
        area.width +
        "x" +
        area.height +
        "<br />"
      );
    }

    function output(text) {
      $("#output").html(text);
    }

    // Log the quantity of selections
    function debugQtyAreas(event, id, areas) {
      console.log(areas.length + ": areas", arguments);
      console.log("argument: " + arguments.event);
    }

    // Display areas coordinates in a div
    function displayAreas(areas) {
      var text = "";
      $.each(areas, function(id, area) {
        text += areaToString(area);
      });
      output(text);
    }
  }

  render() {
    let imagePreviewUrl = this.props.setImagePreivewUrl;

    return (
      <div>
        <img
          src={imagePreviewUrl}
          alt="logo"
          id="example"
          style={{ width: 400, height: 400, margin: "10px" }}
        />
        <table>
          <tbody>
            <tr>
              <td className="actions">
                <input
                  type="button"
                  id="btnView"
                  value="Display areas"
                  className="actionOn"
                />
                <input
                  type="button"
                  id="btnViewRel"
                  value="Display relative"
                  className="actionOn"
                />
                <input
                  type="button"
                  id="btnNew"
                  value="Add New"
                  className="actionOn"
                />
                <input
                  type="button"
                  id="btnNews"
                  value="Add 2 New"
                  className="actionOn"
                />
                <input
                  type="button"
                  id="btnReset"
                  value="Reset"
                  className="actionOn"
                />
                <input
                  type="button"
                  id="btnDestroy"
                  value="Destroy"
                  className="actionOn"
                />
                <input
                  type="button"
                  id="btnCreate"
                  value="Create"
                  className="actionOff"
                />
              </td>
              <td>
                <div id="output" className="output">
                  {" "}
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    );
  }
}
