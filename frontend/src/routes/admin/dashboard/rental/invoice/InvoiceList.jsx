import { useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { Button } from '@mui/material'
import useInvoices from '../../../../../hooks/useInvoices'
import InvoiceTable from '../../../../../components/invoice/InvoiceTable'
import Loading from '../../../../../components/Loading'
import useInvoiceStatuses from '../../../../../hooks/useInvoiceStatuses'

function InvoiceList() {
  const { rental_id } = useParams()
  const { invoices, loading, edit, pagination, setPagination } =
    useInvoices(rental_id)
  const navigate = useNavigate()
  const { invoiceStatuses, loading: statusesLoading } = useInvoiceStatuses()
  // console.log(invoices)
  const onStatusChange = (invoice, status_id) => {
    try {
      const updatedInvoice = { ...invoice }

      updatedInvoice.status.invoice_status_id = status_id
      // console.log(updatedInvoice.status.invoice_status_id)
      edit(updatedInvoice.invoice_id, updatedInvoice)
    } catch (err) {
      console.error(err)
    }
  }

  return (
    <div className='min-h-fit flex justify-center items-top bg-gray-100'>
      {loading && <Loading />}

      <InvoiceTable
        invoices={invoices}
        invoiceStatuses={invoiceStatuses}
        statusesLoading={statusesLoading}
        onStatusChange={onStatusChange}
        totalCount={pagination.total}
        currentPage={pagination.offset / pagination.limit + 1}
        setCurrentPage={page =>
          setPagination(prev => ({
            ...prev,
            offset: (page - 1) * pagination.limit,
          }))
        }
        limit={pagination.limit}
      />
    </div>
  )
}

export default InvoiceList
