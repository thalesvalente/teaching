import axios from "axios";

const API_URL = "http://localhost:3000";

const createUser = async (userData: {
  username: string;
  password: string;
  role: string;
  protocol?: string;
}) => {
  const response = await axios.post(`${API_URL}/users/register`, userData);
  return response.data;
};

const loginUser = async (loginData: { username: string; password: string }) => {
  const response = await axios.post(`${API_URL}/auth/login`, loginData);
  return response.data;
};

const updateUserProfile = async (
  token: string,
  updateData: { username?: string; password?: string; profilePicture?: string }
) => {
  const response = await axios.put(`${API_URL}/users/profile`, updateData, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

const submitScript = async (token: string, scriptData: { content: string }) => {
  const response = await axios.post(`${API_URL}/scripts/submit`, scriptData, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

export interface Analysis {
  id: number;
  result: string;
  scriptId: number;
}

const getAnalysis = async (
  token: string,
  scriptId: number
): Promise<Analysis[]> => {
  const response = await axios.get(`${API_URL}/analysis/${scriptId}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

const createChatCompletion = async (
  messages: { role: string; content: string }[]
) => {
  const response = await axios.post(`${API_URL}/openai/chatCompletion`, {
    messages,
  });
  return response.data;
};
const getAllUsers = async (token: string) => {
  const response = await axios.get(`${API_URL}/users`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

const updateUser = async (token: string, id: string, updateData: any) => {
  const response = await axios.put(`${API_URL}/users/${id}`, updateData, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

const updateUserRole = async (token: string, id: string, role: string) => {
  const response = await axios.put(
    `${API_URL}/users/${id}/role`,
    { role },
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );
  return response.data;
};
const getAllScripts = async (token: string) => {
  const response = await axios.get(`${API_URL}/scripts`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

const updateScript = async (token: string, id: string, updateData: any) => {
  const response = await axios.put(`${API_URL}/scripts/${id}`, updateData, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

const deleteScript = async (token: string, id: string) => {
  const response = await axios.delete(`${API_URL}/scripts/${id}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

const createApi = async (
  token: string,
  apiData: { name: string; url: string }
) => {
  const response = await axios.post(API_URL, apiData, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

const getAllApis = async (token: string) => {
  const response = await axios.get(API_URL, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

const deleteApi = async (token: string, id: number) => {
  const response = await axios.delete(`${API_URL}/${id}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

export {
  createUser,
  loginUser,
  updateUserProfile,
  submitScript,
  getAnalysis,
  createChatCompletion,
  getAllUsers,
  updateUser,
  updateUserRole,
  getAllScripts,
  updateScript,
  deleteScript,
  createApi,
  getAllApis,
  deleteApi,
};
