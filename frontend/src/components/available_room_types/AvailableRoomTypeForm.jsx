import { useState, useEffect } from 'react'
import InputField from '../InputField'
import Button from '../Button'

function AvailableRoomTypeForm({ roomTypes, onSubmit, initialData, reset }) {
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
      // console.log('selected', selectedRoomType)
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
    // console.log(formData)
  }

  const handleSubmit = e => {
    e.preventDefault()
    // console.log(formData)
    onSubmit(formData)
    if (reset) {
      setFormData(initialData)
    }
  }

  return (
    <div className='bg-white p-8 rounded-lg shadow-md w-full'>
      <h1 className='text-2xl font-bold mb-5'>Add Available Room Type</h1>
      <form action=''>
        <InputField
          id='available_room_type_price'
          label='Price'
          type='number'
          value={formData.available_room_type_price}
          onChange={handleChange}
          required
        />

        <InputField
          id='available_room_type_deposit_amount'
          label='Deposit Amount'
          type='number'
          value={formData.available_room_type_deposit_amount}
          onChange={handleChange}
          required
        />

        <InputField
          id='room_type'
          label='Room Type'
          type='select'
          value={formData.room_type.room_type_id}
          onChange={handleChange}
          required
          options={roomTypes.map(roomType => ({
            value: roomType.room_type_id,
            label: roomType.room_type_name,
          }))}
        />

        <Button onClick={handleSubmit}>
          {formData.available_room_type_id ? 'Update' : 'Submit'}
        </Button>
      </form>
    </div>
  )
}

export default AvailableRoomTypeForm
