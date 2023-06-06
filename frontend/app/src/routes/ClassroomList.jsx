import { Link, useLoaderData } from "react-router-dom";

import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";

import TopBar from "../components/TopBar";

export default function ClassroomList() {
  const { classrooms } = useLoaderData();

  const classroomElements = classrooms.map((classroom, idx) => (
    <Row key={idx}>
      <Col>
        <h3>
          <Link to={`${classroom.id}`}>{classroom.name}</Link>
        </h3>
        <p>
          Begin: {new Date(classroom.begin_date).toDateString()}
        </p>
        <p>
          End: {new Date(classroom.end_date).toDateString()}
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
  ));

  return (<>
    <TopBar />
    <Container>
      <Row>
        <Col>
          <h1>Classrooms</h1>
          <Link to={`new`}>
            <Button variant="outline-primary">New Classroom</Button>
          </Link>
        </Col>
      </Row>
      {classroomElements}
    </Container>
  </>);
}
