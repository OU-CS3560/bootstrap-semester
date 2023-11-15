import { Fragment, useState } from "react";
import { Form as RouterForm, redirect, useLoaderData } from "react-router-dom";

import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";

import { importStudentsFromBlackboard } from "../api/classrooms.js";

const blackboardApiBaseUrl = "https://blackboard.ohio.edu";

function parseUrlForCourseId(url) {
  const tokens = url.split("/");
  const idx = tokens.findIndex((e) => e === "courses");
  if (idx !== -1 && idx + 1 < tokens.length) {
    const courseId = tokens[idx + 1];
    if (courseId.startsWith("_")) {
      return courseId;
    }
    return "";
  } else {
    return "";
  }
}

export async function action({ request, params }) {
  console.log("action got called");
  const formData = await request.formData();
  console.log("formData is");
  console.log(formData);
  const updates = Object.fromEntries(formData);
  console.log(updates);

  // const obj = JSON.parse();

  await importStudentsFromBlackboard(
    params.classroomId,
    updates.membership_results
  );

  return redirect(`/classrooms/${params.classroomId}`);
}

export default function ImportStudentsFromBlackboard() {
  const { classroom } = useLoaderData();
  const [courseInput, setCourseInput] = useState("");
  const [membershipUrl, setMembershipUrl] = useState("");
  const [hasValidCourseId, setHasValidCourseId] = useState(false);

  let response;
  if (hasValidCourseId) {
    response = (
      <Fragment>
        <Row>
          <Col xs={3}>
            <p>
              Please visit:{" "}
              <a href={membershipUrl} target="_blank" rel="noreferrer">
                {membershipUrl}
              </a>{" "}
              and copy the content ino the following text box
            </p>
          </Col>
        </Row>
        <Row>
          <Col>
            <Form as={RouterForm} method="post" id="import-students-list-form">
              <textarea name="membership_results"></textarea>
              <Button variant="outline-primary" type="submit">
                Import
              </Button>
            </Form>
          </Col>
        </Row>
      </Fragment>
    );
  } else {
    response = (
      <Row>
        <Col xs={3}>
          <p>Please enter a valid Course ID or a valid URL for the Course</p>
        </Col>
      </Row>
    );
  }

  return (
    <Container fluid>
      <Row>
        <Col>
          <h1>Importing into {classroom.name}</h1>
          <label htmlFor="classroom-id-or-url-txt">Course ID (or a URL)</label>
          <input
            name="classroom-id-or-url-txt"
            type="text"
            value={courseInput}
            onChange={(e) => {
              const value = e.target.value;
              setCourseInput(value);

              if (value.startsWith("http")) {
                const courseId = parseUrlForCourseId(value);
                if (courseId !== "") {
                  setMembershipUrl(
                    `${blackboardApiBaseUrl}/learn/api/public/v1/courses/${courseId}/users?fields=id,userId,user,courseRoleId`
                  );
                  setHasValidCourseId(true);
                } else {
                  // invalid URL?
                  setHasValidCourseId(false);
                }
              } else if (value.startsWith("_")) {
                setMembershipUrl(
                  `${blackboardApiBaseUrl}/learn/api/public/v1/courses/${value}/users?fields=id,userId,user,courseRoleId`
                );
              } else {
                // invalid course id?
                setHasValidCourseId(false);
              }
            }}
          ></input>
        </Col>
      </Row>
      {response}
    </Container>
  );
}
