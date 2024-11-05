import axios from 'axios'
import { getItem } from '../utils/localStorageUtils'

const BASE_URL = `${import.meta.env.VITE_BASE_URL}/api`

const fetchAll = async (limit = 10, offset = 0) => {
  try {
    const response = await axios.get(`${BASE_URL}/bookings`, {
      params: { limit, offset },
      headers: {
        Authorization: `Bearer ${getItem('adminToken')}`,
      },
    })
    return response.data // Ensure this includes both bookings and total count
  } catch (error) {
    console.error('Error fetching bookings:', error)
    throw error
  }
}

const fetchById = async bookingId => {
  try {
    const response = await axios.get(`${BASE_URL}/bookings/${bookingId}`, {
      headers: {
        Authorization: `Bearer ${getItem('adminToken')}`,
      },
    })
    return response.data
  } catch (error) {
    console.error('Error fetching booking:', error)
    throw error
  }
}

const insert = async bookingData => {
  try {
    const response = await axios.post(`${BASE_URL}/bookings`, bookingData, {
      headers: {
        'Content-Type': 'application/json',
      },
    })
    return response.data
  } catch (error) {
    console.error('Error creating booking:', error)
    throw error
  }
}

const update = async (bookingId, bookingData) => {
  try {
    const response = await axios.put(
      `${BASE_URL}/bookings/${bookingId}`,
      bookingData,
      {
        headers: {
          'Content-Type': 'application/json',
        },
      },
    )
    return response.data
  } catch (error) {
    console.error('Error updating booking:', error)
    throw error
  }
}

const del = async bookingId => {
  try {
    await axios.delete(`${BASE_URL}/bookings/${bookingId}`, {
      headers: {
        Authorization: `Bearer ${getItem('adminToken')}`,
      },
    })
  } catch (error) {
    console.error('Error deleting booking:', error)
    throw error
  }
}

export { fetchAll, fetchById, insert, update, del }
