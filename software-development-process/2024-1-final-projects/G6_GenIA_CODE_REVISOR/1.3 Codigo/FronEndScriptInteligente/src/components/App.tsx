import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Home from "../pages/Home";
import Login from "../pages/Login";
import Register from "../pages/Register";
import UserDashboard from "../pages/UserDashboard";
import EditProfile from "../pages/EditProfile";
import UserHome from "../pages/UserHome";
import EmployeeDashboard from "../pages/EmployeeDashboard";
import ViewUserScripts from "../pages/ViewUserScripts";
import AdminDashboard from "../pages/AdminDashboard";
import ConfigureIntegrations from "../pages/ConfigureIntegrations";
import ManageUsers from "../pages/ManageUsers";
import ManageScripts from "../pages/ManageScripts";
import AuditActivities from "../pages/AuditActivities";
import SystemMaintenance from "../pages/SystemMaintenance";
import "../styles/main.css";
import homeIcon from "./images/homeIcon.ico";
import painelFuncionarioIcon from "./images/painel_funcionario.ico";
import painelAdmIcon from "./images/painel_adm.ico";

const App: React.FC = () => {
  const [userType, setUserType] = useState<string | null>(null);

  return (
    <Router>
      <div>
        <nav>
          <ul className="navigation">
            <li>
              <Link to="/" className="nav-icon">
                <img src={homeIcon} alt="Home Icon" className="nav-icon" />
              </Link>
            </li>
            {userType === "user" && (
              <>
                <li>
                  <Link to="/user-home">User Home</Link>
                </li>
              </>
            )}
            {userType === "employee" && (
              <>
                <li>
                  <Link to="/employee-dashboard" className="nav-icon">
                    <img
                      src={painelFuncionarioIcon}
                      alt="Employee Dashboard"
                      className="nav-icon"
                    />
                  </Link>
                </li>
              </>
            )}
            {userType === "admin" && (
              <>
                <li>
                  <Link to="/admin-dashboard" className="nav-icon">
                    <img
                      src={painelAdmIcon}
                      alt="Admin Dashboard"
                      className="nav-icon"
                    />
                  </Link>
                </li>
              </>
            )}
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login onLogin={setUserType} />} />
          <Route
            path="/register"
            element={<Register onRegister={setUserType} />}
          />
          <Route path="/user-dashboard" element={<UserDashboard />} />
          <Route path="/edit-profile" element={<EditProfile />} />
          <Route path="/user-home" element={<UserHome />} />
          <Route path="/employee-dashboard" element={<EmployeeDashboard />} />
          <Route path="/view-user-scripts" element={<ViewUserScripts />} />
          <Route path="/admin-dashboard" element={<AdminDashboard />} />
          <Route
            path="/configure-integrations"
            element={<ConfigureIntegrations />}
          />
          <Route path="/manage-users" element={<ManageUsers />} />
          <Route path="/manage-scripts" element={<ManageScripts />} />
          <Route path="/audit-activities" element={<AuditActivities />} />
          <Route path="/system-maintenance" element={<SystemMaintenance />} />
        </Routes>
        <footer>
          © 2024 Script Inteligente. Todos os direitos reservados.
        </footer>
      </div>
    </Router>
  );
};

export default App;
