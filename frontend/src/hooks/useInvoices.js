import { useEffect, useState } from 'react'
import {
  fetchAll,
  fetchById,
  create,
  update,
  del,
} from '../services/invoiceServices'
import useNotification from './useNotificaiton'

const useInvoices = rentalId => {
  const [invoices, setInvoices] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [pagination, setPagination] = useState({
    limit: 10,
    offset: 0,
    total: 0,
  })

  const notify = useNotification()

  const getAllInvoices = async () => {
    setLoading(true)
    try {
      const data = await fetchAll(rentalId, pagination.limit, pagination.offset)
      if (!data) {
        setPagination(prev => ({ ...prev, total: 0 }))
        return
      }
      setInvoices(data.data)
      setPagination(prev => ({ ...prev, total: data.total_count }))
    } catch (err) {
      setError(err)
      // notify('error', 'Failed to load invoices')
    } finally {
      setLoading(false)
    }
  }

  const getById = async invoiceId => {
    setLoading(true)
    try {
      const invoice = await fetchById(rentalId, invoiceId)
      return invoice
    } catch (err) {
      setError(err)
      notify('error', 'Failed to load invoice details')
    } finally {
      setLoading(false)
    }
  }

  const insert = async invoiceData => {
    setLoading(true)
    try {
      const newInvoice = await create(rentalId, invoiceData)
      setInvoices(prev => [...prev, newInvoice])
      notify('success', 'Invoice created successfully')
    } catch (err) {
      setError(err)
      notify('error', 'Failed to create invoice')
    } finally {
      setLoading(false)
    }
  }

  const edit = async (invoiceId, invoiceData) => {
    setLoading(true)
    try {
      const updatedInvoice = await update(rentalId, invoiceId, invoiceData)
      setInvoices(prev =>
        prev.map(invoice =>
          invoice.invoice_id === invoiceId ? updatedInvoice : invoice,
        ),
      )
      notify('success', 'Invoice updated successfully')
    } catch (err) {
      setError(err)
      notify('error', 'Failed to update invoice')
    } finally {
      setLoading(false)
    }
  }

  const remove = async invoiceId => {
    setLoading(true)
    try {
      await del(rentalId, invoiceId)
      setInvoices(prev =>
        prev.filter(invoice => invoice.invoice_id !== invoiceId),
      )
      notify('success', 'Invoice deleted successfully')
    } catch (err) {
      setError(err)
      notify('error', 'Failed to delete invoice')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    if (rentalId) {
      getAllInvoices()
    }
  }, [rentalId, pagination.limit, pagination.offset])

  return {
    invoices,
    loading,
    error,
    pagination,
    getById,
    insert,
    edit,
    remove,
    setPagination,
  }
}

export default useInvoices
