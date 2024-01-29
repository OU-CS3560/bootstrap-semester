import axios from "axios";

const apiBaseURL = import.meta.env.VITE_API_BASE_URL;

export async function login(data) {
  try {
    const response = await axios.post(`${apiBaseURL}/token`, data, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });

    return {
      status: "success",
      data: response.data,
    };
  } catch (error) {
    console.log(error);

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
