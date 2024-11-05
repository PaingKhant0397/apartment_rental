import { useState, useEffect } from 'react'
import { Button, Box, Typography, Stack } from '@mui/material'
import InputField from '../InputField'

function ApartmentForm({ onSubmit, initialData, reset }) {
  const [formData, setFormData] = useState(initialData)

  useEffect(() => {
    setFormData(initialData)
  }, [initialData])

  const handleChange = e => {
    const { name, value, type } = e.target
    if (type === 'file') {
      setFormData({ ...formData, [name]: e.target.files[0] })
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
        {formData.apartment_id ? 'Edit Apartment' : 'Register Apartment'}
        {/* <br > */}
      </Typography>
      <Box component='form' onSubmit={handleSubmit}>
        <Stack spacing={3}>
          <InputField
            id='apartment_name'
            label='Name'
            type='text'
            value={formData.apartment_name}
            onChange={handleChange}
            required
          />

          <InputField
            id='apartment_date_built'
            label='Apartment Built Date'
            type='date'
            value={formData.apartment_date_built}
            onChange={handleChange}
            required
          />

          <InputField
            id='apartment_capacity'
            label='Capacity'
            type='number'
            value={formData.apartment_capacity}
            onChange={handleChange}
            required
          />

          <InputField
            id='apartment_postal_code'
            label='Postal Code'
            type='number'
            value={formData.apartment_postal_code}
            onChange={handleChange}
            required
          />

          <InputField
            id='apartment_address'
            label='Address'
            type='textarea'
            value={formData.apartment_address}
            onChange={handleChange}
            required
          />

          <InputField
            id='apartment_image'
            label='Apartment Image'
            type='file'
            value={formData.apartment_image}
            onChange={handleChange}
            required
          />

          <InputField
            id='apartment_desc'
            label='Description'
            type='textarea'
            value={formData.apartment_desc}
            onChange={handleChange}
            required
          />

          <Button
            type='submit'
            variant='contained'
            color='primary'
            sx={{ py: 1.5 }}
          >
            {formData.apartment_id ? 'Update' : 'Submit'}
          </Button>
        </Stack>
      </Box>
    </Box>
  )
}

export default ApartmentForm
