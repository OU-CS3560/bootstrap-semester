import axios from "axios";

const apiBaseURL = import.meta.env.VITE_API_BASE_URL;

export async function createClassroom(data) {
  try {
    const response = await axios.post(`${apiBaseURL}/classrooms/`, data);

    return {
      status: "success",
      data: response.data,
    };
  } catch (error) {
    // Convert openapi format to form validation format.
    if (error.response && error.response.status === 422) {
      let errors = {};
      error.response.data.detail.map((e, i) => {
        errors[e.loc[1]] = e.msg;
      });
      return {
        status: "error",
        data: errors,
      };
    }
  }
}

export async function getClassrooms() {
  // Error is handled by the Route.
  const response = await axios.get(`${apiBaseURL}/classrooms/`);
  return response.data;
}

export async function getClassroom(id) {
  try {
    const response = await axios.get(`${apiBaseURL}/classrooms/${id}`);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

export async function deleteClassroom(id) {
  const response = await axios.delete(`${apiBaseURL}/classrooms/${id}`);
  return response.data;
}

export async function updateClassroom(id, classroom) {
  try {
    const response = await axios.patch(
      `${apiBaseURL}/classrooms/${id}`,
      classroom,
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    return {
      status: "success",
      data: response.data,
    };
  } catch (error) {
    console.log(error);

    if (error.code === "ERR_NETWORK") {
      throw error;
    } else if (error.response && error.response.status === 422) {
      // Convert openapi format to form validation format.
      let errors = {};
      error.response.data.detail.map((e, i) => {
        errors[e.loc[1]] = e.msg;
      });
      return {
        status: "error",
        data: errors,
      };
    }
  }
}

export async function importStudentsFromBlackboard(
  classroomId,
  membershipResults
) {
  try {
    const response = await axios.post(
      `${apiBaseURL}/classrooms/${classroomId}/import/students-from-bb`,
      membershipResults,
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    return response.data;
  } catch (error) {
    console.log(error);
  }
}
