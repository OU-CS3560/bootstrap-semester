import { useState, useEffect } from "react";
import axios from "axios";

import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const baseURL = import.meta.env.VITE_API_BASE_URL;

export default function ClassroomList() {
  const [classrooms, setClassrooms] = useState(null);

  useEffect(() => {
    axios.get(`${baseURL}/classrooms/`).then((response) => {
      setClassrooms(response.data);
    });
  }, []);

  if (!classrooms) return null;

  const classroomElements = classrooms.map((classroom, idx) => (
    <Row key={idx}>
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
  ));

  return <Container fluid>{classroomElements}</Container>;
}
