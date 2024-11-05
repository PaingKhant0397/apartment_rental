import React, { useEffect, useState } from 'react'
import {
  TextField,
  Button,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Card,
  CardContent,
  Typography,
  Box,
} from '@mui/material'

function InvoiceUpdateForm({ initialData, onUpdate, statuses, handleGoBack }) {
  const [waterBill, setWaterBill] = useState(0)
  const [electricityBill, setElectricityBill] = useState(0)
  const [invoiceStatus, setInvoiceStatus] = useState({})
  const [issuedDate, setIssuedDate] = useState('')
  const [dueDate, setDueDate] = useState('')
  const [totalAmount, setTotalAmount] = useState(0)
  const availableRoomTypePrice =
    initialData.rental.room.available_room_type.available_room_type_price // Access the room type price from initialData

  useEffect(() => {
    if (initialData) {
      setWaterBill(initialData.water_bill)
      setElectricityBill(initialData.electricity_bill)
      setInvoiceStatus(initialData.status) // Set the full status object
      setIssuedDate(initialData.issued_date)
      setDueDate(initialData.due_date)
      setTotalAmount(initialData.total_amount) // Set the initial total amount
    }
  }, [initialData])

  useEffect(() => {
    // Calculate total amount whenever water bill or electricity bill changes
    const calculateTotalAmount = () => {
      const total = waterBill + electricityBill + availableRoomTypePrice
      setTotalAmount(total)
    }

    calculateTotalAmount()
  }, [waterBill, electricityBill, availableRoomTypePrice])

  const handleSubmit = e => {
    e.preventDefault()
    onUpdate({
      water_bill: waterBill,
      electricity_bill: electricityBill,
      status: {
        invoice_status_id: invoiceStatus.invoice_status_id,
        invoice_status_name: invoiceStatus.invoice_status_name, // Include status name
      },
      issued_date: issuedDate,
      due_date: dueDate,
      total_amount: totalAmount, // Total amount is calculated
    })
  }

  return (
    <Card sx={{ width: 'full', margin: 'auto', mt: 4 }}>
      <CardContent>
        <Typography variant='h5' component='div' gutterBottom>
          Update Invoice
        </Typography>
        <form onSubmit={handleSubmit}>
          <Box mb={2}>
            <TextField
              label='Water Bill'
              type='number'
              value={waterBill}
              onChange={e => setWaterBill(parseFloat(e.target.value))}
              fullWidth
              margin='normal'
              required
            />
            <TextField
              label='Electricity Bill'
              type='number'
              value={electricityBill}
              onChange={e => setElectricityBill(parseFloat(e.target.value))}
              fullWidth
              margin='normal'
              required
            />
            <FormControl fullWidth margin='normal' required>
              <InputLabel>Invoice Status</InputLabel>
              <Select
                value={invoiceStatus.invoice_status_id || ''}
                onChange={e => {
                  const selectedStatus = statuses.find(
                    status => status.invoice_status_id === e.target.value,
                  )
                  setInvoiceStatus(selectedStatus || {})
                }}
              >
                {statuses.map(status => (
                  <MenuItem
                    key={status.invoice_status_id}
                    value={status.invoice_status_id}
                  >
                    {status.invoice_status_name}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
            <TextField
              label='Issued Date'
              type='date'
              value={issuedDate}
              onChange={e => setIssuedDate(e.target.value)}
              fullWidth
              margin='normal'
              InputLabelProps={{
                shrink: true,
              }}
              required
            />
            <TextField
              label='Due Date'
              type='date'
              value={dueDate}
              onChange={e => setDueDate(e.target.value)}
              fullWidth
              margin='normal'
              InputLabelProps={{
                shrink: true,
              }}
              required
            />
            <TextField
              label='Total Amount'
              type='number'
              value={totalAmount}
              InputProps={{
                readOnly: true,
              }}
              fullWidth
              margin='normal'
            />
          </Box>
          <Box display='flex' justifyContent='space-between' mt={2}>
            <Button type='submit' variant='contained' color='primary'>
              Update Invoice
            </Button>
            <Button
              variant='outlined'
              onClick={handleGoBack}
              style={{ marginLeft: '10px' }}
            >
              Go Back
            </Button>
          </Box>
        </form>
      </CardContent>
    </Card>
  )
}

export default InvoiceUpdateForm
