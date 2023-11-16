import axios from "axios";

const apiBaseURL = import.meta.env.VITE_API_BASE_URL;

export async function getStudents(classroom_id) {
  const response = await axios.get(`${apiBaseURL}/classrooms/${classroom_id}/students`);
  return response.data;
}