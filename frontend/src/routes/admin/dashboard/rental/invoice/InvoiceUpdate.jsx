import React, { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import useInvoices from '../../../../../hooks/useInvoices'
import useInvoiceStatuses from '../../../../../hooks/useInvoiceStatuses' // Import the hook for fetching statuses
import InvoiceUpdateForm from '../../../../../components/invoice/InvoiceUpdateForm'

function InvoiceUpdate() {
  const { invoice_id: invoiceId, rental_id: rentalId } = useParams()
  const navigate = useNavigate()
  const { getById, edit } = useInvoices(rentalId)
  const { invoiceStatuses: statuses } = useInvoiceStatuses() // Use the statuses hook
  const [initialData, setInitialData] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchInvoice = async () => {
      if (invoiceId) {
        setLoading(true)
        const invoiceData = await getById(invoiceId)

        setInitialData(invoiceData)
        setLoading(false)
      }
    }

    fetchInvoice()
  }, [invoiceId])

  const handleUpdate = async updatedData => {
    try {
      await edit(invoiceId, { ...updatedData, invoice_id: invoiceId })
      navigate(`/admin/dashboard/rentals/${rentalId}/invoices`)
    } catch (error) {
      console.error('Failed to update invoice:', error)
    }
  }

  const handleGoBack = () => {
    navigate(`/admin/dashboard/rentals/${rentalId}/invoices`)
  }

  if (loading || !initialData) return <p>Loading...</p>

  return (
    <InvoiceUpdateForm
      initialData={initialData}
      onUpdate={handleUpdate}
      statuses={statuses} // Pass the statuses to the InvoiceUpdateForm
      handleGoBack={handleGoBack}
    />
  )
}

export default InvoiceUpdate
