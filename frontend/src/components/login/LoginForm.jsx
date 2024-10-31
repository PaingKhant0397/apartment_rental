import { TextField, Button, CircularProgress } from '@mui/material'

function LoginForm({
  userEmail,
  userPassword,
  handleChange,
  handleSubmit,
  loading,
  errors,
}) {
  return (
    <form onSubmit={handleSubmit}>
      <div className='mb-4'>
        <TextField
          fullWidth
          label='Email'
          name='userEmail'
          value={userEmail}
          onChange={handleChange}
          error={!!errors.userEmail}
          helperText={errors.userEmail}
          variant='outlined'
          margin='normal'
          required
        />
      </div>
      <div className='mb-4'>
        <TextField
          fullWidth
          label='Password'
          name='userPassword'
          type='password'
          value={userPassword}
          onChange={handleChange}
          error={!!errors.userPassword}
          helperText={errors.userPassword}
          variant='outlined'
          margin='normal'
          required
        />
      </div>
      <Button
        type='submit'
        variant='contained'
        color='primary'
        fullWidth
        disabled={loading}
        sx={{ position: 'relative' }}
      >
        {loading ? <CircularProgress size={24} /> : 'Login'}
      </Button>
    </form>
  )
}

export default LoginForm
