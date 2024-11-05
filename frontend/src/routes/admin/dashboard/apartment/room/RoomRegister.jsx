import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import RoomForm from '../../../../../components/room/RoomForm'
import useRooms from '../../../../../hooks/useRooms'
import useAvailableRoomTypes from '../../../../../hooks/useAvailableRoomTypes'
import useRoomStatuses from '../../../../../hooks/useRoomStatuses'
import Loading from '../../../../../components/Loading'
// import RoomForm from '../../../../components/room/RoomForm'
// import useRooms from '../../../../hooks/useRooms'
// import useAvailableRoomTypes from '../../../../hooks/useAvailableRoomTypes'
// import useRoomStatuses from '../../../../hooks/useRoomStatuses'
// import Loading from '../../../../components/Loading'

function RoomRegister() {
  const { id: apartmentId } = useParams()
  // console.log(apartmentId)
  const { getAllRooms, createRoom } = useRooms(apartmentId)
  const {
    loading: loadingRoomTypes,
    availableRoomTypes,
    getAll: fetchAllAvailableRoomTypes,
  } = useAvailableRoomTypes()
  const { loading: loadingStatuses, roomStatuses } = useRoomStatuses()

  // const [availableRoomTypes, setAvailableRoomTypes] = useState([])
  // const [roomStatuses, setRoomStatuses] = useState([])
  const [loading, setLoading] = useState(true)

  const initialData = {
    available_room_type: {},
    status: {},
    room_no: '',
    room_size: '',
    room_floor_no: '',
  }

  useEffect(() => {
    const loadData = async () => {
      setLoading(true)
      try {
        await fetchAllAvailableRoomTypes(apartmentId)
        // setAvailableRoomTypes(roomTypes)
        // const statuses = await fetchAllRoomStatuses()
        // setRoomStatuses(statuses)
      } catch (error) {
        console.error('Error loading data:', error)
      } finally {
        setLoading(false)
      }
    }

    loadData()
  }, [apartmentId])

  const handleOnSubmit = async roomData => {
    // const formattedData = {
    //   available_room_type: {
    //     available_room_type_id:
    //       roomData.available_room_type.available_room_type_id,
    //     apartment_id: apartmentId,
    //     // Additional fields as necessary
    //   },
    //   status: {
    //     room_status_id: roomData.status.room_status_id,
    //     // Additional fields as necessary
    //   },
    //   room_no: roomData.room_no,
    //   room_size: roomData.room_size,
    //   room_floor_no: roomData.room_floor_no,
    // }

    // console.log(roomData)
    await createRoom(roomData)
    // Handle success or redirect
  }

  if (loading || loadingRoomTypes || loadingStatuses) {
    return <Loading />
  }

  return (
    <div className='min-h-fit flex justify-center items-top bg-gray-100'>
      <RoomForm
        onSubmit={handleOnSubmit}
        initialData={initialData}
        availableRoomTypes={availableRoomTypes}
        statuses={roomStatuses}
      />
    </div>
  )
}

export default RoomRegister
