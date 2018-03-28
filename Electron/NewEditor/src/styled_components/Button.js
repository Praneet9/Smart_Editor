import styled from "styled-components";
import Color from "../utils/Color";

export default styled.button`
  padding: 5px 18px;
  background: ${Color.button.BACKGROUND_COLOR};
  text-shadow: none;
  border: none;
  border-radius: 0.25rem;
  box-shadow: none;
  position: relative;
  display: inline-block;
  vertical-align: bottom;
  text-align: center;
  white-space: nowrap;
  margin: 0;
  color: #2c2d30 !important;
  font-size: 14px;
  font-weight: 700;
  user-select: none;
  text-decoration: none;
  cursor: pointer;
  margin: 12px;
  outline: none;
`;
