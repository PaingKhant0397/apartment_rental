import { useState } from 'react'
import { Link } from 'react-router-dom'
import RegisterForm from '../components/register/RegisterForm'
import { registerUser } from '../services/auth'

function Register() {
  const [userName, setUserName] = useState('')
  const [userEmail, setUserEmail] = useState('')
  const [userPassword, setUserPassword] = useState('')
  const [message, setMessage] = useState('')
  const [loading, setLoading] = useState(false)
  const [errors, setErrors] = useState({})

  const handleChange = e => {
    const { name, value } = e.target
    switch (name) {
      case 'userName':
        setUserName(value)
        break
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
    if (!userName) validationErrors.userName = 'Username is required.'
    if (!userEmail) validationErrors.userEmail = 'Email is required.'
    if (!userPassword) validationErrors.userPassword = 'Password is required.'

    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors)
      setLoading(false)
      return
    }

    try {
      await registerUser({
        user_name: userName,
        user_email: userEmail,
        user_password: userPassword,
        user_role_id: 1,
      })
      setMessage('Registration successful!')
      setUserName('')
      setUserEmail('')
      setUserPassword('')
    } catch (error) {
      setMessage('Registration failed. Please try again.')
      console.error(error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className='min-h-screen flex justify-center items-center bg-gray-100'>
      <div className='bg-white shadow-md rounded-lg p-8 max-w-md w-full'>
        <h2 className='text-2xl font-bold text-center text-gray-700 mb-6'>
          Register
        </h2>
        {message && (
          <div
            className={`mb-4 p-2 text-center text-white rounded ${errors.userName ? 'bg-red-500' : 'bg-green-500'}`}
          >
            {message}
          </div>
        )}
        <RegisterForm
          userName={userName}
          userEmail={userEmail}
          userPassword={userPassword}
          handleChange={handleChange}
          handleSubmit={handleSubmit}
          loading={loading}
          errors={errors}
        />
        <div className='mt-4 text-center'>
          <Link to='/signin' className='text-sm text-blue-600 hover:underline'>
            Already have an account? Login
          </Link>
        </div>
      </div>
    </div>
  )
}

export default Register
