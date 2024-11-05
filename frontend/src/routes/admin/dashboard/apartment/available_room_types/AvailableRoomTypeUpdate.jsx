/* eslint-disable react-hooks/exhaustive-deps */
import { useParams, useNavigate } from 'react-router-dom'
import { useEffect, useState } from 'react'
import AvailableRoomTypeForm from '../../../../../components/available_room_types/AvailableRoomTypeForm'
import useAvailableRoomTypes from '../../../../../hooks/useAvailableRoomTypes'
import useRoomTypes from '../../../../../hooks/useRoomTypes'

function AvailableRoomTypeUpdate() {
  // eslint-disable-next-line camelcase
  const { id, available_room_type_id } = useParams()
  const initialData = {
    available_room_type_id: '',
    apartment_id: id,
    room_type: {
      room_type_id: '',
      room_type_name: '',
    },
    available_room_type_price: '',
    available_room_type_deposit_amount: '',
  }
  const [availableRoomType, setAvailableRoomType] = useState(initialData)
  const { getOne, edit } = useAvailableRoomTypes()
  const { roomTypes } = useRoomTypes()

  useEffect(() => {
    const getArt = async () => {
      try {
        const art = await getOne(id, available_room_type_id)
        setAvailableRoomType(art)
      } catch (error) {
        console.error(error)
      }
    }

    getArt()
  }, [])

  const navigate = useNavigate()

  const handleBack = () => {
    navigate(`/admin/dashboard/apartments/${id}/available_room_types`)
  }

  const handleSubmit = formData => {
    edit(formData.available_room_type_id, formData)
  }

  return (
    <div className='min-h-screen flex justify-center items-top bg-gray-100'>
      <AvailableRoomTypeForm
        roomTypes={roomTypes}
        onSubmit={handleSubmit}
        initialData={availableRoomType}
        reset={false}
        handleBack={handleBack}
      />
    </div>
  )
}

export default AvailableRoomTypeUpdate
