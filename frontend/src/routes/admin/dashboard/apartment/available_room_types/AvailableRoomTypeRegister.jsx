import { useParams, useNavigate } from 'react-router-dom'
import AvailableRoomTypeForm from '../../../../../components/available_room_types/AvailableRoomTypeForm'
import useAvailableRoomTypes from '../../../../../hooks/useAvailableRoomTypes'
import useRoomTypes from '../../../../../hooks/useRoomTypes'

function AvailableRoomTypeRegister() {
  const { id } = useParams()
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

  const navigate = useNavigate()

  const handleBack = () => {
    navigate(`/admin/dashboard/apartments/${id}/available_room_types`)
  }

  const { add } = useAvailableRoomTypes()
  const { roomTypes } = useRoomTypes()

  return (
    <div className='min-h-fit flex justify-center items-top bg-gray-100'>
      <AvailableRoomTypeForm
        roomTypes={roomTypes}
        onSubmit={add}
        initialData={initialData}
        reset
        handleBack={handleBack}
      />
    </div>
  )
}

export default AvailableRoomTypeRegister
