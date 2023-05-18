import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

export default function Classroom() {
  const classroom = {
    name: "cs3560 (s22-23)",
    begin_date: new Date(2023, 1, 1),
    end_date: new Date(2023, 5, 5),
    github_classroom_link:
      "https://classroom.github.com/classrooms/60114289-ou-cs3560-spring-2022-2023",
    teams: [
      {
        id: 1,
        name: "Bobcat CS",
        project_brief: "Web application using React and FastAPI",
        technology_platform_description: "Python, JavaScript",
        members: [
          {
            id: 1,
            first_name: "A",
            last_name: "a",
            username: "aa",
            github_username: "aa",
          },
          {
            id: 2,
            first_name: "B",
            last_name: "b",
            username: "bb",
            github_username: "bb",
          },
          {
            id: 3,
            first_name: "C",
            last_name: "c",
            username: "cc",
            github_username: "cc",
          },
          {
            id: 4,
            first_name: "D",
            last_name: "d",
            username: "dd",
            github_username: "d",
          },
        ],
      },
    ],
    milestones: [],
    students: [],
  };

  return (
    <Container fluid>
      <Row>
        <Col>
          <h1>{classroom.name}</h1>
          <p>
            Begin: {classroom.begin_date.toDateString()} End:{" "}
            {classroom.end_date.toDateString()}
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
        <Col xs={12} md={6}>
          <h3>Teams</h3>
          <ul>
            {classroom.teams &&
              classroom.teams.map((team, index) => (
                <li key={index}>
                  <a href={`/team/${team.id}`}>{team.name}</a>
                </li>
              ))}
          </ul>
        </Col>
        <Col xs={12} md={6}>
          <h3>Milestones (Checkpoints)</h3>
          <ul></ul>
        </Col>
      </Row>
      <Row>
        <Col xs={12}>
          <h3>Students</h3>
          <ul></ul>
        </Col>
      </Row>
    </Container>
  );
}
