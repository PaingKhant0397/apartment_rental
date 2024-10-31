import InputField from '../InputField'
import Message from '../notification/Message'

function AdminLoginForm({
  adminUsername,
  adminPassword,
  handleChange,
  handleSubmit,
  loading,
  message,
  errors,
}) {
  return (
    <div className='bg-white p-8 rounded-lg shadow-md w-full max-w-md'>
      <h1 className='text-2xl font-bold mb-6 text-center'>Login</h1>
      <form onSubmit={handleSubmit}>
        {/* Email Input Field */}
        <InputField
          id='adminUsername'
          label='Username'
          type='text'
          value={adminUsername}
          onChange={handleChange}
          error={errors.adminUsername}
          required
        />
        {/* Password Input Field */}
        <InputField
          id='adminPassword'
          label='Password'
          type='password'
          value={adminPassword}
          onChange={handleChange}
          error={errors.adminPassword}
          required
        />
        {/* Submit Button */}
        <button
          type='submit'
          className='w-full bg-indigo-600 text-white py-2 px-4 rounded-md shadow hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2'
          disabled={loading}
        >
          {loading ? 'Logging In...' : 'Login'}
        </button>
      </form>
      {/* Message for results */}
      {message && <Message message={message} />}
    </div>
  )
}

export default AdminLoginForm
