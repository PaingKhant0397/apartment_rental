import { useEffect, useState } from 'react'
import {
  fetchAllRentalStatuses,
  fetchRentalStatusById,
} from '../services/rentalStatusServices'
import useNotification from './useNotificaiton'

const useRentalStatuses = () => {
  const [rentalStatuses, setRentalStatuses] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const notify = useNotification()

  const getAllRentalStatuses = async () => {
    setLoading(true)
    try {
      const data = await fetchAllRentalStatuses()
      setRentalStatuses(data)
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load rental statuses')
    } finally {
      setLoading(false)
    }
  }

  const getRentalStatusById = async id => {
    setLoading(true)
    try {
      const status = await fetchRentalStatusById(id)
      return status
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load rental status details')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    getAllRentalStatuses() // Fetch rental statuses on mount
  }, [])

  return {
    rentalStatuses,
    loading,
    error,
    getRentalStatusById,
  }
}

export default useRentalStatuses
