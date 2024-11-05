/* eslint-disable react-hooks/exhaustive-deps */
import React, { useEffect, useState } from 'react'
import {
  Button,
  Card,
  CardContent,
  CardHeader,
  Grid,
  Typography,
} from '@mui/material'
import InputField from '../InputField'
import useRentals from '../../hooks/useRentals' // Import your useRentals hook

function InvoiceForm({
  initialData = {},
  onSubmit,
  statuses,
  handleGoBack,
  rentalId,
}) {
  const [formData, setFormData] = useState({
    water_bill: initialData.water_bill || '',
    electricity_bill: initialData.electricity_bill || '',
    total_amount: initialData.total_amount || '',
    issued_date: initialData.issued_date || '',
    due_date: initialData.due_date || '',
    invoice_status_id: initialData.status?.invoice_status_id || '',
  })
  const [errors, setErrors] = useState({})
  const { getById } = useRentals()
  const [roomTypePrice, setRoomTypePrice] = useState(0)

  const calculateTotalAmount = (waterBill, electricityBill, roomPrice) => {
    const water = parseFloat(waterBill) || 0
    const electricity = parseFloat(electricityBill) || 0
    return water + electricity + roomPrice
  }

  useEffect(() => {
    const fetchRentalInfo = async () => {
      console.log('rental id', rentalId)
      if (rentalId) {
        const rentalData = await getById(rentalId)
        // console.log('rental data', rentalData)
        if (rentalData) {
          setRoomTypePrice(
            rentalData.room.available_room_type.available_room_type_price || 0,
          )
          setFormData(prev => ({
            ...prev,
            total_amount: calculateTotalAmount(
              prev.water_bill,
              prev.electricity_bill,
              rentalData.room.available_room_type.available_room_type_price,
            ),
          }))
        }
      }
    }

    fetchRentalInfo()
  }, [rentalId])

  const handleChange = e => {
    const { name, value } = e.target
    setFormData(prev => {
      const updatedForm = { ...prev, [name]: value }
      return {
        ...updatedForm,
        total_amount: calculateTotalAmount(
          updatedForm.water_bill,
          updatedForm.electricity_bill,
          roomTypePrice,
        ),
      }
    })
    setErrors(prev => ({ ...prev, [name]: '' })) // Clear error on change
  }

  const handleSubmit = e => {
    e.preventDefault()
    const newErrors = {}
    if (!formData.water_bill) newErrors.water_bill = 'Water bill is required'
    if (!formData.electricity_bill)
      newErrors.electricity_bill = 'Electricity bill is required'
    if (!formData.total_amount)
      newErrors.total_amount = 'Total amount is required'
    if (!formData.issued_date) newErrors.issued_date = 'Issued date is required'
    if (!formData.due_date) newErrors.due_date = 'Due date is required'
    if (!formData.invoice_status_id)
      newErrors.invoice_status_id = 'Status is required'

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors)
      return
    }

    onSubmit(formData)
  }

  return (
    <Card variant='outlined' sx={{ margin: 2 }}>
      <CardHeader title='Register Invoice' />
      <CardContent>
        <form onSubmit={handleSubmit}>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={12}>
              <InputField
                id='water_bill'
                label='Water Bill'
                type='number'
                value={formData.water_bill}
                onChange={handleChange}
                error={errors.water_bill}
                required
              />
            </Grid>
            <Grid item xs={12} sm={12}>
              <InputField
                id='electricity_bill'
                label='Electricity Bill'
                type='number'
                value={formData.electricity_bill}
                onChange={handleChange}
                error={errors.electricity_bill}
                required
              />
            </Grid>

            <Grid item xs={12} sm={12}>
              <InputField
                id='issued_date'
                label='Issued Date'
                type='date'
                value={formData.issued_date}
                onChange={handleChange}
                error={errors.issued_date}
                required
              />
            </Grid>
            <Grid item xs={12} sm={12}>
              <InputField
                id='due_date'
                label='Due Date'
                type='date'
                value={formData.due_date}
                onChange={handleChange}
                error={errors.due_date}
                required
              />
            </Grid>
            <Grid item xs={12}>
              <InputField
                id='invoice_status_id'
                label='Status'
                type='select'
                value={formData.invoice_status_id}
                onChange={handleChange}
                error={errors.invoice_status_id}
                required
                options={statuses.map(status => ({
                  value: status.invoice_status_id,
                  label: status.invoice_status_name,
                }))}
              />
            </Grid>
            <Grid item xs={12} sm={12}>
              <Typography variant='h6'>
                Total Amount: ${formData.total_amount}
              </Typography>
            </Grid>
            <Grid item xs={12}>
              <Button
                type='submit'
                variant='contained'
                color='primary'
                fullWidth
                sx={{ marginBottom: 1 }} // Add margin for spacing
              >
                Submit
              </Button>
              <Button
                variant='outlined'
                color='secondary'
                onClick={handleGoBack}
                fullWidth
              >
                Go Back
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </Card>
  )
}

export default InvoiceForm
