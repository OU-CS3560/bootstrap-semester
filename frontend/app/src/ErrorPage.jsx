import { useRouteError } from "react-router-dom";

function ApiRelatedError({ error }) {
  return (
    <div id="error-page">
      <h1>Oops!</h1>
      <p>Cannot reach the API endpoint.</p>
      <p>
        <i>{error.statusText || error.message}</i>
      </p>
    </div>
  );
}

export default function ErrorPage() {
  const error = useRouteError();

  if (error.name === "AxiosError") {
    return <ApiRelatedError error={error} />;
  } else {
    console.log(error);
    return (
      <div id="error-page">
        <h1>Oops!</h1>
        <p>Sorry, an unexpected error has occurred.</p>
        <p>
          <i>{error.statusText || error.message}</i>
        </p>
      </div>
    );
  }
}
