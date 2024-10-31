/* eslint-disable react-hooks/exhaustive-deps */
import { useNavigate, useParams } from 'react-router-dom'
import { useState, useEffect } from 'react'
import useApartments from '../../../../hooks/useApartments'
import Button from '../../../../components/Button'

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
    <div className='min-h-screen flex justify-center items-start bg-gray-100 py-10'>
      <div className='bg-white p-8 w-full max-w-3xl rounded-lg shadow-lg'>
        {/* Back Button */}
        <div className='mb-6'>
          <Button onClick={handleBack} variant='secondary'>
            Back to Apartments
          </Button>
        </div>

        {/* Apartment Image */}
        <div className='border rounded-md shadow-sm overflow-hidden mb-6'>
          <img
            src={`${import.meta.env.VITE_BASE_URL}/${apartment.apartment_image}`}
            alt={apartment.apartment_name}
            className='w-full h-64 object-cover'
          />
        </div>

        {/* Apartment Details */}
        <h1 className='text-2xl font-bold mb-4'>{apartment.apartment_name}</h1>
        <p className='mb-2 text-gray-700'>
          <strong>Address:</strong> {apartment.apartment_address}
        </p>
        <p className='mb-2 text-gray-700'>
          <strong>Description:</strong> {apartment.apartment_desc}
        </p>
        <p className='mb-2 text-gray-700'>
          <strong>Date Built:</strong> {apartment.apartment_date_built}
        </p>
        <p className='mb-2 text-gray-700'>
          <strong>Postal Code:</strong> {apartment.apartment_postal_code}
        </p>
        <p className='mb-2 text-gray-700'>
          <strong>Capacity:</strong> {apartment.apartment_capacity} people
        </p>

        {/* Action Buttons */}
        <div className='flex space-x-4 mt-8'>
          <Button onClick={handleManageRoomTypes}>Manage Room Types</Button>
          <Button onClick={handleManageRooms}>Manage Rooms</Button>
        </div>
      </div>
    </div>
  )
}

export default ApartmentDetail
