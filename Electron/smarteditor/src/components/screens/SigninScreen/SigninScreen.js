import React, { Component } from "react";

export default class SigninScreen extends Component {
  render() {
    return (
      <div className="signup-flow">
        <div className="signup-wrapper ">
          <div className="signup-wrapper-container">
            {/* top logo */}
            <a className="logo-link">
              <img className="SE-logo">{/* logo */}</img>
            </a>
            {/* form */}
            <form>
              {/* <div id="host-port" class="form-group form-group-separator">
                <div class="form-item">
                  <label>
                    <span class="form-item-label">Name</span>
                  </label>
                  <input
                    type="text"
                    name="Name"
                    value=""
                    class="form-control"
                  />
                </div>
                <div class="form-item">
                  <label>
                    <span class="form-item-label">Email</span>
                  </label>
                  <input
                    type="email"
                    name="email"
                    value=""
                    class="form-control"
                  />
                </div>
                <div class="form-item">
                  <label>
                    <span class="form-item-label">Password</span>
                  </label>
                  <input
                    type="password"
                    name="password"
                    value=""
                    class="form-control"
                  />
                </div>
              </div> */}
            </form>
            {/* submit */}
          </div>
        </div>
        <div className="signup-graphics-pane">{/* add graphics here */}</div>
      </div>
    );
  }
}
