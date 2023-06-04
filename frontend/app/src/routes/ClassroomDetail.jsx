import { Link, useLoaderData } from "react-router-dom";

import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import Badge from "react-bootstrap/Badge";

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
          <Button variant="outline-primary">Edit</Button>
        </Col>
      </Row>
      <Row>
        <Col xs={12} md={6}>
          <h3>
            Teams{" "}
            <small>
              <Badge bg="secondary">13</Badge>
            </small>
          </h3>
          <Link to={`teams/new`}>
            <Button variant="outline-primary">New Team</Button>
          </Link>
          <Link to={`teams`}>
            <Button variant="outline-primary">View All</Button>
          </Link>
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
          <h3>
            Milestones{" "}
            <small>
              <Badge bg="secondary">0</Badge>
            </small>
          </h3>
          <Link to={`milestones/new`}>
            <Button variant="outline-primary">New Milestone</Button>
          </Link>
          <Link to={`milestones`}>
            <Button variant="outline-primary">View All</Button>
          </Link>
          <ul>
            <li>
              Maybe only show the active milestone? (or with up-coming as well)
            </li>
          </ul>
        </Col>
      </Row>
      <Row>
        <Col xs={12}>
          <h3>
            Students{" "}
            <small>
              <Badge bg="secondary">50</Badge>
            </small>
          </h3>
          <Button variant="outline-primary">Add a Student</Button>
          <Link to={`import/students-from-bb`}>
            <Button variant="outline-primary">
              Import Student List from Blackboard
            </Button>
          </Link>
          <Link to={`students`}>
            <Button variant="outline-primary">View All</Button>
          </Link>
          <ul>
            <li>A small list of students (10 or so)</li>
          </ul>
        </Col>
      </Row>
    </Container>
  );
}
