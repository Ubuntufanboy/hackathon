import './App.css'
import "@fontsource/roboto";
import 'material-icons/iconfont/material-icons.css';
import {Navbar,Nav,NavLink,Row,Col,Container, Card} from 'react-bootstrap';
import {Component} from 'react';
import Webcam from 'react-webcam';
import { MDBAccordion, MDBAccordionItem, MDBContainer } from "mdb-react-ui-kit";


function NavBar(){
  return (
    <Navbar fixed='top' className="justify-content-center">
      <Nav>
          <Nav.Link className="navlink" href="#gen" style={{color:'white'}}>Generator</Nav.Link>
          <Nav.Link className="navlink" href="#faq" style={{color:'white'}}>FAQ</Nav.Link>
      </Nav>
    </Navbar>
  );
}

function FrontPage(){
  return (
    <div>
      <Row style={{height: "50px", backgroundColor:"black"}}/>
      <Row className="frontpagerow">
        <h1 className="fronth1" style={{}}>
          COMMUNICATE
        </h1>
      </Row>
      <Row className="frontpagerow" style={{}}>
      <h1 className="fronth1">
            WITH YOUR
        </h1>
      </Row>
    <Row className="frontpagerow" style={{}}>
    <h1 className="fronth1">
            FINGERTIPS
    </h1>
    {/* Creating some blackspace  */}

      </Row>
      <Row style={{height: "100px", backgroundColor:"black"}} />
      <Row style={{height: "100px", backgroundColor:"black"}} />

    </div>
  );
}

function FirstInfo(){
  return (
    <div>
    <Container fluid>
        <Row>
        <Col className="firstinfocol" style={{height: "350px", backgroundColor:"black", color:"white"}}>
            Hi
        </Col>
        <Col className="firstinfocol">
            PIC
        </Col>
      </Row>
    </Container>
    </div>
  );
}

function SecondInfo(){
  return(
    <div>
    <Container fluid>
      <Row>
          <Col className="firstinfocol" style={{height: "350px", backgroundColor:"white", color:"black"}}>
              Hi
          </Col>
          <Col className="firstinfocol" style={{height: "350px", backgroundColor:"black", color:"white"}}>
              PIC
          </Col>
      </Row>
      </Container>
    </div>
  );
}
function GeneratorInfo(){
  return(
  <div>
    <Container fluid id="gen">
      <Row style={{borderColor: 'black', border: '1px solid black'}}>
        <Col className="thirdinfocol">
          <h1 style={{padding: "10px"}}>
            Instructions
          </h1>
          <br />
          <h3>
            <ol>
              <li> Enable Webcam Extension </li>
              <br />
              <li> Click on Start Recording Button</li>
              <br />
              <li> Perform ASL and click Stop Recording Button</li>
              <br />
              <li> Wait for Results Down Below </li>
              <br />
            </ol>
            <br />
            And.. SHAZAM! IT'S THAT EASY!
          </h3>
        </Col>
        <Col>
          <h1 style={{padding:"10px"}}>
            Webcam
          </h1>
          <Webcam style={{width:"500px", height: "500px"}}/>
        </Col>
      </Row>
    </Container>
  </div>
  );
}

function FaQInfo(){
  return (
    <div>
      <Container fluid style={{borderColor: 'black', border: '1px solid black'}}>
        <Row className="justify-content-center">
          <h1>
            FaQ
          </h1>
        </Row>
        <Row>
          <Col style={{padding: "15px"}}>
            <Card style={{height : "100px"}}>
              <Card.Title> QUESTION 1</Card.Title>
              <Card.Body> ANSWER 1 </Card.Body>
            </Card>
          </Col>

          <Col style={{padding: "15px"}}>
            <Card style={{height : "100px"}}>
              <Card.Title> QUESTION 2</Card.Title>
              <Card.Body> ANSWER 2 </Card.Body>
            </Card>
          </Col>
          <Col style={{padding: "15px"}}>
            <Card style={{height : "100px"}}>
              <Card.Title> QUESTION 2</Card.Title>
              <Card.Body> ANSWER 2 </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

function ContactInfo(){
  return (
    <div> 
      <Container fluid style={{backgroundColor: "black", borderColor: 'black', border: '1px solid black'}}>
        <Row className="justify-content-center" style={{}}>
          <h1 style={{color: 'white'}}>
            Contact Us
          </h1>
          <br />
        </Row>
        <Row className="justify-content-center">
            <a href="https://github.com"><span class='material-icons' href="https://github.com" style={{color: 'orange', width:'px', height: '100px',padding: '10px', marginLeft: '10px'}}>github</span></a>
            <a href="https://devpost.com"><span class='material-icons' href="https://github.com" style={{color: 'orange', width:' 100px', height: '100px',padding: '10px',  marginLeft: '10px' }}>Devpost</span></a>
        </Row>
      </Container>
    </div>
  );
}

export default function App() {

  return (
    <div className="App">
      <NavBar />
      <FrontPage />
      <FirstInfo />
      <SecondInfo />
      <GeneratorInfo />
      <FaQInfo />
      <ContactInfo />
    </div>
  );

}