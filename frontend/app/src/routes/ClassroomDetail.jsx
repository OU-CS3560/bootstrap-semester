import { Link, useLoaderData } from "react-router-dom";

import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";

export default function ClassroomDetail() {
  const { classroom } = useLoaderData();

  return (
    <Container fluid>
      <Row>
        <Col>
          <h1>{classroom.name}</h1>
          <p>
            Begin: {new Date(classroom.begin_date).toDateString()} End:{" "}
            {new Date(classroom.end_date).toDateString()}
          </p>
          <a
            href={classroom.github_classroom_link}
            target="_blank"
            rel="noreferrer"
          >
            GitHub Classroom
          </a>
        </Col>
      </Row>
      <Row>
        <Col xs={3}>
          <Button variant="outline-primary">
            Import Student List from Blackboard
          </Button>
        </Col>
      </Row>
      <Row>
        <Col xs={12} md={6}>
          <h3>Teams</h3>
          <ul>
            {classroom.teams &&
              classroom.teams.map((team, index) => (
                <li key={index}>
                  <a href={`/teams/${team.id}`}>{team.name}</a>
                </li>
              ))}
          </ul>
        </Col>
        <Col xs={12} md={6}>
          <h3>Milestones (Checkpoints)</h3>
          <ul></ul>
        </Col>
      </Row>
      <Row>
        <Col xs={12}>
          <h3>Students</h3>
          <ul></ul>
        </Col>
      </Row>
    </Container>
  );
}
