import { Form as RouterForm, redirect, useActionData } from "react-router-dom";

import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Row from "react-bootstrap/Row";

import { login as apiLogin } from "../api/auth";
import TopBar from "../components/TopBar";
import { useAuth } from "../hooks/useAuth";

export async function action({ request, params }) {
  console.log("loging the user in");
  const formData = await request.formData();
  const payload = Object.fromEntries(formData);
  const { status, data } = await apiLogin(payload);

  if (status === "success") {
    window.localStorage.setItem("access_token", JSON.stringify(data));
    return redirect("/");
  } else if (status === "error") {
    return data;
  }
}

export default function LoginPage() {
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
            <h1>Login</h1>
            <Form as={RouterForm} method="post" id="login-form">
              <Form.Group className="mb-3" controlId="username">
                <Form.Label>Username</Form.Label>
                <Form.Control
                  name="username"
                  type="text"
                  isInvalid={!!errors.username}
                />
                <Form.Control.Feedback type="invalid">
                  {errors.username}
                </Form.Control.Feedback>
              </Form.Group>
              <Form.Group className="mb-3" controlId="pasword">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  name="password"
                  type="password"
                  isInvalid={!!errors.password}
                />
                <Form.Control.Feedback type="invalid">
                  {errors.password}
                </Form.Control.Feedback>
              </Form.Group>
              <Button varient="primary" type="submit">
                Login
              </Button>
            </Form>
          </Col>
        </Row>
      </Container>
    </>
  );
}
