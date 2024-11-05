/* eslint-disable camelcase */
import { useEffect, useState } from 'react'
import {
  fetchAllRooms,
  fetchRoomById,
  insertRoom,
  updateRoom,
  deleteRoom,
  fetchAvailableRoom,
} from '../services/roomServices'
import useNotification from './useNotificaiton'

const useRooms = apartmentId => {
  const [rooms, setRooms] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [pagination, setPagination] = useState({
    limit: 10,
    offset: 0,
    total: 0,
  })

  const notify = useNotification()

  const getAllRooms = async () => {
    setLoading(true)
    try {
      const data = await fetchAllRooms(
        apartmentId,
        pagination.limit,
        pagination.offset,
      )
      setRooms(data.data)
      setPagination(prev => ({ ...prev, total: data.total_count }))
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load rooms')
    } finally {
      setLoading(false)
    }
  }

  const getAvailableRooms = async (aID, room_type) => {
    setLoading(true)
    try {
      const data = await fetchAvailableRoom(aID, room_type)
      setRooms(data.data)
      setPagination(prev => ({ ...prev, total: data.total_count }))
      return {
        total_count: data.total_count,
        data: data.data,
      }
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load rooms')
    } finally {
      setLoading(false)
    }
  }

  const getRoomById = async roomId => {
    setLoading(true)
    try {
      const room = await fetchRoomById(apartmentId, roomId)
      return room
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load room details')
    } finally {
      setLoading(false)
    }
  }

  const createRoom = async roomData => {
    setLoading(true)
    try {
      const newRoom = await insertRoom(apartmentId, roomData)
      setRooms(prev => [...prev, newRoom])
      notify('success', 'Room added successfully')
    } catch (err) {
      setError(err)
      notify('error', 'Failed to add room')
    } finally {
      setLoading(false)
    }
  }

  const modifyRoom = async (roomId, roomData) => {
    setLoading(true)
    try {
      const updatedRoom = await updateRoom(apartmentId, roomId, roomData)
      setRooms(prevRooms =>
        prevRooms.map(room => (room.room_id === roomId ? updatedRoom : room)),
      )
      notify('success', 'Room updated successfully')
    } catch (err) {
      setError(err)
      notify('error', 'Failed to update room')
    } finally {
      setLoading(false)
    }
  }

  const removeRoom = async roomId => {
    setLoading(true)
    try {
      await deleteRoom(apartmentId, roomId)
      setRooms(prevRooms => prevRooms.filter(room => room.room_id !== roomId))
      notify('success', 'Room deleted successfully')
    } catch (err) {
      setError(err)
      notify('error', 'Failed to delete room')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    if (apartmentId) {
      getAllRooms() // Fetch rooms on mount or when apartmentId changes
    }
  }, [apartmentId, pagination.limit, pagination.offset])

  return {
    rooms,
    loading,
    error,
    pagination,
    getRoomById,
    createRoom,
    modifyRoom,
    removeRoom,
    getAvailableRooms,
    // getAllRooms,
    setPagination, // Allow setting pagination from components
  }
}

export default useRooms
