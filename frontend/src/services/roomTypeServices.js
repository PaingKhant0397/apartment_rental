// src/services/roomTypeService.js
import axios from 'axios'

const BASE_URL = 'http://127.0.0.1:8080/api'

// Get all room types
const getAll = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/room_types`)
    return response.data
  } catch (error) {
    console.error('Error fetching room types:', error)
    throw error
  }
}

export default getAll
