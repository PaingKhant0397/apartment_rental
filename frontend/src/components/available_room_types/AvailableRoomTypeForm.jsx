import { useState, useEffect } from 'react'
import {
  TextField,
  Button,
  MenuItem,
  Typography,
  Box,
  Paper,
} from '@mui/material'

function AvailableRoomTypeForm({
  roomTypes,
  onSubmit,
  initialData,
  reset,
  handleBack,
}) {
  const [formData, setFormData] = useState(initialData)

  useEffect(() => {
    setFormData(initialData)
  }, [initialData])

  const handleChange = e => {
    const { name, value, type } = e.target

    if (type === 'file') {
      setFormData({ ...formData, [name]: e.target.files[0] })
    } else if (name === 'room_type') {
      const selectedRoomType = roomTypes.find(
        roomType => Number(roomType.room_type_id) === Number(value),
      )
      setFormData(prevData => ({
        ...prevData,
        room_type: {
          ...prevData.room_type,
          room_type_id: Number(value),
          room_type_name: selectedRoomType?.room_type_name || '',
        },
      }))
    } else {
      setFormData({ ...formData, [name]: value })
    }
  }

  const handleSubmit = e => {
    e.preventDefault()
    onSubmit(formData)
    if (reset) {
      setFormData(initialData)
    }
  }

  return (
    <Paper elevation={3} className='w-full p-6'>
      <Typography variant='h5' component='h1' gutterBottom>
        {formData.available_room_type_id
          ? 'Edit Available Room Type'
          : 'Add Available Room Type'}
      </Typography>
      <form onSubmit={handleSubmit}>
        <Box mb={3}>
          <TextField
            id='available_room_type_price'
            label='Price'
            type='number'
            variant='outlined'
            fullWidth
            name='available_room_type_price'
            value={formData.available_room_type_price || ''}
            onChange={handleChange}
            required
          />
        </Box>

        <Box mb={3}>
          <TextField
            id='available_room_type_deposit_amount'
            label='Deposit Amount'
            type='number'
            variant='outlined'
            fullWidth
            name='available_room_type_deposit_amount'
            value={formData.available_room_type_deposit_amount || ''}
            onChange={handleChange}
            required
          />
        </Box>

        <Box mb={3}>
          <TextField
            id='room_type'
            label='Room Type'
            select
            fullWidth
            variant='outlined'
            name='room_type'
            value={formData.room_type.room_type_id || ''}
            onChange={handleChange}
            required
          >
            {roomTypes.map(roomType => (
              <MenuItem
                key={roomType.room_type_id}
                value={roomType.room_type_id}
              >
                {roomType.room_type_name}
              </MenuItem>
            ))}
          </TextField>
        </Box>

        <Box display='flex' gap={2}>
          <Button type='submit' variant='contained' color='primary'>
            {formData.available_room_type_id ? 'Update' : 'Submit'}
          </Button>
          <Button onClick={handleBack} variant='outlined' color='secondary'>
            Go Back
          </Button>
        </Box>
      </form>
    </Paper>
  )
}

export default AvailableRoomTypeForm
