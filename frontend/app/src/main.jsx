import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import App from "./App.jsx";
import ClassroomDetail from "./routes/ClassroomDetail.jsx";
import ClassroomList from "./routes/ClassroomList.jsx";
import TeamDetail from "./routes/TeamDetail.jsx";
import ErrorPage from "./ErrorPage.jsx";

import { getClassrooms, getClassroom } from "./api/classrooms.js";

async function classroomsLoader() {
  const classrooms = await getClassrooms();
  return { classrooms };
}

async function classroomLoader({ params }) {
  console.log(params);
  const classroom = await getClassroom(params.classroomId);
  return { classroom };
}

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage />,
  },
  {
    path: "/hello-world",
    element: <div>Hello world!</div>,
  },
  {
    path: "/classrooms/",
    loader: classroomsLoader,
    element: <ClassroomList />,
  },
  {
    path: "/classrooms/:classroomId",
    loader: classroomLoader,
    element: <ClassroomDetail />,
  },
  {
    path: "/teams/:teamId",
    element: <TeamDetail />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
