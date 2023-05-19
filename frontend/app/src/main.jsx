import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import App from "./App.jsx";
import Classroom from "./routes/Classroom.jsx";
import ClassroomList from "./routes/ClassroomList.jsx";
import Team from "./routes/Team.jsx";
import ErrorPage from "./ErrorPage.jsx";

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
    element: <ClassroomList />,
  },
  {
    path: "/classrooms/:classromId",
    element: <Classroom />,
  },
  {
    path: "/teams/:teamId",
    element: <Team />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
