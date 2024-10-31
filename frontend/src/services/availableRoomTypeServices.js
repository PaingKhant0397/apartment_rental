// src/services/availableRoomTypeService.js
import axios from 'axios'
import { getItem } from '../utils/localStorageUtils'

const BASE_URL = import.meta.env.VITE_API_URL

// Get all available room types
const fetchAll = async apartmentID => {
  try {
    const response = await axios.get(
      `${BASE_URL}/apartments/${apartmentID}/available_room_types`,
    )
    // console.log(response)
    return response.data
  } catch (error) {
    console.error('Error fetching available room types:', error)
    throw error
  }
}

const fetchOne = async (apartmentId, availableRoomTypeID) => {
  try {
    const response = await axios.get(
      `${BASE_URL}/apartments/${apartmentId}/available_room_types/${availableRoomTypeID}`,
    )
    return response.data
  } catch (error) {
    console.error('Error fetching available room types:', error)
    throw error
  }
}

// Create an available room type
const insert = async roomTypeData => {
  try {
    const token = getItem('adminToken')
    const response = await axios.post(
      `${BASE_URL}/apartments/${roomTypeData.apartment_id}/available_room_types`,
      roomTypeData,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      },
    )
    return response.data
  } catch (error) {
    console.error('Error creating available room type:', error)
    throw error
  }
}

// Update an available room type
const update = async (roomTypeId, roomTypeData) => {
  try {
    const token = getItem('adminToken')
    const response = await axios.put(
      `${BASE_URL}/apartments/${roomTypeData.apartment_id}/available_room_types/${roomTypeId}`,
      roomTypeData,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      },
    )
    return response.data
  } catch (error) {
    console.error('Error updating available room type:', error)
    throw error
  }
}

const del = async (apartmentID, roomTypeId) => {
  try {
    const token = getItem('adminToken')
    const response = await axios.delete(
      `${BASE_URL}/apartments/${apartmentID}/available_room_types/${roomTypeId}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      },
    )
    return response.data
  } catch (error) {
    console.error('Error deleting available room type:', error)
    throw error
  }
}

export { fetchAll, insert, update, del, fetchOne }
