import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import AdminLoginForm from '../../components/adminLogin/AdminLoginForm'
import { loginAdmin } from '../../services/auth'

function AdminLogin() {
  const [adminUsername, setAdminUsername] = useState('')
  const [adminPassword, setAdminPassword] = useState('')

  const [message, setMessage] = useState('')
  const [loading, setLoading] = useState(false)
  const [errors, setErrors] = useState({})

  const navigate = useNavigate()

  const handleChange = e => {
    const { name, value } = e.target
    switch (name) {
      case 'adminUsername':
        setAdminUsername(value)
        break
      case 'adminPassword':
        setAdminPassword(value)
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
    if (!adminUsername) validationErrors.adminUsername = 'Email is required.'
    if (!adminPassword) validationErrors.adminPassword = 'Password is required.'

    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors)
      setLoading(false)
      return
    }

    try {
      await loginAdmin({
        admin_username: adminUsername,
        admin_password: adminPassword,
      })
      setMessage('Login successful!')
      navigate('/admin/dashboard/')
      setAdminUsername('')
      setAdminPassword('')
    } catch (error) {
      setMessage('Login failed. Please try again.')
      console.error(error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className='min-h-screen flex justify-center items-center bg-gray-100'>
      <AdminLoginForm
        adminUsername={adminUsername}
        adminPassword={adminPassword}
        handleChange={handleChange}
        handleSubmit={handleSubmit}
        loading={loading}
        message={message}
        errors={errors}
      />
    </div>
  )
}

export default AdminLogin
