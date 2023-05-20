import { Link, useLoaderData } from "react-router-dom";

import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

export default function ClassroomList() {
  const { classrooms } = useLoaderData();

  const classroomElements = classrooms.map((classroom, idx) => (
    <Row key={idx}>
      <Col>
        <h1>
          <Link to={`${classroom.id}`}>{classroom.name}</Link>
        </h1>
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
  ));

  return <Container fluid>{classroomElements}</Container>;
}
