import { useParams } from 'react-router-dom'
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

  const { add } = useAvailableRoomTypes()
  const { roomTypes } = useRoomTypes()

  return (
    <div className='min-h-screen flex justify-center items-top bg-gray-100'>
      <AvailableRoomTypeForm
        roomTypes={roomTypes}
        onSubmit={add}
        initialData={initialData}
        reset
      />
    </div>
  )
}

export default AvailableRoomTypeRegister
