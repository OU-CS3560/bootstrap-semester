import { Navigate } from "react-router-dom";
import { useLocalStorage } from "../hooks/useLocalStorage";

export const ProtectedRoute = ({ children }) => {
  const [storedValue, setValue] = useLocalStorage("access_token", null);
  console.log(storedValue);
  if (!storedValue) {
    return <Navigate to="/login" />;
  }
  return children;
};
