import styled from "styled-components";
import Color from "../utils/Color";

export default styled.button`
  font-size: 14px;
  padding: 5px 18px;
  background: ${Color.button.BACKGROUND_COLOR};
  color: #2c2d30 !important;
  font-weight: 700;
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
  user-select: none;
  text-decoration: none;
  cursor: pointer;
  margin: 12px;
`;
