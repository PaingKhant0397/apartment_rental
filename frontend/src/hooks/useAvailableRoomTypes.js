import { useState, useEffect } from 'react'
import {
  fetchAll,
  insert,
  update,
  del,
  fetchOne,
} from '../services/availableRoomTypeServices'
import useNotification from './useNotificaiton'

const useAvailableRoomTypes = () => {
  const [availableRoomTypes, setAvailableRoomTypes] = useState([])
  const notify = useNotification()

  const getAll = async apartmentID => {
    try {
      const data = await fetchAll(apartmentID)
      // console.log(data)
      setAvailableRoomTypes(data)
    } catch (error) {
      console.error(error)
      throw error
    }
  }

  const getOne = async (apartmentID, availableRoomTypeID) => {
    try {
      const data = await fetchOne(apartmentID, availableRoomTypeID)
      return data
    } catch (error) {
      console.error(error)
    }
  }

  const add = async roomType => {
    try {
      console.log(roomType)
      const newAvailableRoomType = await insert(roomType)
      setAvailableRoomTypes(prev => [...prev, newAvailableRoomType])
      notify('success', 'Room Type Added Successfully.')
    } catch (error) {
      console.error(error)
      notify('error', 'Error adding available room type')
    }
  }

  const edit = async (roomTypeID, updatedRoomType) => {
    try {
      const newAvailableRoomType = await update(roomTypeID, updatedRoomType)
      setAvailableRoomTypes(prev =>
        prev.map(rt =>
          rt.available_room_type_id === roomTypeID ? newAvailableRoomType : rt,
        ),
      )
      notify('success', 'Room Type Updated Successfully.')
    } catch (error) {
      console.error(error)
      notify('error', 'Error updating available room types')
    }
  }
  const remove = async (apartmentID, roomTypeID) => {
    try {
      await del(apartmentID, roomTypeID)
      setAvailableRoomTypes(prev =>
        prev.filter(rt => rt.available_room_type_id !== roomTypeID),
      )
      notify('success', 'Room Type Deleted Successfully.')
    } catch (error) {
      notify('error', 'Error removing available room type')
    }
  }

  return {
    availableRoomTypes,
    getAll,
    getOne,
    add,
    edit,
    remove,
  }
}

export default useAvailableRoomTypes
