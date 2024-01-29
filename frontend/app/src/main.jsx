import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { ProtectedRoute } from "./components/ProtectedRoute.jsx";
import ErrorPage from "./ErrorPage.jsx";
import ClassroomCreate, {
  action as createClassroomAction,
} from "./routes/ClassroomCreate.jsx";
import ClassroomDetail, {
  loader as classroomLoader,
  action as updateClassroomAction,
} from "./routes/ClassroomDetail.jsx";
import ClassroomList, {
  loader as classroomsLoader,
} from "./routes/ClassroomList.jsx";
import ImportStudentsFromBlackboard, {
  action as importAction,
} from "./routes/ImportStudentsFromBlackboard.jsx";
import LoginPage, { action as loginAction } from "./routes/LoginPage.jsx";
import MilestoneDetail from "./routes/MilestoneDetail.jsx";
import StudentList, {
  loader as studentListLoader,
} from "./routes/StudentList.jsx";
import TeamDetail from "./routes/TeamDetail.jsx";
import axios from "axios";

axios.interceptors.request.use(function (config) {
  if (!config.url.endsWith("/token")) {
    const accessToken = JSON.parse(window.localStorage.getItem("access_token"));
    if (!accessToken) {
      throw { response: { status: 401 } };
    }

    config.headers[
      "Authorization"
    ] = `${accessToken["token_type"]} ${accessToken["access_token"]}`;
  }
  return config;
});

const router = createBrowserRouter([
  {
    path: "/hello-world",
    element: <div>Hello world!</div>,
  },
  {
    path: "/",
    loader: classroomsLoader,
    element: (
      <ProtectedRoute>
        <ClassroomList />
      </ProtectedRoute>
    ),
    errorElement: <ErrorPage />,
  },
  {
    path: "/login",
    action: loginAction,
    element: <LoginPage></LoginPage>,
    errorElement: <ErrorPage />,
  },
  {
    path: "/classrooms/new",
    action: createClassroomAction,
    element: (
      <ProtectedRoute>
        <ClassroomCreate />
      </ProtectedRoute>
    ),
  },
  {
    path: "/classrooms/:classroomId",
    loader: classroomLoader,
    action: updateClassroomAction,
    element: (
      <ProtectedRoute>
        <ClassroomDetail />
      </ProtectedRoute>
    ),
    errorElement: <ErrorPage />,
  },
  {
    path: "/classrooms/:classroomId/import/students-from-bb",
    loader: classroomLoader,
    action: importAction,
    element: (
      <ProtectedRoute>
        <ImportStudentsFromBlackboard />
      </ProtectedRoute>
    ),
  },
  {
    path: "/classrooms/:classroomId/milestones/",
    element: <div>Full list of milestones + tool to edit + tool to delete</div>,
  },
  {
    path: "/classrooms/:classroomId/milestones/new",
    element: <div>New milestone page</div>,
  },
  {
    path: "/classrooms/:classroomId/milestones/:milestoneId",
    element: <MilestoneDetail />,
  },
  {
    path: "/classrooms/:classroomId/milestones/:milestoneId/productivity",
    element: <div>Commit frequency page + filter: all-team, fuzzy-search</div>,
  },
  {
    path: "/classrooms/:classroomId/teams/",
    element: <div>Full list of team + tool to edit + tool to delete</div>,
  },
  {
    path: "/classrooms/:classroomId/teams/new",
    element: <div>New team page</div>,
  },
  {
    path: "/classrooms/:classroomId/teams/:teamId",
    element: <TeamDetail />,
  },
  {
    path: "/classrooms/:classroomId/students",
    element: <StudentList />,
    loader: studentListLoader,
    errorElement: <ErrorPage />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
