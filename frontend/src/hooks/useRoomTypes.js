import { useState, useEffect } from 'react'
import getAll from '../services/roomTypeServices'
// import useNotification from './useNotificaiton'

const useRoomTypes = () => {
  const [roomTypes, setRoomTypes] = useState([])

  // const notify = useNotification()
  useEffect(() => {
    const getAllRoomTypes = async () => {
      try {
        const rt = await getAll()
        setRoomTypes(rt)
      } catch (error) {
        console.error(error)
        // notify('error', 'Error getting room types')
      }
    }
    getAllRoomTypes()
  }, [])

  return { roomTypes }
}

export default useRoomTypes
