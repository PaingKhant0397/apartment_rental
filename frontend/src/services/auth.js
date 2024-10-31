import axios from 'axios'
import { setItem } from '../utils/localStorageUtils'

const BASE_URL = `${import.meta.env.VITE_API_URL}`

// Register user
const registerUser = async userData => {
  // console.log(userData)
  // return userData
  const response = await axios.post(`${BASE_URL}/auth/register_user`, userData)
  console.log(response.data)
  return response.data
}

// Login user
const loginUser = async userData => {
  try {
    const response = await axios.post(`${BASE_URL}/auth/login_user`, userData)

    // Destructure response to get token and user data
    const { token, user } = response.data

    // Store token and user information in localStorage

    setItem('token', token)
    setItem('user', JSON.stringify(user)) // Store user object as a string

    // console.log('Login Successful:', user) // Log user object
    return response.data
  } catch (error) {
    console.error('Login error:', error)
    throw error
  }
}

const loginAdmin = async adminData => {
  try {
    const response = await axios.post(`${BASE_URL}/auth/login_admin`, adminData)
    // console.log(response.data)

    // Store token
    if (response.data.token) {
      localStorage.setItem('adminToken', response.data.token)
    }

    return response.data
  } catch (error) {
    console.error('Error during admin login:', error)
    throw error
  }
}

export { registerUser, loginUser, loginAdmin }
