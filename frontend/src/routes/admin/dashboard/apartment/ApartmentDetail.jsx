/* eslint-disable react-hooks/exhaustive-deps */
import { useNavigate, useParams } from 'react-router-dom'
import { useState, useEffect } from 'react'
import { Button, Card, CardContent, Typography } from '@mui/material'
import useApartments from '../../../../hooks/useApartments'

const initialData = {
  apartment_id: '',
  apartment_name: '',
  apartment_address: '',
  apartment_desc: '',
  apartment_date_built: '',
  apartment_postal_code: '',
  apartment_capacity: '',
  apartment_image: null,
}

function ApartmentDetail() {
  const [apartment, setApartment] = useState(initialData)
  const { id } = useParams()
  const { getApartment } = useApartments()

  useEffect(() => {
    const getApt = async () => {
      const apt = await getApartment(id)
      setApartment(apt)
    }
    getApt()
  }, [id])

  const navigate = useNavigate()

  const handleBack = () => {
    navigate('/admin/dashboard/apartments')
  }

  const handleManageRooms = () => {
    navigate(`/admin/dashboard/apartments/${id}/rooms`)
  }

  const handleManageRoomTypes = () => {
    navigate(`/admin/dashboard/apartments/${id}/available_room_types`)
  }

  return (
    <div className='min-h-screen h-screen flex justify-center items-start bg-gray-100 py-10'>
      <Card className='w-full '>
        {/* Back Button */}
        <div className='p-4'>
          <Button variant='outlined' onClick={handleBack}>
            Back to Apartments
          </Button>
        </div>

        {/* Apartment Image */}
        <div className='border rounded-md shadow-sm overflow-hidden'>
          <img
            src={`${import.meta.env.VITE_BASE_URL}/${apartment.apartment_image}`}
            alt={apartment.apartment_name}
            className='w-full h-64 object-cover'
          />
        </div>

        {/* Apartment Details */}
        <CardContent>
          <Typography variant='h5' component='h1' className='mb-2'>
            {apartment.apartment_name}
          </Typography>
          <Typography variant='body1' className='mb-1'>
            <strong>Address:</strong> {apartment.apartment_address}
          </Typography>
          <Typography variant='body1' className='mb-1'>
            <strong>Description:</strong> {apartment.apartment_desc}
          </Typography>
          <Typography variant='body1' className='mb-1'>
            <strong>Date Built:</strong> {apartment.apartment_date_built}
          </Typography>
          <Typography variant='body1' className='mb-1'>
            <strong>Postal Code:</strong> {apartment.apartment_postal_code}
          </Typography>
          <Typography variant='body1' className='mb-1'>
            <strong>Capacity:</strong> {apartment.apartment_capacity} people
          </Typography>
        </CardContent>

        {/* Action Buttons */}
        <div className='p-4 flex space-x-4'>
          <Button variant='contained' onClick={handleManageRoomTypes}>
            Manage Room Types
          </Button>
          <Button variant='contained' onClick={handleManageRooms}>
            Manage Rooms
          </Button>
        </div>
      </Card>
    </div>
  )
}

export default ApartmentDetail
