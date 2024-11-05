import axios from 'axios'
import { getItem } from '../utils/localStorageUtils'

const BASE_URL = import.meta.env.VITE_API_URL

const fetchApartments = async (limit = 10, offset = 0) => {
  try {
    const response = await axios.get(`${BASE_URL}/apartments`, {
      params: { limit, offset },
    })
    return response.data
  } catch (error) {
    console.error('Error fetching apartments:', error)
    throw error
  }
}

const fetchApartmentById = async id => {
  try {
    const response = await axios.get(`${BASE_URL}/apartments/${id}`)
    return response.data
  } catch (error) {
    console.error('Error fetching apartments:', error)
    throw error
  }
}
const createApartment = async apartmentData => {
  try {
    const token = getItem('adminToken')

    const response = await axios.post(`${BASE_URL}/apartments`, apartmentData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: `Bearer ${token}`,
      },
    })
    return response
  } catch (error) {
    console.error('Error creating apartment:', error)
    throw error
  }
}

const updateApartment = async (apartmentId, apartmentData) => {
  try {
    const token = getItem('adminToken')
    const response = await axios.put(
      `${BASE_URL}/apartments/${apartmentId}`,
      apartmentData,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `Bearer ${token}`,
        },
      },
    )
    return response.data
  } catch (error) {
    console.error('Error updating apartment:', error)
    throw error
  }
}

const deleteApartment = async apartmentId => {
  try {
    const token = getItem('adminToken')
    const response = await axios.delete(
      `${BASE_URL}/apartments/${apartmentId}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      },
    )
    return response.data
  } catch (error) {
    console.error('Error deleting apartment:', error)
    throw error
  }
}

export {
  fetchApartments,
  fetchApartmentById,
  createApartment,
  updateApartment,
  deleteApartment,
}
