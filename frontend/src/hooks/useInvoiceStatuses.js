import { useEffect, useState } from 'react'
import {
  fetchAllInvoiceStatuses,
  fetchInvoiceStatusById,
} from '../services/invoiceStatusServices'
import useNotification from './useNotificaiton'

const useInvoiceStatuses = () => {
  const [invoiceStatuses, setInvoiceStatuses] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const notify = useNotification()

  const getAllInvoiceStatuses = async () => {
    setLoading(true)
    try {
      const data = await fetchAllInvoiceStatuses()
      setInvoiceStatuses(data)
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load invoice statuses')
    } finally {
      setLoading(false)
    }
  }

  const getInvoiceStatusById = async id => {
    setLoading(true)
    try {
      const status = await fetchInvoiceStatusById(id)
      return status
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load invoice status details')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    getAllInvoiceStatuses() // Fetch invoice statuses on mount
  }, [])

  return {
    invoiceStatuses,
    loading,
    error,
    getInvoiceStatusById,
  }
}

export default useInvoiceStatuses
