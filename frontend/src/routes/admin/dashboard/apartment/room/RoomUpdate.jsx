import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { toast } from 'react-toastify'
import RoomForm from '../../../../../components/room/RoomForm'
import useRooms from '../../../../../hooks/useRooms'
import useAvailableRoomTypes from '../../../../../hooks/useAvailableRoomTypes'
import useRoomStatuses from '../../../../../hooks/useRoomStatuses'
import Loading from '../../../../../components/Loading'

function RoomUpdate() {
  const { id, room_id: roomId } = useParams() // Assuming you're using React Router to get the room ID from the URL
  const { getRoomById, modifyRoom, loading } = useRooms(id) // Hook to manage room data
  const {
    availableRoomTypes,
    getAll,
    loading: loadingRoomTypes,
  } = useAvailableRoomTypes() // Fetch available room types
  const { roomStatuses, loading: loadingStatuses } = useRoomStatuses() // Fetch statuses (this hook should be created similarly to availableRoomTypes)

  const [initialData, setInitialData] = useState({
    room_id: null,
    available_room_type: {},
    status: {},
    room_no: '',
    room_size: '',
    room_floor_no: '',
  })

  useEffect(() => {
    const fetchRoom = async () => {
      const room = await getRoomById(roomId)
      setInitialData(room)
    }
    getAll(id)

    fetchRoom()
  }, [roomId])

  const handleUpdate = async roomData => {
    await modifyRoom(roomId, roomData)
    toast.success('Room updated successfully!')
  }

  if (loading || loadingRoomTypes || loadingStatuses) return <Loading />

  return (
    <div className='min-h-screen flex justify-center items-top bg-gray-100'>
      <RoomForm
        onSubmit={handleUpdate}
        initialData={initialData}
        availableRoomTypes={availableRoomTypes}
        statuses={roomStatuses}
      />
    </div>
  )
}

export default RoomUpdate
