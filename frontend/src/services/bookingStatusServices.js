import axios from 'axios'

const BASE_URL = `${import.meta.env.VITE_BASE_URL}/api/booking_statuses`

export const fetchAllBookingStatuses = async () => {
  const response = await axios.get(BASE_URL)
  return response.data
}

export const fetchBookingStatusById = async id => {
  const response = await axios.get(`${BASE_URL}/${id}`)
  return response.data
}
