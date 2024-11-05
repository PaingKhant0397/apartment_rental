import { useEffect, useState } from 'react'
import { Button, Box, Typography, Stack } from '@mui/material'
import InputField from '../InputField'

function RoomRegisterForm({
  onSubmit,
  initialData,
  availableRoomTypes,
  statuses,
  reset,
}) {
  const [formData, setFormData] = useState(initialData)

  useEffect(() => {
    setFormData(initialData)
  }, [initialData])
  // console.log('avl', availableRoomTypes)

  const handleChange = e => {
    const { name, value } = e.target

    if (name === 'available_room_type_id') {
      const selectedRoomType = availableRoomTypes.find(
        type => type.available_room_type_id === parseInt(value),
      )
      setFormData(prevData => ({
        ...prevData,
        available_room_type: selectedRoomType || {},
      }))
    } else if (name === 'room_status_id') {
      const selectedStatus = statuses.find(
        status => status.room_status_id === parseInt(value),
      )
      setFormData(prevData => ({
        ...prevData,
        status: selectedStatus || {},
      }))
    } else {
      setFormData(prevData => ({ ...prevData, [name]: value }))
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
    <Box
      sx={{
        bgcolor: 'background.paper',
        p: 4,
        borderRadius: 2,
        boxShadow: 3,
        width: '100%',
      }}
    >
      <Typography variant='h4' component='h1' gutterBottom>
        {formData.room_id ? 'Edit Room' : 'Register Room'}
      </Typography>
      <Box component='form' onSubmit={handleSubmit}>
        <Stack spacing={3}>
          <InputField
            id='room_no'
            label='Room Number'
            type='text'
            value={formData.room_no}
            onChange={handleChange}
            required
          />

          <InputField
            id='room_size'
            label='Room Size'
            type='text'
            value={formData.room_size}
            onChange={handleChange}
            required
          />

          <InputField
            id='room_floor_no'
            label='Floor Number'
            type='text'
            value={formData.room_floor_no}
            onChange={handleChange}
            required
          />

          <InputField
            id='available_room_type_id'
            label='Available Room Type'
            type='select'
            value={formData?.available_room_type.available_room_type_id || ''}
            onChange={handleChange}
            required
            options={availableRoomTypes.map(roomType => ({
              value: roomType.available_room_type_id,
              label: `${roomType.room_type.room_type_name} - Price: ${roomType.available_room_type_price}`,
            }))}
          />

          <InputField
            id='room_status_id'
            label='Room Status'
            type='select'
            value={formData.status.room_status_id || ''}
            onChange={handleChange}
            required
            options={statuses.map(status => ({
              value: status.room_status_id,
              label: status.room_status_name,
            }))}
          />

          <Button
            type='submit'
            variant='contained'
            color='primary'
            sx={{ py: 1.5 }}
          >
            {formData.room_id ? 'Update' : 'Submit'}
          </Button>
        </Stack>
      </Box>
    </Box>
  )
}

export default RoomRegisterForm
