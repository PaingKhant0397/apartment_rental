import { useState, useEffect } from 'react'
import InputField from '../InputField'
import Button from '../Button'

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
    // e.preventDefault()
    onSubmit(formData)
    if (reset) {
      setFormData(initialData)
    }
  }

  return (
    <div className='bg-white p-8 rounded-lg shadow-md w-full'>
      <h1 className='text-2xl font-bold mb-5'>Register Apartment</h1>
      <form action=''>
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
        <Button onClick={handleSubmit}>
          {formData.apartment_id ? 'Update' : 'Submit'}
        </Button>
      </form>
    </div>
  )
}

export default ApartmentForm
