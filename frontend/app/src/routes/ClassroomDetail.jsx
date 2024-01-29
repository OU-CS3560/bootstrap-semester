import { Link, redirect, useLoaderData } from "react-router-dom";

import Badge from "react-bootstrap/Badge";
import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";

import {
  deleteClassroom,
  getClassroom,
  updateClassroom,
} from "../api/classrooms";
import ClassroomBasicInfoPanel from "../components/ClassroomBasicInfoPanel";
import TopBar from "../components/TopBar";

export async function loader({ params }) {
  try {
    const classroom = await getClassroom(params.classroomId);
    return { classroom };
  } catch (error) {
    if (error.response && error.response.status === 401) {
      return redirect("/login");
    } else {
      throw error;
    }
  }
}

// This action is used in <ClassroomBasicInfoPanel />
export async function action({ request, params }) {
  switch (request.method) {
    case "PATCH": {
      const formData = await request.formData();
      const payload = Object.fromEntries(formData);
      const result = await updateClassroom(params.classroomId, payload);
      return result;
    }
    case "DELETE": {
      await deleteClassroom(params.classroomId);
      return redirect("/");
    }
    default: {
      throw new Response("", { status: 405 });
    }
  }
}

export default function ClassroomDetail() {
  const { classroom } = useLoaderData();

  return (
    <>
      <TopBar />
      <Container>
        <ClassroomBasicInfoPanel classroom={classroom} />
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
                Maybe only show the active milestone? (or with up-coming as
                well)
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
    </>
  );
}
