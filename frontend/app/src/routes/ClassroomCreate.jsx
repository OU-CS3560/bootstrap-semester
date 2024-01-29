import { Form as RouterForm, redirect, useActionData } from "react-router-dom";

import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Row from "react-bootstrap/Row";

import { createClassroom } from "../api/classrooms";
import TopBar from "../components/TopBar";

export async function action({ request, params }) {
  try {
    console.log("[ClassroomCreate.action]: creating a classroom");
    const formData = await request.formData();
    const payload = Object.fromEntries(formData);
    const { status, data } = await createClassroom(payload);

    if (status === "success") {
      return redirect(`/classrooms/${data.id}`);
    } else if (status === "error") {
      return data;
    }
  } catch (error) {
    if (error.response && error.response.status === 401) {
      return redirect("/login");
    } else {
      throw error;
    }
  }
}

export default function ClassroomCreate() {
  const errors = useActionData() || {};
  if (errors) {
    console.log(errors);
  }
  return (
    <>
      <TopBar />
      <Container>
        <Row>
          <Col>
            <h1>New Classroom</h1>
            <Form as={RouterForm} method="post" id="create-classroom-form">
              <Form.Group className="mb-3" controlId="name">
                <Form.Label>Name</Form.Label>
                <Form.Control
                  name="name"
                  type="text"
                  isInvalid={!!errors.name}
                />
                <Form.Control.Feedback type="invalid">
                  {errors.name}
                </Form.Control.Feedback>
              </Form.Group>
              <Form.Group className="mb-3" controlId="begin-date">
                <Form.Label>Begin Date</Form.Label>
                <Form.Control
                  name="begin_date"
                  type="date"
                  isInvalid={!!errors.begin_date}
                />
                <Form.Control.Feedback type="invalid">
                  {errors.begin_date}
                </Form.Control.Feedback>
              </Form.Group>
              <Form.Group className="mb-3" controlId="end-date">
                <Form.Label>End Date</Form.Label>
                <Form.Control
                  name="end_date"
                  type="date"
                  isInvalid={!!errors.end_date}
                />
                <Form.Control.Feedback type="invalid">
                  {errors.end_date}
                </Form.Control.Feedback>
              </Form.Group>
              <Form.Group className="mb-3" controlId="github-classroom-link">
                <Form.Label>GitHub Classroom Link</Form.Label>
                <Form.Control
                  name="github_classroom_link"
                  type="text"
                  isInvalid={!!errors.github_classroom_link}
                />
                <Form.Control.Feedback type="invalid">
                  {errors.github_classroom_link}
                </Form.Control.Feedback>
              </Form.Group>
              <Button varient="primary" type="submit">
                Create
              </Button>
            </Form>
          </Col>
        </Row>
      </Container>
    </>
  );
}
