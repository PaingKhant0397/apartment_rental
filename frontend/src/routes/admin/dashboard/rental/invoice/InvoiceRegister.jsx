import { useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { Button } from '@mui/material'
import useInvoices from '../../../../../hooks/useInvoices'
import InvoiceForm from '../../../../../components/invoice/InvoiceForm'
import useInvoiceStatuses from '../../../../../hooks/useInvoiceStatuses'

function InvoiceRegister() {
  const { rental_id: rentalId } = useParams()
  const navigate = useNavigate()
  const { insert } = useInvoices(rentalId)
  const { invoiceStatuses: statuses, loading: statusesLoading } =
    useInvoiceStatuses()

  const handleRegisterInvoice = async invoiceData => {
    const invoicePayload = {
      rental: { rental_id: rentalId },
      status: {
        invoice_status_id: invoiceData.invoice_status_id,
        invoice_status_name: statuses.find(
          status => status.invoice_status_id === invoiceData.invoice_status_id,
        )?.invoice_status_name,
      },
      water_bill: invoiceData.water_bill,
      electricity_bill: invoiceData.electricity_bill,
      total_amount: invoiceData.total_amount,
      issued_date: invoiceData.issued_date,
      due_date: invoiceData.due_date,
    }

    try {
      await insert(invoicePayload)
      navigate(`/admin/dashboard/rentals/${rentalId}/invoices`)
    } catch (error) {
      console.error('Failed to register invoice', error)
    }
  }

  const handleGoBack = () => {
    navigate(-1)
  }

  if (statusesLoading) return <p>Loading statuses...</p>

  return (
    <div>
      <InvoiceForm
        initialData={{}}
        onSubmit={handleRegisterInvoice}
        statuses={statuses}
        handleGoBack={handleGoBack}
        rentalId={rentalId}
      />
    </div>
  )
}

export default InvoiceRegister
