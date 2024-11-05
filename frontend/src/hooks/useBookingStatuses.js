import { useEffect, useState } from 'react'
import {
  fetchAllBookingStatuses,
  fetchBookingStatusById,
} from '../services/bookingStatusServices'
import useNotification from './useNotificaiton'

const useBookingStatuses = () => {
  const [bookingStatuses, setBookingStatuses] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const notify = useNotification()

  const getAllBookingStatuses = async () => {
    setLoading(true)
    try {
      const data = await fetchAllBookingStatuses()
      setBookingStatuses(data)
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load booking statuses')
    } finally {
      setLoading(false)
    }
  }

  const getBookingStatusById = async id => {
    setLoading(true)
    try {
      const status = await fetchBookingStatusById(id)
      return status
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load booking status details')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    getAllBookingStatuses() // Fetch booking statuses on mount
  }, [])

  return {
    bookingStatuses,
    loading,
    error,
    getBookingStatusById,
  }
}

export default useBookingStatuses
