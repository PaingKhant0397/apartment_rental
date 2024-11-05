import { useEffect, useState } from 'react'
import {
  fetchAllRoomStatuses,
  fetchRoomStatusById,
} from '../services/roomStatusServices'
import useNotification from './useNotificaiton'

const useRoomStatuses = () => {
  const [roomStatuses, setRoomStatuses] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const notify = useNotification()

  const getAllRoomStatuses = async () => {
    setLoading(true)
    try {
      const data = await fetchAllRoomStatuses()
      setRoomStatuses(data)
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load room statuses')
    } finally {
      setLoading(false)
    }
  }

  const getRoomStatusById = async id => {
    setLoading(true)
    try {
      const status = await fetchRoomStatusById(id)
      return status
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load room status details')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    getAllRoomStatuses() // Fetch room statuses on mount
  }, [])

  return {
    roomStatuses,
    loading,
    error,
    getRoomStatusById,
  }
}

export default useRoomStatuses
