import {
  Table,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  Button,
  Pagination,
  Paper,
  Select,
  MenuItem,
} from '@mui/material'
import { useNavigate, useParams } from 'react-router-dom'
import useEmail from '../../hooks/useEmail'
import useNotification from '../../hooks/useNotificaiton'
import { generateInvoiceHTML } from '../../utils/generalUtils'

function InvoiceTable({
  invoices,
  onStatusChange,
  totalCount,
  currentPage,
  setCurrentPage,
  limit,
  invoiceStatuses,
  statusesLoading,
}) {
  const { rental_id } = useParams()
  const totalPages = Math.ceil(totalCount / limit)
  const navigate = useNavigate()
  const { sendEmail, loading } = useEmail() // Using the email hook
  const notify = useNotification() // Notification hook

  const handlePageChange = (event, newPage) => {
    setCurrentPage(newPage)
  }

  const handleSendEmail = async invoice => {
    const emailData = {
      to_emails: [invoice.rental.user.user_email],
      from_email: 'paingkhant0397@gmail.com',
      subject: `Invoice #${invoice.invoice_id}`,
      html_body: generateInvoiceHTML(invoice),
      body: '',
    }

    try {
      await sendEmail(emailData)
      notify('success', 'Email sent successfully!') // Notify on success
    } catch (error) {
      notify('error', 'Failed to send email.') // Notify on error
    }
  }

  return (
    <div className='p-4 w-full'>
      <div className='mb-5'>
        <Button
          color='primary'
          onClick={() =>
            navigate(`/admin/dashboard/rentals/${rental_id}/invoices/register`)
          }
        >
          Generate Invoice
        </Button>
      </div>
      <Paper elevation={3} className='p-4'>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell align='center'>Invoice ID</TableCell>
              <TableCell align='center'>User Email</TableCell>
              <TableCell align='center'>Water Bill</TableCell>
              <TableCell align='center'>Electricity Bill</TableCell>
              <TableCell align='center'>Total Amount</TableCell>
              <TableCell align='center'>Issued Date</TableCell>
              <TableCell align='center'>Due Date</TableCell>
              <TableCell align='center'>Status</TableCell>
              <TableCell align='center'>Actions</TableCell>
              <TableCell align='center'>Send Email</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {invoices.map(invoice => (
              <TableRow key={invoice.invoice_id} hover>
                <TableCell align='center'>{invoice.invoice_id}</TableCell>
                <TableCell align='center'>
                  {invoice.rental.user.user_email}
                </TableCell>
                <TableCell align='center'>{invoice.water_bill}</TableCell>
                <TableCell align='center'>{invoice.electricity_bill}</TableCell>
                <TableCell align='center'>{invoice.total_amount}</TableCell>
                <TableCell align='center'>{invoice.issued_date}</TableCell>
                <TableCell align='center'>{invoice.due_date}</TableCell>
                <TableCell align='center'>
                  <Select
                    className='w-32'
                    value={invoice.status.invoice_status_id}
                    onChange={e => onStatusChange(invoice, e.target.value)}
                    disabled={statusesLoading}
                  >
                    {invoiceStatuses.map(status => (
                      <MenuItem
                        key={status.invoice_status_id}
                        value={status.invoice_status_id}
                      >
                        {status.invoice_status_name}
                      </MenuItem>
                    ))}
                  </Select>
                </TableCell>
                <TableCell align='center'>
                  <Button
                    variant='outlined'
                    color='primary'
                    onClick={() =>
                      navigate(
                        `/admin/dashboard/rentals/${invoice.rental.rental_id}/invoices/${invoice.invoice_id}/update`,
                      )
                    }
                  >
                    Update
                  </Button>
                </TableCell>
                <TableCell align='center'>
                  {' '}
                  {/* Send Email Button */}
                  <Button
                    variant='contained'
                    color='secondary'
                    onClick={() => handleSendEmail(invoice)}
                    disabled={loading} // Disable button while sending email
                  >
                    Send Email
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
        <div className='flex justify-center mt-4'>
          <Pagination
            count={totalPages}
            page={currentPage}
            onChange={handlePageChange}
            color='primary'
            shape='rounded'
          />
        </div>
      </Paper>
    </div>
  )
}

export default InvoiceTable
