import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { loginUser } from '../services/auth'
import LoginForm from '../components/login/LoginForm'

function Login() {
  const [userEmail, setUserEmail] = useState('')
  const [userPassword, setUserPassword] = useState('')
  const [message, setMessage] = useState('')
  const [loading, setLoading] = useState(false)
  const [errors, setErrors] = useState({})
  const navigate = useNavigate()
  const handleChange = e => {
    const { name, value } = e.target
    switch (name) {
      case 'userEmail':
        setUserEmail(value)
        break
      case 'userPassword':
        setUserPassword(value)
        break
      default:
        break
    }
  }

  const handleSubmit = async e => {
    e.preventDefault()
    setLoading(true)
    setMessage('')
    setErrors({})

    const validationErrors = {}
    if (!userEmail) validationErrors.userEmail = 'Email is required.'
    if (!userPassword) validationErrors.userPassword = 'Password is required.'

    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors)
      setLoading(false)
      return
    }

    try {
      await loginUser({
        user_email: userEmail,
        user_password: userPassword,
      })
      setMessage('Login successful!')
      setUserEmail('')
      setUserPassword('')
      navigate('/Home')
    } catch (error) {
      setMessage('Login failed. Please try again.')
      console.error(error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className='min-h-screen flex justify-center items-center bg-gray-100'>
      <div className='bg-white shadow-md rounded-lg p-8 max-w-md w-full'>
        <h2 className='text-2xl font-bold text-center text-gray-700 mb-6'>
          Login
        </h2>
        {message && (
          <div
            className={`mb-4 p-2 text-center text-white rounded ${errors.userEmail ? 'bg-red-500' : 'bg-green-500'}`}
          >
            {message}
          </div>
        )}
        <LoginForm
          userEmail={userEmail}
          userPassword={userPassword}
          handleChange={handleChange}
          handleSubmit={handleSubmit}
          loading={loading}
          errors={errors}
        />
        {/* <div className='mt-6 text-center'>
          <Link
            to='/forgot-password'
            className='text-sm text-blue-600 hover:underline'
          >
            Forgot Password?
          </Link>
        </div> */}
        <div className='mt-4 text-center'>
          <Link to='/signup' className='text-sm text-blue-600 hover:underline'>
            Don't have an account? Sign Up
          </Link>
        </div>
      </div>
    </div>
  )
}

export default Login
