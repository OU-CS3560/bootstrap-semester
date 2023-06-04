import { Link, useLoaderData } from "react-router-dom";

import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";

function PresentationControl() {
  return (
    <div>
      <h2>#1 cpp-web-app (presented)</h2>
      <p>Should be draggable?</p>
      <ul>
        <li>
          <s>
            Student A (strikethrough indicate student is marked as presented;
            tap to toggle this state?)
          </s>
        </li>
        <li>
          Student B (not strikethrough indicate student is marked as NOT
          presented; tap to toggle this state?)
        </li>
        <li>
          Student C (not strikethrough indicate student is marked as NOT
          presented; tap to toggle this state?)
        </li>
      </ul>
    </div>
  );
}

export default function MilestoneDetail() {
  return (
    <Container fluid>
      <Row>
        <Col>
          <h1>Milestone #1 - NAME</h1>
          <p>Presented: 10 teams (out of 13 teams)</p>
        </Col>
      </Row>
      <Row>
        <Col>
          <h1>Presentations</h1>
          <Button variant="outline-primary" disabled>
            Create Presentation Order (NOTE: should be hidden since the order
            already created)
          </Button>
          <ul>
            <li>{PresentationControl()}</li>
          </ul>
        </Col>
      </Row>
    </Container>
  );
}
