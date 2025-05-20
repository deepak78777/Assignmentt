import React from "react";
import Signup from "./components/Signup";
import Login from "./components/Login";

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-100 to-blue-100 flex flex-col items-center justify-center p-4">
      <h1 className="text-4xl font-bold text-gray-800 mb-6">Auth System</h1>
      <Signup />
      <Login />
    </div>
  );
}

export default App;
