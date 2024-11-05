import axios from 'axios'

const BASE_URL = `${import.meta.env.VITE_BASE_URL}/api/room_statuses`

export const fetchAllRoomStatuses = async () => {
  const response = await axios.get(BASE_URL)
  return response.data
}

export const fetchRoomStatusById = async id => {
  const response = await axios.get(`${BASE_URL}/${id}`)
  return response.data
}
