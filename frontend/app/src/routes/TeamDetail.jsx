export default function TeamDetail() {
  const team = {
    name: "Bobcat CS",
    project_brief: "Web application using React and FastAPI",
    technology_platform_description: "Python, JavaScript",
    members: [
      {
        first_name: "A",
        last_name: "a",
        username: "aa",
        github_username: "aa",
      },
      {
        first_name: "B",
        last_name: "b",
        username: "bb",
        github_username: "bb",
      },
      {
        first_name: "C",
        last_name: "c",
        username: "cc",
        github_username: "cc",
      },
      {
        first_name: "D",
        last_name: "d",
        username: "dd",
        github_username: "d",
      },
    ],
  };

  return (
    <div id="team">
      <section id="team-info">
        <h1>{team.name}</h1>
      </section>
      <section id="members-list">
        <h3>Members</h3>
        <p>{team.project_brief}</p>
        <p>{team.technology_platform_description}</p>
        <ul>
          {team.members &&
            team.members.map((student, index) => (
              <li key={index}>
                <a href={`/student/${student.id}`}>
                  {student.first_name} {student.last_name}
                </a>
              </li>
            ))}
        </ul>
      </section>
    </div>
  );
}
