import { useState } from "react";
import { Link, useLoaderData } from "react-router-dom";

import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";

export default function ImportStudentsFromBlackboard() {
  const { classroom } = useLoaderData();

  return (
    <Container fluid>
      <Row>
        <Col>
          <h1>Importing into {classroom.name}</h1>
          <label htmlFor="classroom-id-or-url-txt">Course ID (or a URL)</label>
          <input name="classroom-id-or-url-txt" type="text"></input>
        </Col>
      </Row>
      <Row>
        <Col xs={3}>
          <p>
            Please visit: (LINK) and copy the content ino the following text box
          </p>
          <textarea></textarea>
        </Col>
      </Row>
      <Row>
        <Col>
          <Button variant="outline-primary">Import</Button>
        </Col>
      </Row>
    </Container>
  );
}
