import { Link, useLoaderData } from "react-router-dom";

import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";

import { getClassroom } from "../api/classrooms";
import { getStudents } from "../api/students";
import TopBar from "../components/TopBar";

export async function loader({ params }) {
  const classroom = await getClassroom(params.classroomId);
  const students = await getStudents(params.classroomId);
  return { classroom: classroom, students: students };
}

export default function StudentList() {
  const { classroom, students } = useLoaderData();

  const studentElements = students.map((student, idx) => (
    <p key={idx}>
      {student.first_name} {student.last_name}
    </p>
  ));

  return (
    <>
      <TopBar />
      <Container>
        <Row>
          <Col>
            <h1>
              <Link to={`/classrooms/${classroom.id}`}>{classroom.name}</Link>{" "}
              -&nbgt; Student List
            </h1>
          </Col>
        </Row>
        {studentElements}
      </Container>
    </>
  );
}
