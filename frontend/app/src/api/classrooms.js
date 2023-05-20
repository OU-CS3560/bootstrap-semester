import axios from "axios";

const apiBaseURL = import.meta.env.VITE_API_BASE_URL;

export async function getClassrooms() {
  try {
    const response = await axios.get(`${apiBaseURL}/classrooms/`);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

export async function getClassroom(id) {
  console.log(id);
  try {
    const response = await axios.get(`${apiBaseURL}/classrooms/${id}`);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}
