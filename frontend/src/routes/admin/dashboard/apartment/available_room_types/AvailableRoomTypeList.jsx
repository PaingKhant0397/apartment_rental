/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import useAvailableRoomTypes from '../../../../../hooks/useAvailableRoomTypes'
import AvailableRoomTypeTable from '../../../../../components/available_room_types/AvailableRoomTypeTable'

function AvailableRoomTypeList() {
  const { availableRoomTypes, remove, getAll } = useAvailableRoomTypes()
  const { id } = useParams()

  useEffect(() => {
    getAll(id)
  }, [])

  const navigate = useNavigate()

  const onDelete = (apartmentID, availableRoomTypeID) => {
    remove(apartmentID, availableRoomTypeID)
  }
  const onEdit = availableRoomType => {
    navigate(
      `/admin/dashboard/apartments/${availableRoomType.apartment_id}/available_room_types/${availableRoomType.available_room_type_id}/update`,
    )
  }

  const onAdd = () => {
    navigate(`/admin/dashboard/apartments/${id}/available_room_types/register`)
  }
  return (
    <div className='min-h-screen flex justify-center items-top bg-gray-100'>
      <AvailableRoomTypeTable
        data={availableRoomTypes}
        onDelete={onDelete}
        onEdit={onEdit}
        onAdd={onAdd}
      />
    </div>
  )
}

export default AvailableRoomTypeList
