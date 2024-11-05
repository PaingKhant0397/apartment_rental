import { useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { Button } from '@mui/material'
import useRooms from '../../../../../hooks/useRooms'
import RoomTable from '../../../../../components/room/RoomTable'
import Loading from '../../../../../components/Loading'

function RoomList() {
  const { id: apartmentId } = useParams()
  const { rooms, loading, removeRoom, getAllRooms, pagination, setPagination } =
    useRooms(apartmentId)
  console.log('rooms', rooms)
  const navigate = useNavigate()

  // useEffect(() => {
  //   getAllRooms()
  // }, [pagination.limit, pagination.offset]) // Fetch rooms when pagination changes

  const onDelete = id => {
    removeRoom(id)
  }

  const onEdit = room => {
    navigate(
      `/admin/dashboard/apartments/${apartmentId}/rooms/${room.room_id}/update`,
    )
  }

  const onRegister = () => {
    navigate(`/admin/dashboard/apartments/${apartmentId}/rooms/register`)
  }

  return (
    <div className='min-h-fit flex justify-center items-top bg-gray-100'>
      {loading && <Loading />}

      <RoomTable
        rooms={rooms}
        onDelete={onDelete}
        onEdit={onEdit}
        onRegister={onRegister}
        totalCount={pagination.total}
        currentPage={pagination.offset / pagination.limit + 1} // Calculate current page
        setCurrentPage={page =>
          setPagination(prev => ({
            ...prev,
            offset: (page - 1) * pagination.limit,
          }))
        }
        limit={pagination.limit}
      />
    </div>
  )
}

export default RoomList
