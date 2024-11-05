/* eslint-disable camelcase */
import axios from 'axios'
import { getItem } from '../utils/localStorageUtils'

const BASE_URL = `${import.meta.env.VITE_BASE_URL}/api/rentals`

const fetchAll = async (limit = 10, offset = 0) => {
  try {
    const response = await axios.get(`${BASE_URL}`, {
      params: { limit, offset },
      headers: {
        Authorization: `Bearer ${getItem('adminToken')}`,
      },
    })
    return response.data
  } catch (error) {
    console.error('Error fetching rentals:', error)
    throw error
  }
}

const fetchById = async rentalId => {
  try {
    const response = await axios.get(`${BASE_URL}/${rentalId}`, {
      headers: {
        Authorization: `Bearer ${getItem('adminToken')}`,
      },
    })
    return response.data
  } catch (error) {
    console.error('Error fetching rental:', error)
    throw error
  }
}

const insert = async rentalData => {
  try {
    const response = await axios.post(`${BASE_URL}`, rentalData, {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${getItem('adminToken')}`,
      },
    })
    return response.data
  } catch (error) {
    console.error('Error creating rental:', error)
    throw error
  }
}

const update = async (rentalId, rentalData) => {
  try {
    const response = await axios.put(`${BASE_URL}/${rentalId}`, rentalData, {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${getItem('adminToken')}`,
      },
    })
    return response.data
  } catch (error) {
    console.error('Error updating rental:', error)
    throw error
  }
}

const del = async rentalId => {
  try {
    await axios.delete(`${BASE_URL}/${rentalId}`, {
      headers: {
        Authorization: `Bearer ${getItem('adminToken')}`,
      },
    })
  } catch (error) {
    console.error('Error deleting rental:', error)
    throw error
  }
}

export { fetchAll, fetchById, insert, update, del }
