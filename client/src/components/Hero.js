import styled from "styled-components";
const Hero = styled.header`
  margin-top: 67px;
  min-height: calc(100vh - 67px);
  background: url('http://127.0.0.1:8000/media/hero.jpg');
  background-size: cover;
  background-position: 50% 15%;
  display: flex;
  align-items: center;
  justify-content: center;
`;

export default Hero;