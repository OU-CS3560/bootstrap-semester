import { Link, useLoaderData, redirect } from "react-router-dom";

import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";

import TopBar from "../components/TopBar";
import { getClassrooms } from "../api/classrooms";

export async function loader() {
  try {
    const classrooms = await getClassrooms();
    return { classrooms };
  } catch (error) {
    if (error.response && error.response.status === 401) {
      return redirect("/login");
    } else {
      throw error;
    }
  }
}

function ClassroomCard({ classroom }) {
  return (
    <Row>
      <Col>
        <h3>
          <Link to={`classrooms/${classroom.id}`}>{classroom.name}</Link>
        </h3>
        <p>Begin: {new Date(classroom.begin_date).toDateString()}</p>
        <p>End: {new Date(classroom.end_date).toDateString()}</p>
        <a
          href={classroom.github_classroom_link}
          target="_blank"
          rel="noreferrer"
        >
          GitHub Classroom
        </a>
      </Col>
    </Row>
  );
}

export default function ClassroomList() {
  const { classrooms } = useLoaderData();

  const classroomElements = classrooms.map((classroom, idx) => (
    <ClassroomCard key={idx} classroom={classroom}></ClassroomCard>
  ));

  return (
    <>
      <TopBar />
      <Container>
        <Row>
          <Col>
            <h1>Classrooms</h1>
            <Link to={`classrooms/new`}>
              <Button variant="outline-primary">New Classroom</Button>
            </Link>
          </Col>
        </Row>
        {classroomElements}
      </Container>
    </>
  );
}
