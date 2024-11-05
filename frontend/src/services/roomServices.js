/* eslint-disable camelcase */
import axios from 'axios'
import { getItem } from '../utils/localStorageUtils'

const BASE_URL = `${import.meta.env.VITE_BASE_URL}/api/apartments`

const fetchAllRooms = async (apartmentId, limit = 10, offset = 0) => {
  try {
    const response = await axios.get(`${BASE_URL}/${apartmentId}/rooms`, {
      params: { limit, offset },
      headers: {
        Authorization: `Bearer ${getItem('adminToken')}`,
      },
    })
    return response.data // Ensure this includes both rooms and total count
  } catch (error) {
    console.error('Error fetching rooms:', error)
    throw error
  }
}

const fetchAvailableRoom = async (
  apartmentId,
  room_type,
  limit = 0,
  offset = 0,
) => {
  try {
    const response = await axios.get(`${BASE_URL}/${apartmentId}/rooms`, {
      params: { limit, offset, room_type },
      headers: {
        Authorization: `Bearer ${getItem('adminToken')}`,
      },
    })
    return response.data // Ensure this includes both rooms and total count
  } catch (error) {
    console.error('Error fetching rooms:', error)
    throw error
  }
}

const fetchRoomById = async (apartmentId, roomId) => {
  try {
    const response = await axios.get(
      `${BASE_URL}/${apartmentId}/rooms/${roomId}`,
      {
        headers: {
          Authorization: `Bearer ${getItem('adminToken')}`,
        },
      },
    )
    return response.data
  } catch (error) {
    console.error('Error fetching room:', error)
    throw error
  }
}

const insertRoom = async (apartmentId, roomData) => {
  try {
    const response = await axios.post(
      `${BASE_URL}/${apartmentId}/rooms`,
      roomData,
      {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${getItem('adminToken')}`,
        },
      },
    )
    return response.data
  } catch (error) {
    console.error('Error creating room:', error)
    throw error
  }
}

const updateRoom = async (apartmentId, roomId, roomData) => {
  try {
    const response = await axios.put(
      `${BASE_URL}/${apartmentId}/rooms/${roomId}`,
      roomData,
      {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${getItem('adminToken')}`,
        },
      },
    )
    return response.data
  } catch (error) {
    console.error('Error updating room:', error)
    throw error
  }
}

const deleteRoom = async (apartmentId, roomId) => {
  try {
    await axios.delete(`${BASE_URL}/${apartmentId}/rooms/${roomId}`, {
      headers: {
        Authorization: `Bearer ${getItem('adminToken')}`,
      },
    })
  } catch (error) {
    console.error('Error deleting room:', error)
    throw error
  }
}

export {
  fetchAllRooms,
  fetchAvailableRoom,
  fetchRoomById,
  insertRoom,
  updateRoom,
  deleteRoom,
}
