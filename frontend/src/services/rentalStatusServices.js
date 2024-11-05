import axios from 'axios'

const BASE_URL = `${import.meta.env.VITE_BASE_URL}/api/rental_statuses`

export const fetchAllRentalStatuses = async () => {
  const response = await axios.get(BASE_URL)
  return response.data
}

export const fetchRentalStatusById = async id => {
  const response = await axios.get(`${BASE_URL}/${id}`)
  return response.data
}
